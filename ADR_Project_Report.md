# Adverse Drug Reaction (ADR) Data Analysis
**Internship Task 4 — VirtualWorks Lab**
**Submitted by:** Sudesh Ganesh Jagadale

---

## 1. Objective

Analyze healthcare datasets containing patient symptoms, medication usage,
and timelines to identify possible adverse drug reactions (ADRs). Correlate
symptoms with drugs, identify high-risk medicines, and evaluate possible
causes of reactions.

## 2. Dataset

An ADR reporting dataset (`adr_data.csv`) with **1,248 reports** (after
removing 10 duplicate entries) covering 12 commonly used medicines.

| Column | Description |
|---|---|
| ReportID | Unique ADR report identifier |
| Date | Date the reaction was reported |
| PatientAge | Patient's age |
| PatientGender | Patient's gender |
| Drug | Medicine associated with the reaction |
| Reaction | Reported adverse reaction/symptom |
| Severity | Mild / Moderate / Serious |
| Onset_Days | Days between starting the drug and the reaction appearing |
| Outcome | Patient outcome (Recovered, Recovering, Not Recovered, Hospitalized) |

## 3. Data Cleaning

- Removed 10 exact duplicate reports
- Standardized gender values into consistent categories (Male/Female/Unknown)
- Corrected invalid onset-day values (negative entries treated as missing, then filled with the median)
- Filled missing patient ages with the median age

Result: **1,248 clean ADR reports** used for analysis.

## 4. Key Metrics

| Metric | Value |
|---|---|
| Total ADR Reports | 1,248 |
| Serious Cases | 210 (16.8%) |
| Mild Cases | 647 |
| Moderate Cases | 391 |

*(See `severity_distribution.png` for the chart.)*

## 5. Drug–Reaction Correlation

The most frequently reported drug-reaction pairs include Losartan with
Dizziness (57 reports), Amlodipine with Dizziness (45 reports), and
Metformin with Diarrhea (43 reports).

The most commonly reported reactions overall, across all drugs, are:
**Nausea (151), Headache (134), Rash (115), Dizziness (102), and
Diarrhea (82).**

## 6. High-Risk Medicines

Ranking medicines by their **serious-case rate** (% of reports classified
as Serious) highlights the riskiest drugs in this dataset:

| Drug | Total Reports | Serious Cases | Serious Rate (%) |
|---|---|---|---|
| Atorvastatin | 98 | 31 | 31.6% |
| Warfarin | 96 | 26 | 27.1% |
| Azithromycin | 102 | 26 | 25.5% |
| Insulin | 94 | 22 | 23.4% |
| Losartan | 135 | 21 | 15.6% |
| Amlodipine | 108 | 16 | 14.8% |

**Medicines flagged as high-risk** (above-median serious-case rate):
**Atorvastatin, Warfarin, Azithromycin, Insulin, Losartan, Amlodipine.**

This aligns with known clinical risk profiles — Warfarin (bleeding risk),
Insulin (hypoglycemia risk), and Atorvastatin (liver enzyme/muscle effects)
are all medicines that require closer monitoring in real practice.

*(See `high_risk_drugs.png` for the chart.)*

## 7. Onset Timeline Analysis

Average onset time (days from starting the drug to the reaction appearing)
ranges narrowly from **14.3 to 16.9 days** across medicines, with no single
drug showing a dramatically faster or delayed onset. Onset time does not
vary meaningfully by severity either (Mild: 15.8 days, Moderate: 15.6 days,
Serious: 16.0 days) — suggesting that in this dataset, how quickly a
reaction appears is not a strong predictor of how serious it will be.

## 8. Patient Outcomes

| Outcome | Count |
|---|---|
| Recovered | 819 |
| Recovering | 258 |
| Not Recovered | 115 |
| Hospitalized | 56 |

The majority of patients (66%) recovered fully, but **56 cases required
hospitalization**, reinforcing the importance of monitoring the high-risk
medicines identified above.

## 9. Possible Causes & Recommendations

- Drugs with higher serious-case rates (Atorvastatin, Warfarin, Azithromycin, Insulin) warrant closer post-prescription monitoring, especially in older patients.
- Common but usually mild reactions (Nausea, Headache, Rash) appear across many drug classes and are likely general tolerability issues rather than drug-specific red flags.
- Since onset timing doesn't strongly predict severity, monitoring should continue throughout the full course of treatment, not just the first few days.

## 10. Tools Used

- **Python** with **pandas** for cleaning and analysis, **matplotlib** for charts
- Full reproducible script: `adr_analysis.py`

## 11. Files Submitted

- `adr_data.csv` — raw ADR dataset
- `adr_analysis.py` — full cleaning & analysis script
- `cleaned_adr_data.csv` — cleaned dataset
- `analysis_summary.txt` — analysis output
- `severity_distribution.png` — severity breakdown chart
- `high_risk_drugs.png` — serious-case rate by drug chart
- `top_reactions.png` — most common reactions chart
- `Project_Report.md` — this report
