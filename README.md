# Adverse Drug Reaction (ADR) Data Analysis

Internship project completed as part of the Data Analytics (Healthcare/Pharmacy)
internship at VirtualWorks Lab (by Noivrn).

**Intern:** Sudesh Ganesh Jagadale
**Task:** Task 4 — Adverse Drug Reaction (ADR) Data Analysis

---

## Objective

Analyze healthcare datasets containing patient symptoms, medication usage,
and timelines to identify possible adverse drug reactions (ADRs). Correlate
symptoms with drugs, identify high-risk medicines, and evaluate possible
causes of reactions.

## Dataset

`adr_data.csv` contains 1,248 ADR reports covering 12 commonly used
medicines, including patient age, gender, drug, reaction, severity,
onset time, and outcome.

## Approach

1. Cleaned the dataset — removed duplicate reports, standardized gender
   values, fixed invalid onset-day entries, filled missing ages
2. Correlated drugs with their most frequently reported reactions
3. Ranked medicines by serious-case rate to identify high-risk drugs
4. Analyzed onset timelines (days from starting a drug to reaction onset)
5. Reviewed patient outcomes

## Key Findings

- **1,248 total ADR reports**, of which **210 (16.8%) were Serious**
- Most common reactions: Nausea, Headache, Rash, Dizziness, Diarrhea
- **High-risk medicines** (highest serious-case rates): Atorvastatin,
  Warfarin, Azithromycin, Insulin, Losartan, Amlodipine
- Onset timing (14–17 days on average) did not strongly predict severity
- 56 patients required hospitalization

## Files

- `adr_data.csv` — raw ADR dataset
- `cleaned_adr_data.csv` — cleaned dataset
- `adr_analysis.py` — full cleaning & analysis script
- `adr_analysis_summary.txt` — analysis output
- `severity_distribution.png` — severity breakdown chart
- `high_risk_drugs.png` — serious-case rate by drug chart
- `top_reactions.png` — most common reactions chart
- `ADR_Project_Report.md` — full written report

## Tools Used

- **Python 3**
- **pandas** — data cleaning and analysis
- **matplotlib** — data visualization
