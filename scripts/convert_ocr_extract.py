#!/usr/bin/env python3
"""
Convert all documents to PDF, OCR the PDFs, and extract all text from the OCR PDFs.
DLCD Course Documents Pipeline.
"""

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path
import json
import pymupdf

ROOT_DIR = Path(__file__).resolve().parent.parent

OFFICE_DOCS = [
    ROOT_DIR / "lab/week8/PES2UG25CS615_Yashwanth K_DLCDLab8.docx",
    ROOT_DIR / "resources/QB.doc",
    ROOT_DIR / "resources/U1QB_soln.docx",
    ROOT_DIR / "resources/U2MCQ1.docx",
    ROOT_DIR / "resources/U2MCQ2.docx",
    ROOT_DIR / "resources/U2QB.docx",
    ROOT_DIR / "resources/U2QB_soln.docx",
    ROOT_DIR / "resources/u3/3/Assignments/3.1.1_ASSIGNMENT.docx",
    ROOT_DIR / "resources/u3/3/Slides/3.1.1_Sequential_Building_Block.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.3.1_Memory_Arrays.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.6.1_Introduction.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.7.1_Assembly_Language.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.9.1_Machine_Language.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.11.1_Programming.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.14.1_Addressing_Mode.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.14.2_COM-ASS-LOAD.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.15.1_Parallelism.pptx",
    ROOT_DIR / "resources/u3/3/Slides/3.17.1_Classwork_problems.pptx",
]

IMAGE_DOCS = [
    ROOT_DIR / "notes/question1.jpeg",
    ROOT_DIR / "notes/sequential-1.jpg",
    ROOT_DIR / "notes/sequential-2.jpg",
]

PREEXISTING_PDFS = [
    ROOT_DIR / "notes/FSM.pdf",
    ROOT_DIR / "notes/U2N1.pdf",
    ROOT_DIR / "notes/U2N2.pdf",
    ROOT_DIR / "resources/DLCD - Unit 1 Combined Slides.pdf",
    ROOT_DIR / "resources/DLCD - Unit 2 Combined Slides.pdf",
    ROOT_DIR / "resources/U2MCQ3.pdf",
    ROOT_DIR / "resources/u3/QA/3.1.1_QA.pdf",
    ROOT_DIR / "resources/u3/QB/3.1.1_QB.pdf",
]

OUTPUT_DIR = ROOT_DIR / "output_ocr"
OUTPUT_PDF_DIR = OUTPUT_DIR / "pdfs"
OUTPUT_TXT_DIR = OUTPUT_DIR / "text"


def convert_office_to_pdf(doc_path: Path) -> Path:
    """Convert .doc, .docx, .pptx to .pdf using LibreOffice."""
    out_dir = doc_path.parent
    pdf_path = out_dir / (doc_path.stem + ".pdf")
    if pdf_path.exists() and pdf_path.stat().st_mtime > doc_path.stat().st_mtime:
        print(f"[CONVERT] Office -> PDF already up-to-date: {pdf_path.relative_to(ROOT_DIR)}")
        return pdf_path

    cmd = [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        str(doc_path),
        "--outdir",
        str(out_dir),
    ]
    print(f"[CONVERT] Office -> PDF: {doc_path.relative_to(ROOT_DIR)} ...")
    start = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Conversion failed for {doc_path}: {res.stderr}")
    if not pdf_path.exists():
        raise FileNotFoundError(f"Expected converted PDF not found: {pdf_path}")
    print(f"  -> Created {pdf_path.relative_to(ROOT_DIR)} in {time.time() - start:.1f}s")
    return pdf_path


def convert_image_to_pdf(img_path: Path) -> Path:
    """Convert an image note (.jpg, .jpeg) to PDF using PyMuPDF."""
    pdf_path = img_path.parent / (img_path.stem + ".pdf")
    if pdf_path.exists() and pdf_path.stat().st_mtime > img_path.stat().st_mtime:
        print(f"[CONVERT] Image -> PDF already up-to-date: {pdf_path.relative_to(ROOT_DIR)}")
        return pdf_path

    print(f"[CONVERT] Image -> PDF: {img_path.relative_to(ROOT_DIR)} ...")
    doc = pymupdf.open()
    img = pymupdf.open(img_path)
    rect = img[0].rect
    pdfbytes = img.convert_to_pdf()
    img_pdf = pymupdf.open("pdf", pdfbytes)
    page = doc.new_page(width=rect.width, height=rect.height)
    page.show_pdf_page(rect, img_pdf, 0)
    doc.save(str(pdf_path))
    doc.close()
    img.close()
    print(f"  -> Created {pdf_path.relative_to(ROOT_DIR)}")
    return pdf_path


def ocr_pdf(input_pdf: Path, output_pdf: Path) -> Path:
    """Run OCRmyPDF to generate searchable PDF with OCR layer."""
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    
    # If output_pdf already exists and is non-empty, check if valid
    if output_pdf.exists() and output_pdf.stat().st_size > 1000:
        try:
            d = pymupdf.open(output_pdf)
            if len(d) > 0:
                print(f"[OCR] Skipping already OCR'd: {output_pdf.name}")
                d.close()
                return output_pdf
            d.close()
        except Exception:
            pass

    temp_output = output_pdf.with_name(output_pdf.stem + ".tmp.pdf")
    if temp_output.exists():
        temp_output.unlink()
        
    cmd = [
        "uvx",
        "ocrmypdf",
        "--redo-ocr",
        "--output-type",
        "pdf",
        "--invalidate-digital-signatures",
        "--tesseract-timeout",
        "300",
        "-j",
        "16",
        str(input_pdf),
        str(temp_output),
    ]
    print(f"[OCR] Processing ({input_pdf.name}) ...")
    start = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        # Fall back to --skip-text if redo-ocr encountered tagged structure conflicts
        print(f"  [INFO] redo-ocr returned code {res.returncode}. Retrying with --skip-text...")
        cmd_fallback = [
            "uvx",
            "ocrmypdf",
            "--skip-text",
            "--output-type",
            "pdf",
            "--invalidate-digital-signatures",
            "--tesseract-timeout",
            "300",
            "-j",
            "16",
            str(input_pdf),
            str(temp_output),
        ]
        res_fb = subprocess.run(cmd_fallback, capture_output=True, text=True)
        if res_fb.returncode != 0:
            raise RuntimeError(f"OCR failed for {input_pdf}: {res.stderr}\nFallback: {res_fb.stderr}")
            
    temp_output.replace(output_pdf)
    elapsed = time.time() - start
    print(f"  -> Completed OCR for {output_pdf.name} in {elapsed:.1f}s")
    return output_pdf


def extract_text_from_pdf(pdf_path: Path, out_txt_path: Path, orig_name: str) -> dict:
    """Extract all text with page layout and structure using PyMuPDF and pdftotext."""
    out_txt_path.parent.mkdir(parents=True, exist_ok=True)
    
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    page_texts = []
    total_words = 0
    total_chars = 0
    
    for page_idx in range(total_pages):
        page = doc[page_idx]
        text = page.get_text("text").strip()
        words = len(text.split())
        total_words += words
        total_chars += len(text)
        page_texts.append(f"--- [Page {page_idx + 1} of {total_pages}] ---\n{text}\n")
        
    doc.close()
    
    structured_content = (
        f"================================================================================\n"
        f"ORIGINAL DOCUMENT : {orig_name}\n"
        f"OCR PDF FILE      : {pdf_path.name}\n"
        f"TOTAL PAGES       : {total_pages}\n"
        f"WORD COUNT        : {total_words}\n"
        f"CHARACTER COUNT   : {total_chars}\n"
        f"DATE EXTRACTED    : {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"================================================================================\n\n"
        + "\n".join(page_texts)
    )
    
    out_txt_path.write_text(structured_content, encoding="utf-8")
    print(f"[EXTRACT] Saved text: {out_txt_path.name} ({total_pages} pages, {total_words} words)")
    return {
        "pages": total_pages,
        "words": total_words,
        "chars": total_chars,
    }


def get_disambiguated_name(file_path: Path) -> str:
    rel = str(file_path.relative_to(ROOT_DIR))
    stem = file_path.stem
    if "u3/3/Slides" in rel:
        return f"U3_Slides_{stem}"
    elif "u3/3/Assignments" in rel:
        return f"U3_Assignment_{stem}"
    elif "u3/QA" in rel:
        return f"U3_QA_{stem}"
    elif "u3/QB" in rel:
        return f"U3_QB_{stem}"
    elif "notes" in rel:
        return f"Notes_{stem}"
    elif "lab" in rel:
        return f"Lab_{stem}"
    elif "resources" in rel:
        return f"Resources_{stem}"
    return stem


def main():
    OUTPUT_PDF_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_TXT_DIR.mkdir(parents=True, exist_ok=True)
    
    all_docs = []
    
    print("=== STEP 1: CONVERTING OFFICE DOCUMENTS TO PDF ===")
    for doc in OFFICE_DOCS:
        if not doc.exists():
            print(f"[SKIP] Document not found: {doc}")
            continue
        pdf_path = convert_office_to_pdf(doc)
        all_docs.append((doc, pdf_path))
        
    print("\n=== STEP 1.5: CONVERTING NOTE IMAGES TO PDF ===")
    for img in IMAGE_DOCS:
        if not img.exists():
            print(f"[SKIP] Image not found: {img}")
            continue
        pdf_path = convert_image_to_pdf(img)
        all_docs.append((img, pdf_path))
        
    print("\n=== STEP 1.8: ADDING PRE-EXISTING PDFS ===")
    for pdf in PREEXISTING_PDFS:
        if not pdf.exists():
            print(f"[SKIP] PDF not found: {pdf}")
            continue
        all_docs.append((pdf, pdf))
        
    print(f"\nTotal documents to OCR and extract: {len(all_docs)}")
    
    # Sort by page count (ascending) so small files finish first and large files last
    def get_pages(item):
        _, pdf_p = item
        try:
            d = pymupdf.open(pdf_p)
            c = len(d)
            d.close()
            return c
        except Exception:
            return 999
            
    all_docs.sort(key=get_pages)
    
    print("\nProcessing order by page count:")
    for idx, (orig, pdf) in enumerate(all_docs, 1):
        pages = get_pages((orig, pdf))
        print(f"  {idx:2d}. [{pages:3d} pages] {orig.relative_to(ROOT_DIR)}")
        
    print("\n=== STEP 2: OCRING PDFS & STEP 3: EXTRACTING TEXT ===")
    summary_report = []
    total_start = time.time()
    
    for idx, (orig_file, pdf_path) in enumerate(all_docs, 1):
        safe_name = get_disambiguated_name(orig_file)
        central_ocr_pdf = OUTPUT_PDF_DIR / f"{safe_name}_ocr.pdf"
        central_txt = OUTPUT_TXT_DIR / f"{safe_name}.txt"
        local_txt = pdf_path.parent / f"{pdf_path.stem}.txt"
        
        pages = get_pages((orig_file, pdf_path))
        print(f"\n[{idx}/{len(all_docs)}] ({pages} pages) {orig_file.name}")
        
        # 1. OCR
        t0 = time.time()
        ocr_pdf(pdf_path, central_ocr_pdf)
        ocr_time = time.time() - t0
        
        # 2. Extract Text
        stats = extract_text_from_pdf(central_ocr_pdf, central_txt, orig_file.name)
        
        # Also copy to local txt beside the source document
        shutil.copyfile(central_txt, local_txt)
        
        summary_report.append({
            "identifier": safe_name,
            "original_file": str(orig_file.relative_to(ROOT_DIR)),
            "pdf_file": str(pdf_path.relative_to(ROOT_DIR)),
            "ocr_pdf_file": str(central_ocr_pdf.relative_to(ROOT_DIR)),
            "extracted_text_file": str(central_txt.relative_to(ROOT_DIR)),
            "local_text_file": str(local_txt.relative_to(ROOT_DIR)),
            "pages": stats["pages"],
            "words": stats["words"],
            "chars": stats["chars"],
            "ocr_time_seconds": round(ocr_time, 2),
        })
        
    # Write summary JSON
    report_path = OUTPUT_DIR / "ocr_extraction_summary.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(summary_report, f, indent=2)
        
    # Write summary README.md
    readme_path = OUTPUT_DIR / "README.md"
    readme_lines = [
        "# DLCD Course Document OCR and Text Extraction Summary",
        "",
        f"Pipeline completed on: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total documents processed: **{len(summary_report)}**",
        f"Total pages: **{sum(s['pages'] for s in summary_report)}**",
        f"Total words extracted: **{sum(s['words'] for s in summary_report):,}**",
        "",
        "## Summary Table",
        "",
        "| # | Document | Pages | Words | OCR PDF | Extracted Text |",
        "|---|----------|-------|-------|---------|----------------|",
    ]
    for i, s in enumerate(summary_report, 1):
        readme_lines.append(
            f"| {i} | `{s['original_file']}` | {s['pages']} | {s['words']:,} | [{Path(s['ocr_pdf_file']).name}](file://{OUTPUT_PDF_DIR / Path(s['ocr_pdf_file']).name}) | [{Path(s['extracted_text_file']).name}](file://{OUTPUT_TXT_DIR / Path(s['extracted_text_file']).name}) |"
        )
        
    readme_path.write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
    
    print(f"\n=======================================================")
    print(f"ALL DONE in {time.time() - total_start:.1f}s!")
    print(f"Summary JSON: {report_path.relative_to(ROOT_DIR)}")
    print(f"Summary Markdown: {readme_path.relative_to(ROOT_DIR)}")
    print(f"=======================================================")


if __name__ == "__main__":
    main()
