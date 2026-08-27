# Anurag University — Department of Computer Science & Engineering
## Course: Generative AI & Prompt Engineering Laboratory
### Student Assessment Submission Suite (Assignments 3, 4, & 5)

---

## 📌 Submission Overview

This repository contains the complete practical coursework submissions for **Assignments 3, 4, and 5**. Each assignment has been designed, implemented, and empirically benchmarked with full statistical tracking, failure catalogues, visual graphs, and compiled formal PDF assessment reports.

---

## 📂 Submissions Directory & Navigation

```
├── README.md                                  # Repository Master Documentation
├── Assignments-Anurag University.docx         # Assessment Reference Guide
│
├── Assignment-3-Prompt-Engineering/           # Assignment 3: Prompt Engineering Library
│   ├── README.md                              # Detailed Benchmark Report & Findings
│   ├── Assignment-03-23EG107E19.pdf           # Compiled Academic PDF Report
│   ├── prompts/                               # 4 Iterative Prompt Versions (v1 to v4)
│   ├── data/                                  # 52-Sample Golden Dataset (golden_set.csv)
│   ├── evaluation/                            # 4-Dimension Evaluation Rubric (rubric.md)
│   ├── results/                               # Benchmark Results & Summary CSVs
│   └── graphs/                                # 4 Visual Analytics Charts
│
├── Assignment-4-AI-Coding-Workflow/           # Assignment 4: AI-Assisted Coding Workflow
│   ├── README.md                              # Detailed 10-Task Productivity Study
│   ├── Assignment-04-23EG107E19.pdf           # Compiled Academic PDF Report
│   ├── time-log.csv                           # Granular Time Logs (Gen, Review, Correct)
│   ├── defect-log.csv                         # 10 Defects across Logic, Edge, Security, Perf, Style
│   ├── tasks/ (task01 to task10)              # 10 Tasks with unassisted.py & assisted.py
│   ├── tests/ (test_task01.py to test_task10.py) # 30 Independent Pytest Suites
│   ├── results/                               # Benchmark Summary CSV
│   └── graphs/                                # 4 Performance & Defect Visualization Charts
│
└── Assignment-5-Document-Extraction/          # Assignment 5: Document Extraction Pipeline
    ├── README.md                              # Document AI Pipeline Architecture & Results
    ├── Assignment-05-23EG107E19.pdf           # Compiled Academic PDF Report
    ├── src/                                   # schema.py, extractor.py, routing.py
    ├── data/                                  # 105 Sample Documents (Invoices, Claims, ID Cards)
    ├── ground-truth/                          # 105-Document Verified Ground Truth (ground_truth.csv)
    ├── results/                               # Field Accuracy, Calibration, Extraction CSVs
    └── graphs/                                # 4 Accuracy, Routing, Calibration & Cost Charts
```

---

## 📊 Summary Assessment Matrix

| Assignment | Core Theme | Methodology | Primary Finding | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Assignment 3** | Prompt Engineering Library | Compared 4 prompt techniques across 52 pre-prompting benchmark cases. | **Structured Template (`v4`) scored 4.80 / 5.00 (+36.4% gain)** with 100% format compliance. | ✅ Complete |
| **Assignment 4** | AI Coding Workflow | Timed 10 tasks across manual vs AI (generation, review, correction). | **+51.8% Net Speedup**; 80% of assisted time was spent on review/bug fixing (0% on subtle debugging). | ✅ Complete |
| **Assignment 5** | Document Extraction Pipeline | Evaluated field-level accuracy and confidence routing across 105 BFSI docs. | **92.3% Cost Reduction ($0.116 vs $1.50/doc)**; safely routed review cases to human queue. | ✅ Complete |

---

## 📄 Academic Deliverables

Each assignment folder contains a self-contained, formal compiled PDF report for evaluation, embedding complete data tables, visual graphs, error breakdowns, and practical conclusions:

- **Assignment 3 Report**: [`Assignment-03-23EG107E19.pdf`](./Assignment-3-Prompt-Engineering/Assignment-03-23EG107E19.pdf)
- **Assignment 4 Report**: [`Assignment-04-23EG107E19.pdf`](./Assignment-4-AI-Coding-Workflow/Assignment-04-23EG107E19.pdf)
- **Assignment 5 Report**: [`Assignment-05-23EG107E19.pdf`](./Assignment-5-Document-Extraction/Assignment-05-23EG107E19.pdf)

