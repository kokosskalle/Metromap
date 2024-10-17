# app.py

import streamlit as st

st.title('Heart Failure Care Pathway Flowchart in Region Stockholm')

# Define the Graphviz DOT code for the flowchart
dot = '''
digraph heart_failure_flowchart {
  rankdir=TB;
  node [shape=rectangle, style=filled, fontcolor=black, fontsize=12];

  // Define nodes with labels and colors
  SymptomOnset [label="Symptom Onset", fillcolor="gold"];
  PrimaryCare [label="Primary Care Consultation", fillcolor="gold"];
  DiagnosticTesting [label="Diagnostic Testing", fillcolor="gold"];
  ReferralCardiology [label="Referral to Cardiology", fillcolor="skyblue"];
  AdvancedDiagnostics [label="Advanced Diagnostics", fillcolor="skyblue"];
  TreatmentInitiation [label="Treatment Initiation", fillcolor="lightgreen"];
  LifestyleModification [label="Lifestyle Modification", fillcolor="green"];
  DeviceTherapy [label="Device Therapy", fillcolor="fuchsia"];
  RehabilitationPrograms [label="Rehabilitation Programs", fillcolor="#20B2AA"];
  FollowUpCare [label="Follow-up Care", fillcolor="#8B008B"];
  AdvancedTherapies [label="Advanced Therapies", fillcolor="darkblue"];
  PalliativeCare [label="Palliative Care", fillcolor="orange"];

  // Define edges with labels
  SymptomOnset -> PrimaryCare [label="1 week"];
  PrimaryCare -> DiagnosticTesting [label="2 weeks"];
  DiagnosticTesting -> ReferralCardiology [label="Abnormal results", style=dashed];
  ReferralCardiology -> AdvancedDiagnostics;
  AdvancedDiagnostics -> TreatmentInitiation [label="1 month"];
  TreatmentInitiation -> LifestyleModification [label="Ongoing"];
  LifestyleModification -> DeviceTherapy [label="If symptoms persist", style=dashed];
  DeviceTherapy -> RehabilitationPrograms;
  RehabilitationPrograms -> FollowUpCare;
  FollowUpCare -> AdvancedTherapies [label="If condition worsens", style=dashed];
  AdvancedTherapies -> PalliativeCare [label="If necessary", style=dashed];

  // High-risk indicator
  AdvancedDiagnostics -> DeviceTherapy [label="High Risk", color=red, fontcolor=red];

  // Milestone
  TreatmentInitiation -> Milestone [label="Milestone Reached", style=dotted];
  Milestone [shape=diamond, label="", width=0.1, style=filled, fillcolor="white"];

  // Hospital node
  ReferralCardiology -> Hospital [label="Referral", style=dotted];
  Hospital [shape=house, label="Hospital", style=filled, fillcolor="white"];

  // Legend
  subgraph cluster_legend {
    label="Legend";
    labelloc="t";
    fontsize=16;
    style=dashed;

    key [label=<
      <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD BGCOLOR="gold" WIDTH="20"></TD><TD>1st Line Diagnostics</TD></TR>
        <TR><TD BGCOLOR="skyblue"></TD><TD>2nd Line Diagnostics</TD></TR>
        <TR><TD BGCOLOR="lightgreen"></TD><TD>Treatment Initiation</TD></TR>
        <TR><TD BGCOLOR="green"></TD><TD>Lifestyle Modification</TD></TR>
        <TR><TD BGCOLOR="fuchsia"></TD><TD>Device Therapy</TD></TR>
        <TR><TD BGCOLOR="#20B2AA"></TD><TD>Rehabilitation Programs</TD></TR>
        <TR><TD BGCOLOR="#8B008B"></TD><TD>Follow-up Care</TD></TR>
        <TR><TD BGCOLOR="darkblue"></TD><TD>Advanced Therapies</TD></TR>
        <TR><TD BGCOLOR="orange"></TD><TD>Palliative Care</TD></TR>
      </TABLE>
    >, shape=none]
  }
}
'''

# Render the graph using Streamlit's built-in function
st.graphviz_chart(dot)
