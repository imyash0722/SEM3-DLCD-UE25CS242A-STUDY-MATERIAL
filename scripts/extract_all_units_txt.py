#!/usr/bin/env python3
"""
Extract all source PDF documents as txt and compile full unit content into one big txt file per unit.
Generates UNIT_1.txt, UNIT_2.txt, and UNIT_3.txt.
"""

from pathlib import Path
import time
import pymupdf

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_OCR_TXT = ROOT_DIR / "output_ocr/text"
SOURCE_PDF_TXT_DIR = ROOT_DIR / "source_pdf_text"
SOURCE_PDF_TXT_DIR.mkdir(parents=True, exist_ok=True)


def extract_source_pdf(pdf_path: Path) -> Path:
    """Extract native digital text directly from a source PDF document."""
    out_txt_path = SOURCE_PDF_TXT_DIR / f"{pdf_path.stem}_source.txt"
    # Also save alongside the PDF
    local_source_txt = pdf_path.parent / f"{pdf_path.stem}_source.txt"
    
    doc = pymupdf.open(pdf_path)
    page_count = len(doc)
    pages = []
    total_words = 0
    total_chars = 0
    
    for page_idx in range(page_count):
        page = doc[page_idx]
        text = page.get_text("text").strip()
        words = len(text.split())
        total_words += words
        total_chars += len(text)
        if text:
            pages.append(f"--- [Page {page_idx + 1} of {page_count}] ---\n{text}\n")
            
    doc.close()
    
    header = (
        f"================================================================================\n"
        f"SOURCE PDF DOCUMENT : {pdf_path.name}\n"
        f"SOURCE PATH         : {pdf_path.relative_to(ROOT_DIR)}\n"
        f"PAGES               : {page_count}\n"
        f"WORDS EXTRACTED     : {total_words}\n"
        f"CHARACTERS          : {total_chars}\n"
        f"EXTRACTION MODE     : Direct Native PDF Digital Stream (PyMuPDF)\n"
        f"================================================================================\n\n"
    )
    content = header + "\n".join(pages)
    out_txt_path.write_text(content, encoding="utf-8")
    local_source_txt.write_text(content, encoding="utf-8")
    print(f"[NATIVE PDF EXTRACT] {pdf_path.name}: {total_words} words -> {out_txt_path.name}")
    return out_txt_path


# 1. Source PDFs to extract native text from
SOURCE_PDFS = [
    ROOT_DIR / "resources/DLCD - Unit 1 Combined Slides.pdf",
    ROOT_DIR / "resources/DLCD - Unit 2 Combined Slides.pdf",
    ROOT_DIR / "resources/U2MCQ3.pdf",
    ROOT_DIR / "resources/u3/QA/3.1.1_QA.pdf",
    ROOT_DIR / "resources/u3/QB/3.1.1_QB.pdf",
    ROOT_DIR / "notes/FSM.pdf",
    ROOT_DIR / "notes/U2N1.pdf",
    ROOT_DIR / "notes/U2N2.pdf",
    # Also converted slide/doc PDFs:
    ROOT_DIR / "resources/QB.pdf",
    ROOT_DIR / "resources/U1QB_soln.pdf",
    ROOT_DIR / "resources/U2QB.pdf",
    ROOT_DIR / "resources/U2QB_soln.pdf",
    ROOT_DIR / "resources/U2MCQ1.pdf",
    ROOT_DIR / "resources/U2MCQ2.pdf",
    ROOT_DIR / "resources/u3/3/Assignments/3.1.1_ASSIGNMENT.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.1.1_Sequential_Building_Block.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.3.1_Memory_Arrays.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.6.1_Introduction.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.7.1_Assembly_Language.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.9.1_Machine_Language.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.11.1_Programming.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.14.1_Addressing_Mode.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.14.2_COM-ASS-LOAD.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.15.1_Parallelism.pdf",
    ROOT_DIR / "resources/u3/3/Slides/3.17.1_Classwork_problems.pdf",
    ROOT_DIR / "lab/week8/PES2UG25CS615_Yashwanth K_DLCDLab8.pdf",
    ROOT_DIR / "notes/question1.pdf",
    ROOT_DIR / "notes/sequential-1.pdf",
    ROOT_DIR / "notes/sequential-2.pdf",
]


# Unit Configurations for full content bundling into UNIT_X.txt
UNIT_BUNDLES = [
    {
        "unit": 1,
        "filename": "UNIT_1.txt",
        "title": "UNIT 1: COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN — COMPLETE UNIT REPOSITORY",
        "files": [
            # 1. Source PDF & OCR Extracted Transcripts
            ("SOURCE PDF EXTRACT: DLCD - Unit 1 Combined Lecture Slides (255 Pages)", ROOT_DIR / "source_pdf_text/DLCD - Unit 1 Combined Slides_source.txt"),
            ("OCR PDF EXTRACT (with Diagram Labels): Unit 1 Combined Slides", OUTPUT_OCR_TXT / "Resources_DLCD - Unit 1 Combined Slides.txt"),
            ("SOURCE / OCR EXTRACT: Unit 1 Descriptive Question Bank Solved", OUTPUT_OCR_TXT / "Resources_U1QB_soln.txt"),
            ("SOURCE / OCR EXTRACT: Unit 1 Complete 120 Question Bank", OUTPUT_OCR_TXT / "Resources_QB.txt"),
            ("OCR EXTRACT: Problem Solving Note 1", OUTPUT_OCR_TXT / "Notes_question1.txt"),
            ("OCR EXTRACT: Sequential Logic & Latches Note 1", OUTPUT_OCR_TXT / "Notes_sequential-1.txt"),
            ("OCR EXTRACT: Sequential Logic & Latches Note 2", OUTPUT_OCR_TXT / "Notes_sequential-2.txt"),
            # 2. Synthesized packages
            ("SYNTHESIZED STUDY PACKAGE: Unit 1 Clean Slides", ROOT_DIR / "resources/DLCD_Unit_1_Clean_Slides.md"),
            ("SYNTHESIZED STUDY PACKAGE: Unit 1 Solved Question Bank", ROOT_DIR / "resources/DLCD_Unit_1_Question_Bank.md"),
            ("SYNTHESIZED STUDY PACKAGE: Unit 1 Multiple Choice Questions", ROOT_DIR / "resources/DLCD_Unit_1_MCQs.md"),
            # 3. Topic Guides
            ("TOPIC 01: Digital Circuits Introduction", ROOT_DIR / "docs/01_digital-circuits-introduction.md"),
            ("TOPIC 02: Boolean Equations", ROOT_DIR / "docs/02_boolean-equations.md"),
            ("TOPIC 03: Logic Minimization & K-Maps (3-Variable)", ROOT_DIR / "docs/03_logic-minimization-kmaps-3var.md"),
            ("TOPIC 04: K-Maps (4-Variable) & Seven-Segment Display", ROOT_DIR / "docs/04_kmaps-4var-seven-segment.md"),
            ("TOPIC 05: Combinational Building Blocks", ROOT_DIR / "docs/05_combinational-building-blocks.md"),
            ("TOPIC 06: Sequential Basics — Latches", ROOT_DIR / "docs/06_sequential-basics-latches.md"),
            ("TOPIC 07: Flip-Flops, Timing & Metastability", ROOT_DIR / "docs/07_flipflops-timing-metastability.md"),
        ]
    },
    {
        "unit": 2,
        "filename": "UNIT_2.txt",
        "title": "UNIT 2: FINITE STATE MACHINES & DIGITAL BUILDING BLOCKS — COMPLETE UNIT REPOSITORY",
        "files": [
            # 1. Source PDF & OCR Extracted Transcripts
            ("SOURCE PDF EXTRACT: DLCD - Unit 2 Combined Lecture Slides (139 Pages)", ROOT_DIR / "source_pdf_text/DLCD - Unit 2 Combined Slides_source.txt"),
            ("OCR PDF EXTRACT (with Diagram Labels): Unit 2 Combined Slides", OUTPUT_OCR_TXT / "Resources_DLCD - Unit 2 Combined Slides.txt"),
            ("SOURCE / OCR EXTRACT: Unit 2 Question Bank Solved", OUTPUT_OCR_TXT / "Resources_U2QB_soln.txt"),
            ("SOURCE / OCR EXTRACT: Unit 2 Descriptive Question Bank", OUTPUT_OCR_TXT / "Resources_U2QB.txt"),
            ("SOURCE / OCR EXTRACT: Unit 2 MCQs Set 1", OUTPUT_OCR_TXT / "Resources_U2MCQ1.txt"),
            ("SOURCE / OCR EXTRACT: Unit 2 MCQs Set 2", OUTPUT_OCR_TXT / "Resources_U2MCQ2.txt"),
            ("SOURCE PDF EXTRACT: Unit 2 MCQs Set 3 (Number Systems)", ROOT_DIR / "source_pdf_text/U2MCQ3_source.txt"),
            ("OCR PDF EXTRACT: Unit 2 MCQs Set 3 (Number Systems)", OUTPUT_OCR_TXT / "Resources_U2MCQ3.txt"),
            ("OCR EXTRACT: Finite State Machines Comprehensive Notes (24 Pages)", OUTPUT_OCR_TXT / "Notes_FSM.txt"),
            ("OCR EXTRACT: Unit 2 Lecture Notes Part 1 (15 Pages)", OUTPUT_OCR_TXT / "Notes_U2N1.txt"),
            ("OCR EXTRACT: Unit 2 Lecture Notes Part 2 (13 Pages)", OUTPUT_OCR_TXT / "Notes_U2N2.txt"),
            ("SOURCE / OCR EXTRACT: Lab Week 8 - Prefix Adder & 4-bit Comparator", OUTPUT_OCR_TXT / "Lab_PES2UG25CS615_Yashwanth K_DLCDLab8.txt"),
            ("VERILOG SOURCE CODE: 4-bit Comparator (Lab Week 8)", ROOT_DIR / "lab/week8/comparator.v"),
            ("VERILOG SOURCE CODE: Prefix Adder (Lab Week 8)", ROOT_DIR / "lab/week8/prefix_adder.v"),
            # 2. Synthesized packages
            ("SYNTHESIZED STUDY PACKAGE: Unit 2 Clean Slides", ROOT_DIR / "resources/DLCD_Unit_2_Clean_Slides.md"),
            ("SYNTHESIZED STUDY PACKAGE: Unit 2 Solved Question Bank", ROOT_DIR / "resources/DLCD_Unit_2_Question_Bank.md"),
            ("SYNTHESIZED STUDY PACKAGE: Unit 2 Multiple Choice Questions", ROOT_DIR / "resources/DLCD_Unit_2_MCQs.md"),
            # 3. Topic Guides
            ("TOPIC 08: Finite State Machines — Moore & Mealy Design", ROOT_DIR / "docs/08_fsm-moore-mealy-design.md"),
            ("TOPIC 09: State Encoding & Factoring", ROOT_DIR / "docs/09_state-encoding-factoring.md"),
            ("TOPIC 10: Arithmetic Circuits — Adders", ROOT_DIR / "docs/10_arithmetic-adders.md"),
            ("TOPIC 11: ALU, Comparators, Shifters & Multipliers", ROOT_DIR / "docs/11_alu-comparator-shifter-multiplier.md"),
            ("TOPIC 12: Number Systems — Fixed-Point", ROOT_DIR / "docs/12_number-systems-fixedpoint.md"),
            ("TOPIC 13: Floating-Point Arithmetic — IEEE 754", ROOT_DIR / "docs/13_floating-point-ieee754.md"),
        ]
    },
    {
        "unit": 3,
        "filename": "UNIT_3.txt",
        "title": "UNIT 3: COMPUTER ARCHITECTURE & PROCESSOR DESIGN — COMPLETE UNIT REPOSITORY",
        "files": [
            # 1. Slide Decks & Assignments
            ("SOURCE / OCR EXTRACT: Slide Deck 3.1.1 - Sequential Building Blocks", OUTPUT_OCR_TXT / "U3_Slides_3.1.1_Sequential_Building_Block.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.3.1 - Memory Arrays (RAM, ROM, PLA)", OUTPUT_OCR_TXT / "U3_Slides_3.3.1_Memory_Arrays.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.6.1 - Computer Architecture Introduction", OUTPUT_OCR_TXT / "U3_Slides_3.6.1_Introduction.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.7.1 - Assembly Language & MIPS", OUTPUT_OCR_TXT / "U3_Slides_3.7.1_Assembly_Language.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.9.1 - Machine Language & Encoding", OUTPUT_OCR_TXT / "U3_Slides_3.9.1_Machine_Language.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.11.1 - Programming & Procedures in Assembly", OUTPUT_OCR_TXT / "U3_Slides_3.11.1_Programming.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.14.1 - Addressing Modes", OUTPUT_OCR_TXT / "U3_Slides_3.14.1_Addressing_Mode.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.14.2 - Compiling, Assembling, and Loading", OUTPUT_OCR_TXT / "U3_Slides_3.14.2_COM-ASS-LOAD.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.15.1 - Parallelism (ILP, Multithreading, Multicore)", OUTPUT_OCR_TXT / "U3_Slides_3.15.1_Parallelism.txt"),
            ("SOURCE / OCR EXTRACT: Slide Deck 3.17.1 - Classwork Practice Problems", OUTPUT_OCR_TXT / "U3_Slides_3.17.1_Classwork_problems.txt"),
            ("SOURCE / OCR EXTRACT: Assignment 3.1.1 - Sequential Building Blocks", OUTPUT_OCR_TXT / "U3_Assignment_3.1.1_ASSIGNMENT.txt"),
            # 2. Source Question Banks
            ("SOURCE PDF EXTRACT: 3.1.1 QA Solved Question Bank (5, 8, 10 Mark)", ROOT_DIR / "source_pdf_text/3.1.1_QA_source.txt"),
            ("OCR PDF EXTRACT: 3.1.1 QA Solved Question Bank", OUTPUT_OCR_TXT / "U3_QA_3.1.1_QA.txt"),
            ("SOURCE PDF EXTRACT: 3.1.1 QB Descriptive Question Bank", ROOT_DIR / "source_pdf_text/3.1.1_QB_source.txt"),
            ("OCR PDF EXTRACT: 3.1.1 QB Descriptive Question Bank", OUTPUT_OCR_TXT / "U3_QB_3.1.1_QB.txt"),
            # 3. Topic Guides
            ("TOPIC 18: Sequential Building Blocks", ROOT_DIR / "docs/18_sequential-building-blocks.md"),
            ("TOPIC 19: Computer Architecture Introduction", ROOT_DIR / "docs/19_computer-architecture-intro.md"),
            ("TOPIC 20: Assembly Language & MIPS Architecture", ROOT_DIR / "docs/20_assembly-language.md"),
            ("TOPIC 21: Machine Language & Instruction Encoding", ROOT_DIR / "docs/21_machine-language.md"),
            ("TOPIC 22: Addressing Modes", ROOT_DIR / "docs/22_addressing-modes.md"),
            ("TOPIC 23: Compiling, Assembling, and Loading", ROOT_DIR / "docs/23_compiling-assembling-loading.md"),
            ("TOPIC 24: Parallelism — Architecture & Performance", ROOT_DIR / "docs/24_parallelism.md"),
            ("TOPIC 25: Classwork Problems & Step-by-Step Solutions", ROOT_DIR / "docs/25_classwork-problems.md"),
            ("TOPIC 26: Unit 3 Comprehensive MCQ Practice", ROOT_DIR / "docs/26_unit3-mcq-practice.md"),
        ]
    }
]


def main():
    print("=== STEP 1: EXTRACTING NATIVE DIGITAL TEXT DIRECTLY FROM SOURCE PDFS ===")
    for pdf_path in SOURCE_PDFS:
        if pdf_path.exists():
            extract_source_pdf(pdf_path)
        else:
            print(f"[SKIP] PDF not found: {pdf_path}")
            
    print("\n=== STEP 2: GENERATING ONE COMPLETE TXT FILE PER UNIT ===")
    results = []
    
    for bundle in UNIT_BUNDLES:
        unit_num = bundle["unit"]
        out_filename = bundle["filename"]
        out_path = ROOT_DIR / out_filename
        title = bundle["title"]
        file_list = bundle["files"]
        
        print(f"\nBuilding {out_filename} ({title}) ...")
        
        sections = []
        
        # Big Header
        border = "#" * 80
        sections.append(border)
        sections.append(f"# {title}")
        sections.append(f"# Generated : {time.strftime('%Y-%m-%d %H:%M:%S')}")
        sections.append(f"# Total Sections Included: {len(file_list)}")
        sections.append(border)
        sections.append("\nTABLE OF CONTENTS:")
        for idx, (sec_name, sec_path) in enumerate(file_list, 1):
            sections.append(f"  {idx:2d}. {sec_name}")
        sections.append("\n" + border + "\n\n")
        
        # Append every file content
        for idx, (sec_name, sec_path) in enumerate(file_list, 1):
            divider = "=" * 80
            sections.append(divider)
            sections.append(f"SECTION [{idx:2d} of {len(file_list):2d}]: {sec_name}")
            sections.append(f"FILE PATH: {sec_path.relative_to(ROOT_DIR) if ROOT_DIR in sec_path.parents else sec_path.name}")
            sections.append(divider + "\n")
            
            if sec_path.exists():
                text = sec_path.read_text(encoding="utf-8")
                sections.append(text)
            else:
                sections.append(f"[WARNING: File not found: {sec_path}]\n")
                
            sections.append("\n\n")
            
        full_text = "\n".join(sections)
        out_path.write_text(full_text, encoding="utf-8")
        
        word_count = len(full_text.split())
        line_count = len(full_text.splitlines())
        byte_size = len(full_text.encode("utf-8"))
        
        print(f"  -> Generated {out_filename}: {word_count:,} words, {line_count:,} lines, {byte_size/1024:.1f} KB")
        results.append({
            "unit": unit_num,
            "file": out_filename,
            "words": word_count,
            "lines": line_count,
            "size_kb": byte_size / 1024,
            "sections": len(file_list),
        })
        
    print("\n=======================================================")
    print("ALL BIG TXT FILES READY!")
    print("=======================================================")
    for r in results:
        print(f"  Unit {r['unit']}: {r['file']} -> {r['words']:,} words ({r['lines']:,} lines, {r['sections']} sections, {r['size_kb']:.1f} KB)")
    print(f"TOTAL WORDS ACROSS ALL 3 BIG TXT FILES: {sum(r['words'] for r in results):,} words!")


if __name__ == "__main__":
    main()
