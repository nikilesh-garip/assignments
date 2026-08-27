# Assignment 4: AI-Assisted Coding Workflow with Verification Discipline
## Course: Generative AI & Prompt Engineering Laboratory
### Student Practical Submission

---

## 📌 Executive Summary
Productivity claims regarding AI-assisted software development often quote prompt-to-code generation speed, ignoring the considerable time spent reviewing, debugging, and correcting generated code. 

In this assignment, I conducted an **empirical productivity and defect study across 10 distinct coding tasks** spanning **Boilerplate, Algorithms, Refactoring, Test Writing, Debugging, and Integration**. Each task was solved twice:
1. **Unassisted (Manual Baseline)**: Written and debugged entirely from scratch.
2. **AI-Assisted**: Using AI generation, recording **Generation Time**, **Review Time**, and **Correction Time** separately.

Both implementations were evaluated against an independent `pytest` test suite (30 assertions), and all defects were logged across 5 standard engineering defect categories.

---

## 📂 Submission Directory Layout

```
Assignment-4-AI-Coding-Workflow/
├── README.md                          # Productivity analysis & methodology documentation
├── Assignment-04-23EG107E19.pdf       # Compiled formal assessment PDF report
├── time-log.csv                       # Granular time logs (Unassisted vs Gen, Review, Correct)
├── defect-log.csv                     # 10 Defect logs across Logic, Edge, Security, Perf, Style
├── tasks/                             # 10 development tasks (unassisted.py & assisted.py)
│   ├── task01/                        # [Boilerplate] Email & password strength validator
│   ├── task02/                        # [Boilerplate] CSV to JSON record converter
│   ├── task03/                        # [Algorithms] Palindrome words & longest substring
│   ├── task04/                        # [Algorithms] Running balance & overdraft detector
│   ├── task05/                        # [Refactoring] Nested discount calculator cleanup
│   ├── task06/                        # [Refactoring] Unicode and whitespace normalizer
│   ├── task07/                        # [Test Writing] Unit test suite for cart price engine
│   ├── task08/                        # [Debugging] Binary search off-by-one boundary fix
│   ├── task09/                        # [Debugging] Python mutable default argument fix
│   └── task10/                        # [Integration] Weather JSON parser & formatter
├── tests/                             # Independent pytest test suites (30 tests)
│   ├── test_task01.py ... test_task10.py
├── results/
│   └── benchmark_summary.csv          # Category benchmark dataset
└── graphs/
    ├── time_spent_breakdown.png       # Stacked time comparison per task
    ├── net_productivity_by_type.png   # Net productivity gain % by category
    ├── defect_distribution.png        # Categorization across the 5 defect types
    └── acceptance_rate_by_type.png    # Code acceptance rate (% lines kept)
```

---

## 📊 Summary Benchmark Table

| Category | Tasks | Unassisted Time | AI Gen Time | Review Time | Correction Time | Total Assisted Time | Net Productivity Gain (%) | Acceptance Rate (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Boilerplate** | 2 | 47.0 min | 4.0 min | 7.0 min | 3.0 min | 14.0 min | **+70.2%** | **90.5%** |
| **Test Writing** | 1 | 32.0 min | 3.0 min | 6.0 min | 2.0 min | 11.0 min | **+65.6%** | **90.0%** |
| **Integration** | 1 | 26.0 min | 2.0 min | 5.0 min | 3.0 min | 10.0 min | **+61.5%** | **84.6%** |
| **Algorithms** | 2 | 58.0 min | 5.0 min | 14.0 min | 8.0 min | 27.0 min | **+53.4%** | **78.4%** |
| **Refactoring** | 2 | 55.0 min | 5.0 min | 13.0 min | 8.0 min | 26.0 min | **+52.7%** | **78.5%** |
| **Debugging** | 2 | 33.0 min | 5.0 min | 15.0 min | 13.0 min | 33.0 min | **0.0% (Break-even)** | **56.0%** |
| **TOTAL / AVG** | **10** | **251.0 min** | **24.0 min** | **60.0 min** | **37.0 min** | **121.0 min** | **+51.8%** | **78.2%** |

---

## 🐛 Defect Taxonomy Caught Across 5 Categories

During independent verification of generated code, 10 distinct defects were identified and logged in `defect-log.csv`:
1. **Logic (3 defects)**: Overdraft counter logic bug (`task04`), binary search boundary miss (`task08`), mutable default argument persistence (`task09`).
2. **Edge Case (2 defects)**: Age validation boundary limits (`task01`), CSV header trailing whitespace (`task02`).
3. **Security (2 defects)**: Negative price exploit (`task05`), unescaped HTML/XSS injection (`task06`).
4. **Performance (1 defect)**: $O(N^3)$ brute force substring search bottleneck on long strings (`task03`).
5. **Style (2 defects)**: Missing negative exception test assertions (`task07`), floating point display formatting (`task10`).

---

## 🏆 Key Academic Takeaways

1. **Overall Net Productivity Gain**: **+51.8%** across the 10-task suite (Total development time reduced from 251 mins to 121 mins).
2. **Review Overhead Reality**: AI generation took only **24 minutes**, but reviewing and correcting subtle defects took **97 minutes (80% of total assisted time)**.
3. **Debugging Break-Even (0.0% Gain)**: On subtle logic bugs (off-by-one boundary conditions, mutable default arguments), AI generated plausible-looking code that retained the exact bug, taking as long to audit and fix as solving it manually from scratch.

---

## 📄 Assessment Report
The compiled academic assessment report is available in [`Assignment-04-23EG107E19.pdf`](./Assignment-04-23EG107E19.pdf).
