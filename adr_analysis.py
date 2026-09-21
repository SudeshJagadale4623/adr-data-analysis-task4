"""
Adverse Drug Reaction (ADR) Data Analysis
--------------------------------------------
Internship Task 4 - VirtualWorks Lab

Steps:
1. Load and clean the ADR dataset
2. Correlate symptoms/reactions with drugs
3. Identify high-risk medicines
4. Evaluate onset timelines and possible causes
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

pd.set_option("display.width", 120)

# ---------------------------------------------------------
# STEP 1: LOAD & CLEAN
# ---------------------------------------------------------
df = pd.read_csv("adr_data.csv")

print("=" * 60)
print("STEP 1: DATA OVERVIEW & CLEANING")
print("=" * 60)
print(f"Raw shape: {df.shape}")
print("\nMissing values:")
print(df.isnull().sum())
print(f"\nDuplicate rows: {df.duplicated().sum()}")

before = len(df)
df = df.drop_duplicates()
print(f"Removed {before - len(df)} duplicate reports.")

# Standardize gender
gender_map = {"male": "Male", "Male": "Male", "m": "Male", "M": "Male",
              "female": "Female", "Female": "Female", "f": "Female", "F": "Female"}
df["PatientGender"] = df["PatientGender"].astype(str).str.strip().map(gender_map)
df["PatientGender"] = df["PatientGender"].fillna("Unknown")

# Fix invalid onset days (negative -> missing), then fill with median
df.loc[df["Onset_Days"] < 0, "Onset_Days"] = pd.NA
df["Onset_Days"] = df["Onset_Days"].fillna(df["Onset_Days"].median())

# Fill missing age with median
df["PatientAge"] = df["PatientAge"].fillna(df["PatientAge"].median()).round().astype(int)

df.to_csv("cleaned_adr_data.csv", index=False)
print(f"\nCleaned shape: {df.shape}")
print("Cleaned dataset saved to 'cleaned_adr_data.csv'")

# ---------------------------------------------------------
# STEP 2: OVERALL ADR METRICS
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 2: OVERALL METRICS")
print("=" * 60)

total_reports = len(df)
serious_count = (df["Severity"] == "Serious").sum()
serious_pct = serious_count / total_reports * 100

print(f"Total ADR Reports: {total_reports}")
print(f"Serious Cases: {serious_count} ({serious_pct:.1f}%)")

severity_counts = df["Severity"].value_counts()
print("\nSeverity distribution:")
print(severity_counts)

# ---------------------------------------------------------
# STEP 3: CORRELATE SYMPTOMS WITH DRUGS
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 3: DRUG-REACTION CORRELATION")
print("=" * 60)

drug_reaction_counts = df.groupby(["Drug", "Reaction"]).size().sort_values(ascending=False)
print("\nTop 15 drug-reaction pairs (most frequently reported):")
print(drug_reaction_counts.head(15))

top_reactions = df["Reaction"].value_counts().head(10)
print("\nMost commonly reported reactions overall:")
print(top_reactions)

# ---------------------------------------------------------
# STEP 4: IDENTIFY HIGH-RISK MEDICINES
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 4: HIGH-RISK MEDICINE IDENTIFICATION")
print("=" * 60)

drug_summary = df.groupby("Drug").agg(
    Total_Reports=("ReportID", "count"),
    Serious_Cases=("Severity", lambda x: (x == "Serious").sum()),
).reset_index()
drug_summary["Serious_Rate_%"] = (drug_summary["Serious_Cases"] / drug_summary["Total_Reports"] * 100).round(1)
drug_summary = drug_summary.sort_values("Serious_Rate_%", ascending=False)

print("\nDrugs ranked by serious-case rate (high-risk medicines):")
print(drug_summary.to_string(index=False))

high_risk = drug_summary[drug_summary["Serious_Rate_%"] >= drug_summary["Serious_Rate_%"].median()]
print(f"\nMedicines flagged as high-risk (above median serious rate): {', '.join(high_risk['Drug'].tolist())}")

# ---------------------------------------------------------
# STEP 5: ONSET TIMELINE ANALYSIS
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 5: ONSET TIMELINE ANALYSIS")
print("=" * 60)

avg_onset_by_drug = df.groupby("Drug")["Onset_Days"].mean().round(1).sort_values()
print("\nAverage onset time (days from starting drug to reaction) by drug:")
print(avg_onset_by_drug)

avg_onset_by_severity = df.groupby("Severity")["Onset_Days"].mean().round(1)
print("\nAverage onset time by severity:")
print(avg_onset_by_severity)

outcome_counts = df["Outcome"].value_counts()
print("\nPatient outcomes:")
print(outcome_counts)

# ---------------------------------------------------------
# CHARTS
# ---------------------------------------------------------
# Severity distribution pie chart
plt.figure(figsize=(5, 5))
severity_counts.plot(kind="pie", autopct="%1.1f%%", colors=["#10b981", "#f59e0b", "#ef4444"])
plt.title("ADR Severity Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("severity_distribution.png", dpi=120)
plt.close()

# Serious case rate by drug
plt.figure(figsize=(8, 5))
drug_summary.set_index("Drug")["Serious_Rate_%"].sort_values().plot(kind="barh", color="#ef4444")
plt.title("Serious Case Rate (%) by Medicine")
plt.xlabel("Serious Case Rate (%)")
plt.tight_layout()
plt.savefig("high_risk_drugs.png", dpi=120)
plt.close()

# Top reactions bar chart
plt.figure(figsize=(8, 5))
top_reactions.sort_values().plot(kind="barh", color="#3b82f6")
plt.title("Most Commonly Reported Reactions")
plt.xlabel("Number of Reports")
plt.tight_layout()
plt.savefig("top_reactions.png", dpi=120)
plt.close()

print("\nCharts saved: severity_distribution.png, high_risk_drugs.png, top_reactions.png")

# ---------------------------------------------------------
# SAVE TEXT SUMMARY
# ---------------------------------------------------------
with open("analysis_summary.txt", "w") as f:
    f.write("ADVERSE DRUG REACTION (ADR) ANALYSIS SUMMARY\n")
    f.write("=" * 45 + "\n\n")
    f.write(f"Total ADR Reports: {total_reports}\n")
    f.write(f"Serious Cases: {serious_count} ({serious_pct:.1f}%)\n\n")
    f.write("Severity distribution:\n")
    f.write(severity_counts.to_string() + "\n\n")
    f.write("Top drug-reaction pairs:\n")
    f.write(drug_reaction_counts.head(15).to_string() + "\n\n")
    f.write("High-risk medicines (serious-case rate):\n")
    f.write(drug_summary.to_string(index=False) + "\n\n")
    f.write("Average onset time by drug (days):\n")
    f.write(avg_onset_by_drug.to_string() + "\n\n")
    f.write("Average onset time by severity (days):\n")
    f.write(avg_onset_by_severity.to_string() + "\n\n")
    f.write("Patient outcomes:\n")
    f.write(outcome_counts.to_string() + "\n")

print("\nSummary written to 'analysis_summary.txt'")
