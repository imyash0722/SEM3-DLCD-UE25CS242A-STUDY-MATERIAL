# DLCD Course Complete OCR & Document Text Extraction Repository

This directory (`ocr/`) contains all converted PDFs, OCR'd searchable PDFs, extracted text transcripts, native PDF stream text, and the aggregated unit-by-unit master text files.

---

## 1. Master Unit Files (All Content Bundled)

Each master unit file compiles **every document, slide deck, question bank, MCQ, lab report, handwritten lecture note, and topic module** belonging to that unit into one consolidated, complete document:

| Unit | Plain Text File | Markdown File | Word Count | Size | Description |
|:---:|:---|:---|:---:|:---:|:---|
| **Unit 1** | [`UNIT_1.txt`](file:///mnt/shared/sem3/DLCD/ocr/UNIT_1.txt) | [`UNIT_1_ALL_CONTENT.md`](file:///mnt/shared/sem3/DLCD/ocr/UNIT_1_ALL_CONTENT.md) | **80,694 words** | 430 KB | Combinational & Sequential Logic Design (17 sections) |
| **Unit 2** | [`UNIT_2.txt`](file:///mnt/shared/sem3/DLCD/ocr/UNIT_2.txt) | [`UNIT_2_ALL_CONTENT.md`](file:///mnt/shared/sem3/DLCD/ocr/UNIT_2_ALL_CONTENT.md) | **56,886 words** | 333 KB | FSMs & Digital Building Blocks (23 sections) |
| **Unit 3** | [`UNIT_3.txt`](file:///mnt/shared/sem3/DLCD/ocr/UNIT_3.txt) | [`UNIT_3_ALL_CONTENT.md`](file:///mnt/shared/sem3/DLCD/ocr/UNIT_3_ALL_CONTENT.md) | **75,459 words** | 451 KB | Computer Architecture & Processor Design (24 sections) |
| **Total** | — | — | **213,039 words** | **~1.2 MB** | Complete 3-Unit Course Package |

---

## 2. Directory Structure

```
ocr/
├── README.md                          <- This guide and index
├── ocr_extraction_summary.json        <- Machine-readable metadata for all 29 documents
├── UNIT_1.txt                         <- Master Unit 1 plain text (80k words)
├── UNIT_1_ALL_CONTENT.md              <- Master Unit 1 markdown with anchors
├── UNIT_2.txt                         <- Master Unit 2 plain text (56k words)
├── UNIT_2_ALL_CONTENT.md              <- Master Unit 2 markdown with anchors
├── UNIT_3.txt                         <- Master Unit 3 plain text (75k words)
├── UNIT_3_ALL_CONTENT.md              <- Master Unit 3 markdown with anchors
├── pdfs/                              <- 29 OCR'd PDFs with embedded searchable text layers
├── text/                              <- 29 individual OCR extracted text files
└── source_pdf_text/                   <- 29 native digital text stream extractions
```

---

## 3. Complete Document Inventory (29 Documents)

| # | Original Document | Pages | Words | Searchable OCR PDF | Extracted Text Transcript | Native Stream Text |
|---|-------------------|:---:|:---:|:---|:---|:---|
| 1 | `notes/question1.jpeg` | 1 | 131 | [Notes_question1_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Notes_question1_ocr.pdf) | [Notes_question1.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Notes_question1.txt) | [question1_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/question1_source.txt) |
| 2 | `notes/sequential-1.jpg` | 1 | 20 | [Notes_sequential-1_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Notes_sequential-1_ocr.pdf) | [Notes_sequential-1.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Notes_sequential-1.txt) | [sequential-1_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/sequential-1_source.txt) |
| 3 | `notes/sequential-2.jpg` | 1 | 0 | [Notes_sequential-2_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Notes_sequential-2_ocr.pdf) | [Notes_sequential-2.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Notes_sequential-2.txt) | [sequential-2_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/sequential-2_source.txt) |
| 4 | `resources/U2QB.docx` | 2 | 585 | [Resources_U2QB_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_U2QB_ocr.pdf) | [Resources_U2QB.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_U2QB.txt) | [U2QB_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2QB_source.txt) |
| 5 | `resources/u3/3/Assignments/3.1.1_ASSIGNMENT.docx` | 2 | 591 | [U3_Assignment_3.1.1_ASSIGNMENT_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Assignment_3.1.1_ASSIGNMENT_ocr.pdf) | [U3_Assignment_3.1.1_ASSIGNMENT.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Assignment_3.1.1_ASSIGNMENT.txt) | [3.1.1_ASSIGNMENT_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.1.1_ASSIGNMENT_source.txt) |
| 6 | `lab/week8/PES2UG25CS615_Yashwanth K_DLCDLab8.docx` | 6 | 387 | [Lab_PES2UG25CS615_Yashwanth K_DLCDLab8_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Lab_PES2UG25CS615_Yashwanth%20K_DLCDLab8_ocr.pdf) | [Lab_PES2UG25CS615_Yashwanth K_DLCDLab8.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Lab_PES2UG25CS615_Yashwanth%20K_DLCDLab8.txt) | [PES2UG25CS615_Yashwanth K_DLCDLab8_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/PES2UG25CS615_Yashwanth%20K_DLCDLab8_source.txt) |
| 7 | `resources/U2MCQ2.docx` | 6 | 1,411 | [Resources_U2MCQ2_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_U2MCQ2_ocr.pdf) | [Resources_U2MCQ2.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_U2MCQ2.txt) | [U2MCQ2_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2MCQ2_source.txt) |
| 8 | `resources/U2QB_soln.docx` | 10 | 2,102 | [Resources_U2QB_soln_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_U2QB_soln_ocr.pdf) | [Resources_U2QB_soln.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_U2QB_soln.txt) | [U2QB_soln_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2QB_soln_source.txt) |
| 9 | `resources/U2MCQ1.docx` | 13 | 2,493 | [Resources_U2MCQ1_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_U2MCQ1_ocr.pdf) | [Resources_U2MCQ1.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_U2MCQ1.txt) | [U2MCQ1_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2MCQ1_source.txt) |
| 10 | `notes/U2N2.pdf` | 13 | 489 | [Notes_U2N2_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Notes_U2N2_ocr.pdf) | [Notes_U2N2.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Notes_U2N2.txt) | [U2N2_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2N2_source.txt) |
| 11 | `resources/u3/3/Slides/3.6.1_Introduction.pptx` | 14 | 822 | [U3_Slides_3.6.1_Introduction_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.6.1_Introduction_ocr.pdf) | [U3_Slides_3.6.1_Introduction.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.6.1_Introduction.txt) | [3.6.1_Introduction_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.6.1_Introduction_source.txt) |
| 12 | `resources/u3/QB/3.1.1_QB.pdf` | 14 | 5,177 | [U3_QB_3.1.1_QB_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_QB_3.1.1_QB_ocr.pdf) | [U3_QB_3.1.1_QB.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_QB_3.1.1_QB.txt) | [3.1.1_QB_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.1.1_QB_source.txt) |
| 13 | `notes/U2N1.pdf` | 15 | 439 | [Notes_U2N1_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Notes_U2N1_ocr.pdf) | [Notes_U2N1.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Notes_U2N1.txt) | [U2N1_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2N1_source.txt) |
| 14 | `resources/u3/3/Slides/3.17.1_Classwork_problems.pptx` | 16 | 1,182 | [U3_Slides_3.17.1_Classwork_problems_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.17.1_Classwork_problems_ocr.pdf) | [U3_Slides_3.17.1_Classwork_problems.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.17.1_Classwork_problems.txt) | [3.17.1_Classwork_problems_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.17.1_Classwork_problems_source.txt) |
| 15 | `resources/QB.doc` | 19 | 4,455 | [Resources_QB_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_QB_ocr.pdf) | [Resources_QB.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_QB.txt) | [QB_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/QB_source.txt) |
| 16 | `resources/U2MCQ3.pdf` | 21 | 2,514 | [Resources_U2MCQ3_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_U2MCQ3_ocr.pdf) | [Resources_U2MCQ3.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_U2MCQ3.txt) | [U2MCQ3_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U2MCQ3_source.txt) |
| 17 | `notes/FSM.pdf` | 24 | 6,798 | [Notes_FSM_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Notes_FSM_ocr.pdf) | [Notes_FSM.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Notes_FSM.txt) | [FSM_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/FSM_source.txt) |
| 18 | `resources/u3/QA/3.1.1_QA.pdf` | 24 | 8,643 | [U3_QA_3.1.1_QA_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_QA_3.1.1_QA_ocr.pdf) | [U3_QA_3.1.1_QA.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_QA_3.1.1_QA.txt) | [3.1.1_QA_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.1.1_QA_source.txt) |
| 19 | `resources/u3/3/Slides/3.14.2_COM-ASS-LOAD.pptx` | 26 | 2,531 | [U3_Slides_3.14.2_COM-ASS-LOAD_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.14.2_COM-ASS-LOAD_ocr.pdf) | [U3_Slides_3.14.2_COM-ASS-LOAD.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.14.2_COM-ASS-LOAD.txt) | [3.14.2_COM-ASS-LOAD_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.14.2_COM-ASS-LOAD_source.txt) |
| 20 | `resources/u3/3/Slides/3.14.1_Addressing_Mode.pptx` | 29 | 1,756 | [U3_Slides_3.14.1_Addressing_Mode_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.14.1_Addressing_Mode_ocr.pdf) | [U3_Slides_3.14.1_Addressing_Mode.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.14.1_Addressing_Mode.txt) | [3.14.1_Addressing_Mode_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.14.1_Addressing_Mode_source.txt) |
| 21 | `resources/U1QB_soln.docx` | 30 | 3,297 | [Resources_U1QB_soln_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_U1QB_soln_ocr.pdf) | [Resources_U1QB_soln.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_U1QB_soln.txt) | [U1QB_soln_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/U1QB_soln_source.txt) |
| 22 | `resources/u3/3/Slides/3.9.1_Machine_Language.pptx` | 34 | 2,829 | [U3_Slides_3.9.1_Machine_Language_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.9.1_Machine_Language_ocr.pdf) | [U3_Slides_3.9.1_Machine_Language.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.9.1_Machine_Language.txt) | [3.9.1_Machine_Language_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.9.1_Machine_Language_source.txt) |
| 23 | `resources/u3/3/Slides/3.15.1_Parallelism.pptx` | 37 | 2,572 | [U3_Slides_3.15.1_Parallelism_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.15.1_Parallelism_ocr.pdf) | [U3_Slides_3.15.1_Parallelism.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.15.1_Parallelism.txt) | [3.15.1_Parallelism_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.15.1_Parallelism_source.txt) |
| 24 | `resources/u3/3/Slides/3.3.1_Memory_Arrays.pptx` | 41 | 4,384 | [U3_Slides_3.3.1_Memory_Arrays_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.3.1_Memory_Arrays_ocr.pdf) | [U3_Slides_3.3.1_Memory_Arrays.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.3.1_Memory_Arrays.txt) | [3.3.1_Memory_Arrays_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.3.1_Memory_Arrays_source.txt) |
| 25 | `resources/u3/3/Slides/3.1.1_Sequential_Building_Block.pptx` | 48 | 4,306 | [U3_Slides_3.1.1_Sequential_Building_Block_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.1.1_Sequential_Building_Block_ocr.pdf) | [U3_Slides_3.1.1_Sequential_Building_Block.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.1.1_Sequential_Building_Block.txt) | [3.1.1_Sequential_Building_Block_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.1.1_Sequential_Building_Block_source.txt) |
| 26 | `resources/u3/3/Slides/3.7.1_Assembly_Language.pptx` | 56 | 5,078 | [U3_Slides_3.7.1_Assembly_Language_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.7.1_Assembly_Language_ocr.pdf) | [U3_Slides_3.7.1_Assembly_Language.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.7.1_Assembly_Language.txt) | [3.7.1_Assembly_Language_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.7.1_Assembly_Language_source.txt) |
| 27 | `resources/u3/3/Slides/3.11.1_Programming.pptx` | 85 | 7,307 | [U3_Slides_3.11.1_Programming_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/U3_Slides_3.11.1_Programming_ocr.pdf) | [U3_Slides_3.11.1_Programming.txt](file:///mnt/shared/sem3/DLCD/ocr/text/U3_Slides_3.11.1_Programming.txt) | [3.11.1_Programming_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/3.11.1_Programming_source.txt) |
| 28 | `resources/DLCD - Unit 2 Combined Slides.pdf` | 139 | 7,849 | [Resources_DLCD - Unit 2 Combined Slides_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_DLCD%20-%20Unit%202%20Combined%20Slides_ocr.pdf) | [Resources_DLCD - Unit 2 Combined Slides.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_DLCD%20-%20Unit%202%20Combined%20Slides.txt) | [DLCD - Unit 2 Combined Slides_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/DLCD%20-%20Unit%202%20Combined%20Slides_source.txt) |
| 29 | `resources/DLCD - Unit 1 Combined Slides.pdf` | 255 | 20,117 | [Resources_DLCD - Unit 1 Combined Slides_ocr.pdf](file:///mnt/shared/sem3/DLCD/ocr/pdfs/Resources_DLCD%20-%20Unit%201%20Combined%20Slides_ocr.pdf) | [Resources_DLCD - Unit 1 Combined Slides.txt](file:///mnt/shared/sem3/DLCD/ocr/text/Resources_DLCD%20-%20Unit%201%20Combined%20Slides.txt) | [DLCD - Unit 1 Combined Slides_source.txt](file:///mnt/shared/sem3/DLCD/ocr/source_pdf_text/DLCD%20-%20Unit%201%20Combined%20Slides_source.txt) |
