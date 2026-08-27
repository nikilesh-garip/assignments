# Assignment 5: Document Extraction Pipeline with Accuracy Measurement
## Course: Generative AI & Prompt Engineering Laboratory
### Student Practical Submission

---

## 📌 Executive Summary
In BFSI back-office operations (banking, insurance claims, identity cards), aggregate document accuracy figures can be misleading—a system with 95% overall accuracy can fail catastrophically if high error rates are concentrated in financial fields like `tax_id` or `diagnosis_code`.

In this assignment, I designed a **document extraction and validation pipeline** evaluated against a **manually verified ground truth dataset of 105 documents** across 3 distinct document layouts (**Commercial Invoices, Health Insurance Claims, and National Identity Cards**). The system features field-level accuracy benchmarking, confidence calibration, automated human review routing, and per-document unit economics modeling.

---

## 📂 Submission Directory Layout

```
Assignment-5-Document-Extraction/
├── README.md                          # Pipeline documentation & routing guide
├── Assignment-05-23EG107E19.pdf       # Compiled formal assessment PDF report
├── src/                               # Pipeline core modules (schema.py, extractor.py, routing.py)
├── data/                              # 105 sample synthetic document text files
│   ├── invoices/                      # 35 Commercial tax invoice documents
│   ├── insurance_claims/              # 35 Health insurance claim documents
│   └── id_cards/                      # 35 National identity card documents
├── ground-truth/
│   └── ground_truth.csv               # 105-document verified ground truth dataset
├── results/
│   ├── extraction_results.csv         # Full 105-doc extraction, confidence & routing records
│   ├── field_accuracy_report.csv      # Field-by-field accuracy matrix (clean vs noisy scans)
│   └── confidence_calibration.csv     # Model confidence vs empirical true accuracy
└── graphs/
    ├── field_level_accuracy.png       # Field accuracy comparison across schemas
    ├── confidence_calibration.png     # Confidence calibration curve
    ├── routing_distribution.png       # Auto-accept vs Review vs Rejection proportions
    └── cost_comparison.png            # Unit economics and cost comparison chart
```

---

## 📊 Summary Benchmark Results

### 1. Document Routing Proportions ($N = 105$ Documents)

| Routing Destination | Routing Policy Condition | Documents (n) | Proportion (%) | Operational Action |
| :--- | :--- | :---: | :---: | :--- |
| **Auto-Accepted** | All required fields $\ge 0.85$ confidence + valid schema | **66** | **62.9%** | Direct database ingestion with 0 human overhead. |
| **Human Review Queue** | Any required field $0.50 \le \text{confidence} < 0.85$ | **24** | **22.9%** | Flagged for 45-second specialist review. |
| **Rejected** | Confidence $< 0.50$ or corrupted layout | **15** | **14.3%** | Returned with rejection reason code. |

---

### 2. Field-Level Accuracy Breakdown

| Document Type | Field Name | Clean Scan Accuracy (%) | Noisy Scan Accuracy (%) | Overall Accuracy (%) | Mean Confidence |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Invoice** | `invoice_number` | 100.0% | 100.0% | **100.0%** | 0.896 |
| **Invoice** | `vendor_name` | 100.0% | 100.0% | **100.0%** | 0.896 |
| **Invoice** | `tax_id` (GSTIN) | 100.0% | 100.0% | **100.0%** | 0.883 |
| **Invoice** | `subtotal` | 100.0% | 87.5% | **96.7%** | 0.882 |
| **Invoice** | `tax_amount` | 100.0% | 87.5% | **96.7%** | 0.882 |
| **Invoice** | `total_amount` | 100.0% | 87.5% | **96.7%** | 0.882 |
| **Insurance Claim** | `claim_id` | 100.0% | 100.0% | **100.0%** | 0.883 |
| **Insurance Claim** | `diagnosis_code` (ICD-10) | 100.0% | 100.0% | **100.0%** | 0.803 (Routed to review) |
| **ID Card** | `id_number` | 100.0% | 100.0% | **100.0%** | 0.909 |
| **ID Card** | `date_of_birth` | 100.0% | 100.0% | **100.0%** | 0.909 |

---

## 💰 Unit Economics & Financial Impact

| Metric | Manual Baseline | AI Pipeline + Human Review | Delta / Savings |
| :--- | :---: | :---: | :---: |
| **Cost per Document** | **$1.50** | **$0.116** | **-92.3% per doc** |
| **Monthly Cost (10,000 docs)** | **$15,000.00** | **$1,159.00** | **$13,841.00 / month saved** |
| **Average Processing Time** | 3.0 minutes | Instant (< 2 seconds) | 98.9% cycle time reduction |

---

## 🏆 Key Academic Insights

1. **The Critical Need for Field-Level Measurement**: While overall document accuracy averaged 98.8%, low-confidence fields (`diagnosis_code` with confidence 0.803) were properly flagged and routed to the human review queue. Field-level tracking prevents silent failures in downstream financial ledgers.
2. **Calibrated Confidence**: Assigned confidence scores strongly mirrored true accuracy (0.85–1.00 confidence bucket yielded **100.0% empirical accuracy**), ensuring auto-accepted documents are safe for database ingestion.
3. **Safe Rejection**: All 15 corrupted/unreadable document scans were successfully rejected with low confidence (< 0.20), preventing garbled data from entering the pipeline.

---

## 📄 Assessment Report
The compiled academic assessment report is available in [`Assignment-05-23EG107E19.pdf`](./Assignment-05-23EG107E19.pdf).
