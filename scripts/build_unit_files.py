#!/usr/bin/env python3
"""
Compile ALL course content into 3 big files, one per unit (Units 1, 2, and 3).
DLCD Course Document Bundler.
"""

from pathlib import Path
import time

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_OCR_TXT = ROOT_DIR / "output_ocr/text"

# Unit 1 Specifications
UNIT_1_CONFIG = {
    "title": "UNIT 1: COMBINATIONAL AND SEQUENTIAL LOGIC DESIGN",
    "unit_number": 1,
    "filename": "UNIT_1_ALL_CONTENT.md",
    "ocr_documents": [
        {
            "name": "DLCD - Unit 1 Combined Lecture Slides (255 Pages)",
            "source": "resources/DLCD - Unit 1 Combined Slides.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_DLCD - Unit 1 Combined Slides.txt",
        },
        {
            "name": "Unit 1 Descriptive Question Bank with Model Solutions (30 Pages)",
            "source": "resources/U1QB_soln.docx",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_U1QB_soln.txt",
        },
        {
            "name": "Unit 1 Complete 120 Question Bank (19 Pages)",
            "source": "resources/QB.doc",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_QB.txt",
        },
        {
            "name": "Lecture Notes: Problem Solving 1",
            "source": "notes/question1.jpeg",
            "ocr_text": OUTPUT_OCR_TXT / "Notes_question1.txt",
        },
        {
            "name": "Lecture Notes: Sequential Logic & Latches (Part 1)",
            "source": "notes/sequential-1.jpg",
            "ocr_text": OUTPUT_OCR_TXT / "Notes_sequential-1.txt",
        },
        {
            "name": "Lecture Notes: Sequential Logic & Latches (Part 2)",
            "source": "notes/sequential-2.jpg",
            "ocr_text": OUTPUT_OCR_TXT / "Notes_sequential-2.txt",
        },
    ],
    "resource_markdowns": [
        ROOT_DIR / "resources/DLCD_Unit_1_Clean_Slides.md",
        ROOT_DIR / "resources/DLCD_Unit_1_Question_Bank.md",
        ROOT_DIR / "resources/DLCD_Unit_1_MCQs.md",
    ],
    "docs_topics": [
        ROOT_DIR / "docs/01_digital-circuits-introduction.md",
        ROOT_DIR / "docs/02_boolean-equations.md",
        ROOT_DIR / "docs/03_logic-minimization-kmaps-3var.md",
        ROOT_DIR / "docs/04_kmaps-4var-seven-segment.md",
        ROOT_DIR / "docs/05_combinational-building-blocks.md",
        ROOT_DIR / "docs/06_sequential-basics-latches.md",
        ROOT_DIR / "docs/07_flipflops-timing-metastability.md",
    ],
}

# Unit 2 Specifications
UNIT_2_CONFIG = {
    "title": "UNIT 2: FINITE STATE MACHINES & DIGITAL BUILDING BLOCKS",
    "unit_number": 2,
    "filename": "UNIT_2_ALL_CONTENT.md",
    "ocr_documents": [
        {
            "name": "DLCD - Unit 2 Combined Lecture Slides (139 Pages)",
            "source": "resources/DLCD - Unit 2 Combined Slides.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_DLCD - Unit 2 Combined Slides.txt",
        },
        {
            "name": "Unit 2 Question Bank Solved (10 Pages)",
            "source": "resources/U2QB_soln.docx",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_U2QB_soln.txt",
        },
        {
            "name": "Unit 2 Descriptive Question Bank (2 Pages)",
            "source": "resources/U2QB.docx",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_U2QB.txt",
        },
        {
            "name": "Unit 2 Multiple Choice Questions Set 1 (13 Pages)",
            "source": "resources/U2MCQ1.docx",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_U2MCQ1.txt",
        },
        {
            "name": "Unit 2 Multiple Choice Questions Set 2 (6 Pages)",
            "source": "resources/U2MCQ2.docx",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_U2MCQ2.txt",
        },
        {
            "name": "Unit 2 Multiple Choice Questions Set 3 - Number Systems (21 Pages)",
            "source": "resources/U2MCQ3.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "Resources_U2MCQ3.txt",
        },
        {
            "name": "Lecture Notes: Finite State Machines Comprehensive (24 Pages)",
            "source": "notes/FSM.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "Notes_FSM.txt",
        },
        {
            "name": "Lecture Notes: Unit 2 Topics Part 1 (15 Pages)",
            "source": "notes/U2N1.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "Notes_U2N1.txt",
        },
        {
            "name": "Lecture Notes: Unit 2 Topics Part 2 (13 Pages)",
            "source": "notes/U2N2.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "Notes_U2N2.txt",
        },
        {
            "name": "Lab Week 8: Prefix Adder and 4-bit Comparator Submission (6 Pages)",
            "source": "lab/week8/PES2UG25CS615_Yashwanth K_DLCDLab8.docx",
            "ocr_text": OUTPUT_OCR_TXT / "Lab_PES2UG25CS615_Yashwanth K_DLCDLab8.txt",
        },
    ],
    "resource_markdowns": [
        ROOT_DIR / "resources/DLCD_Unit_2_Clean_Slides.md",
        ROOT_DIR / "resources/DLCD_Unit_2_Question_Bank.md",
        ROOT_DIR / "resources/DLCD_Unit_2_MCQs.md",
    ],
    "docs_topics": [
        ROOT_DIR / "docs/08_fsm-moore-mealy-design.md",
        ROOT_DIR / "docs/09_state-encoding-factoring.md",
        ROOT_DIR / "docs/10_arithmetic-adders.md",
        ROOT_DIR / "docs/11_alu-comparator-shifter-multiplier.md",
        ROOT_DIR / "docs/12_number-systems-fixedpoint.md",
        ROOT_DIR / "docs/13_floating-point-ieee754.md",
    ],
}

# Unit 3 Specifications
UNIT_3_CONFIG = {
    "title": "UNIT 3: COMPUTER ARCHITECTURE & PROCESSOR DESIGN",
    "unit_number": 3,
    "filename": "UNIT_3_ALL_CONTENT.md",
    "ocr_documents": [
        {
            "name": "Slide Deck 3.1.1: Sequential Building Blocks (48 Pages)",
            "source": "resources/u3/3/Slides/3.1.1_Sequential_Building_Block.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.1.1_Sequential_Building_Block.txt",
        },
        {
            "name": "Slide Deck 3.3.1: Memory Arrays - RAM, ROM, PLA (41 Pages)",
            "source": "resources/u3/3/Slides/3.3.1_Memory_Arrays.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.3.1_Memory_Arrays.txt",
        },
        {
            "name": "Slide Deck 3.6.1: Computer Architecture Introduction (14 Pages)",
            "source": "resources/u3/3/Slides/3.6.1_Introduction.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.6.1_Introduction.txt",
        },
        {
            "name": "Slide Deck 3.7.1: Assembly Language & MIPS Architecture (56 Pages)",
            "source": "resources/u3/3/Slides/3.7.1_Assembly_Language.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.7.1_Assembly_Language.txt",
        },
        {
            "name": "Slide Deck 3.9.1: Machine Language & Instruction Encoding (34 Pages)",
            "source": "resources/u3/3/Slides/3.9.1_Machine_Language.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.9.1_Machine_Language.txt",
        },
        {
            "name": "Slide Deck 3.11.1: Programming & Procedures in Assembly (85 Pages)",
            "source": "resources/u3/3/Slides/3.11.1_Programming.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.11.1_Programming.txt",
        },
        {
            "name": "Slide Deck 3.14.1: Addressing Modes (29 Pages)",
            "source": "resources/u3/3/Slides/3.14.1_Addressing_Mode.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.14.1_Addressing_Mode.txt",
        },
        {
            "name": "Slide Deck 3.14.2: Compiling, Assembling, and Loading (26 Pages)",
            "source": "resources/u3/3/Slides/3.14.2_COM-ASS-LOAD.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.14.2_COM-ASS-LOAD.txt",
        },
        {
            "name": "Slide Deck 3.15.1: Parallelism - ILP, Multi-threading & Multi-core (37 Pages)",
            "source": "resources/u3/3/Slides/3.15.1_Parallelism.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.15.1_Parallelism.txt",
        },
        {
            "name": "Slide Deck 3.17.1: Classwork Practice Problems (16 Pages)",
            "source": "resources/u3/3/Slides/3.17.1_Classwork_problems.pptx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Slides_3.17.1_Classwork_problems.txt",
        },
        {
            "name": "Assignment 3.1.1: Sequential Building Blocks Assignment (2 Pages)",
            "source": "resources/u3/3/Assignments/3.1.1_ASSIGNMENT.docx",
            "ocr_text": OUTPUT_OCR_TXT / "U3_Assignment_3.1.1_ASSIGNMENT.txt",
        },
        {
            "name": "Question-Answer Bank: 5, 8, 10 Mark Solved Questions (24 Pages)",
            "source": "resources/u3/QA/3.1.1_QA.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "U3_QA_3.1.1_QA.txt",
        },
        {
            "name": "Comprehensive Descriptive Question Bank (14 Pages)",
            "source": "resources/u3/QB/3.1.1_QB.pdf",
            "ocr_text": OUTPUT_OCR_TXT / "U3_QB_3.1.1_QB.txt",
        },
    ],
    "resource_markdowns": [],
    "docs_topics": [
        ROOT_DIR / "docs/18_sequential-building-blocks.md",
        ROOT_DIR / "docs/19_computer-architecture-intro.md",
        ROOT_DIR / "docs/20_assembly-language.md",
        ROOT_DIR / "docs/21_machine-language.md",
        ROOT_DIR / "docs/22_addressing-modes.md",
        ROOT_DIR / "docs/23_compiling-assembling-loading.md",
        ROOT_DIR / "docs/24_parallelism.md",
        ROOT_DIR / "docs/25_classwork-problems.md",
        ROOT_DIR / "docs/26_unit3-mcq-practice.md",
    ],
}


def build_big_file(config: dict):
    out_file = ROOT_DIR / config["filename"]
    print(f"\n=======================================================")
    print(f"Generating {config['filename']} for {config['title']} ...")
    print(f"=======================================================")

    lines = []
    
    # Master Header
    lines.append(f"# {config['title']}")
    lines.append(f"**Generated**: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Course**: Digital Logic and Computer Design (DLCD) — UE25CS242A / UE25CS251A")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## TABLE OF CONTENTS")
    lines.append("")
    lines.append("### PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS")
    for idx, doc in enumerate(config["ocr_documents"], 1):
        lines.append(f"{idx}. [{doc['name']}](#doc-{idx}) — *Source: `{doc['source']}`*")
    lines.append("")
    
    if config["resource_markdowns"]:
        lines.append("### PART 2: DLCD SYNTHESIZED STUDY PACKAGE (Clean Slides, Question Banks, MCQs)")
        for idx, res in enumerate(config["resource_markdowns"], 1):
            lines.append(f"{idx}. [{res.name}](#res-{idx})")
        lines.append("")

    if config["docs_topics"]:
        lines.append("### PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS")
        for idx, doc_t in enumerate(config["docs_topics"], 1):
            lines.append(f"{idx}. [{doc_t.name}](#topic-{idx})")
        lines.append("")

    lines.append("---")
    lines.append("")

    # PART 1: OCR Documents
    lines.append("# PART 1: OCR EXTRACTED TEXT FROM ORIGINAL SLIDES & DOCUMENTS")
    lines.append("")
    for idx, doc_info in enumerate(config["ocr_documents"], 1):
        name = doc_info["name"]
        src = doc_info["source"]
        ocr_path = doc_info["ocr_text"]
        
        print(f"  [+] Adding OCR Doc {idx}/{len(config['ocr_documents'])}: {name} ...")
        lines.append(f'<a id="doc-{idx}"></a>')
        lines.append(f"## Document {idx}: {name}")
        lines.append(f"**Source Document**: `{src}`")
        lines.append(f"**OCR Extraction File**: `{ocr_path.name}`")
        lines.append("")
        lines.append("```")
        if ocr_path.exists():
            text_content = ocr_path.read_text(encoding="utf-8")
            lines.append(text_content)
        else:
            lines.append(f"[ERROR: OCR file not found: {ocr_path}]")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    # PART 2: Synthesized Study Package (if any)
    if config["resource_markdowns"]:
        lines.append("# PART 2: DLCD SYNTHESIZED STUDY PACKAGE")
        lines.append("")
        for idx, res_path in enumerate(config["resource_markdowns"], 1):
            print(f"  [+] Adding Synthesized Study Doc {idx}/{len(config['resource_markdowns'])}: {res_path.name} ...")
            lines.append(f'<a id="res-{idx}"></a>')
            lines.append(f"## Synthesized Resource {idx}: {res_path.name}")
            lines.append(f"**Source File**: `{res_path.relative_to(ROOT_DIR)}`")
            lines.append("")
            if res_path.exists():
                lines.append(res_path.read_text(encoding="utf-8"))
            else:
                lines.append(f"[ERROR: File not found: {res_path}]")
            lines.append("")
            lines.append("---")
            lines.append("")

    # PART 3: Detailed Topic Curriculum Notes (if any)
    if config["docs_topics"]:
        lines.append("# PART 3: DETAILED TOPIC CURRICULUM NOTES & DERIVATIONS")
        lines.append("")
        for idx, doc_t in enumerate(config["docs_topics"], 1):
            print(f"  [+] Adding Topic Note {idx}/{len(config['docs_topics'])}: {doc_t.name} ...")
            lines.append(f'<a id="topic-{idx}"></a>')
            lines.append(f"## Topic Module {idx}: {doc_t.name}")
            lines.append(f"**Source File**: `{doc_t.relative_to(ROOT_DIR)}`")
            lines.append("")
            if doc_t.exists():
                lines.append(doc_t.read_text(encoding="utf-8"))
            else:
                lines.append(f"[ERROR: File not found: {doc_t}]")
            lines.append("")
            lines.append("---")
            lines.append("")

    content_str = "\n".join(lines)
    out_file.write_text(content_str, encoding="utf-8")
    
    total_words = len(content_str.split())
    total_chars = len(content_str)
    print(f"  -> Generated {out_file.name}: {total_words:,} words, {total_chars:,} characters, {len(lines):,} lines.")
    return {
        "unit": config["unit_number"],
        "filename": config["filename"],
        "words": total_words,
        "chars": total_chars,
        "lines": len(lines),
    }


def main():
    results = []
    results.append(build_big_file(UNIT_1_CONFIG))
    results.append(build_big_file(UNIT_2_CONFIG))
    results.append(build_big_file(UNIT_3_CONFIG))

    print("\n=======================================================")
    print("ALL 3 BIG UNIT FILES SUCCESSFULLY GENERATED!")
    print("=======================================================")
    for r in results:
        print(f"  Unit {r['unit']}: {r['filename']} -> {r['words']:,} words ({r['lines']:,} lines, {r['chars']:,} bytes)")
    print(f"Total Words Across Units 1-3: {sum(r['words'] for r in results):,} words!")


if __name__ == "__main__":
    main()
