# Causal Inference Tutorial

This tutorial shows how to move from observed data to a causal estimate.

The tutorial uses a backdoor defense example and is organized into three notebooks:

```text
00_data_preparation.ipynb
        ↓
01_correlational_analysis.ipynb
        ↓
02_causal_inference.ipynb
```

The causal question is:

> **To what extent does applying the backdoor defense, instead of baseline random filtering, cause the probability of successful backdoor detection to change?**

The notebooks use `treatment` and `outcome` as column names:

- `treatment = 0`: baseline random filtering;
- `treatment = 1`: backdoor defense;
- `outcome = 0`: detection failed;
- `outcome = 1`: detection succeeded.

In this tutorial:

| Variable | Value | Meaning |
|---|---:|---|
| `treatment` | `0` | Random filtering is used |
| `treatment` | `1` | The backdoor defense is used |
| `outcome` | `0` | Detection failed |
| `outcome` | `1` | Detection succeeded |

The average of `outcome` is the **Detection Success Rate**, or **DSR**.

The causal effect compares detection success under the backdoor defense with detection success under random filtering.

---

# Tutorial structure

## 00 — Data preparation

Notebook:

```text
00_data_preparation.ipynb
```

This notebook prepares the data used in the rest of the tutorial.

It:

1. loads the code and docstring data;
2. extracts numeric features from the code;
3. creates the treatment and outcome used in the tutorial;
4. creates additional variables used in the causal example;
5. checks the resulting data;
6. saves the data for the next notebooks.

The output is:

```text
data/causal_data.csv
```

Each row represents one software example.

Each example has:

- one observed treatment;
- one observed outcome;
- measured variables that may be relevant to the causal analysis.

For one example, we observe either:

```text
treatment = 0
```

or:

```text
treatment = 1
```

We do not observe the same example under both treatments.

This is why causal inference is needed.

---

# 01 — Correlational analysis

Notebook:

```text
01_correlational_analysis.ipynb
```

This notebook explores relationships in the data prepared by notebook 00.

It examines:

- the DSR under random filtering;
- the DSR under backdoor defense;
- correlations among variables;
- differences between the two treatment groups;
- standardized mean differences;
- association with treatment;
- association with outcome;
- selected pairwise relationships.

All plots use Seaborn.

The purpose of this notebook is to understand the observed data before building the causal graph.

A variable that is associated with both treatment and outcome is not automatically a confounder.

For example, this pattern:

```text
X is associated with treatment
X is associated with outcome
```

could be produced by:

```text
X → treatment
X → outcome
```

but it could also be produced by:

```text
treatment → X → outcome
```

or:

```text
treatment → X ← outcome
```

Correlation alone cannot tell us which structure is correct.

The notebook therefore also considers when variables are measured and whether they occur before or after treatment.

At the end of the notebook, it creates:

```text
data/dag_worksheet.csv
```

The worksheet contains the statistical results and space to record:

- a proposed causal role;
- proposed graph edges;
- a reason for each proposed edge.

The worksheet is used in notebook 02.

---

# 02 — Causal inference

Notebook:

```text
02_causal_inference.ipynb
```

This notebook uses the data and the worksheet from the first two notebooks.

The goal is to estimate:

> **To what extent does applying the backdoor defense, instead of baseline random filtering, cause the probability of successful backdoor detection to change?**

The notebook follows this sequence:

```text
causal assumptions
        ↓
DAG
        ↓
identification
        ↓
estimation
        ↓
refutation
```

## Build the DAG

The graph begins with:

```text
treatment → outcome
```

This edge represents the causal effect that we want to study.

You then decide which additional edges belong in the graph.

Use:

- the results from notebook 01;
- the timing of each variable;
- knowledge about how the variables could affect one another.

Do not add an edge only because two variables are correlated.

For every proposed edge:

```text
A → B
```

ask:

1. Does A occur before B?
2. Can A plausibly change B?
3. Could the observed relationship have another explanation?

The graph interface uses different colors to show different graph roles.

The roles come from the graph that you build.

They are not inferred from the correlation matrix.

---

# Identification

After the DAG is frozen, DoWhy checks whether the causal effect can be identified from the observed data.

Identification asks:

> **If this DAG is correct, what quantity in the observed data corresponds to the effect of using the backdoor defense instead of random filtering on successful detection?**

The tutorial uses the **Average Treatment Effect**, or **ATE**.

```text
ATE = E[Y(1) - Y(0)]
```

Here:

```text
Y(1)
```

is the detection result if the backdoor defense is used.

```text
Y(0)
```

is the detection result if random filtering is used.

The ATE compares these two conditions on average.

---

# Estimation

The tutorial estimates the ATE using inverse propensity score weighting. Here, the ATE measures the average change in detection success caused by using the backdoor defense instead of random filtering.

For a binary outcome, the result can be interpreted as a change in detection probability.

For example:

```text
Estimated ATE = 0.08
```

means:

> The backdoor defense is estimated to increase the probability of successful detection by about 8 percentage points on average compared with random filtering.

If the estimate is negative, the backdoor defense is estimated to reduce detection success.

---

# Refutation

The tutorial runs checks that test how stable the estimate is.

These include:

- placebo treatment;
- random common cause.

These checks can reveal problems with an estimate.

They do not prove that the causal graph is correct.

They also do not prove that every important variable has been measured.

---

# Reveal

The tutorial includes a synthetic causal process so that the correct graph and causal effect are known.

The project contains:

```text
data/synthetic_ground_truth_edges.csv
```

Notebook 00 also creates:

```text
data/synthetic_study_metadata.json
```

Do not inspect these files before the reveal section in notebook 02 if you want to complete the graph exercise first.

At the end of notebook 02, you compare:

```text
your proposed graph
```

with:

```text
the graph used to create the synthetic data
```

You also compare your estimated ATE with the known synthetic ATE.

This makes it possible to see which conclusions could and could not be reached from correlation alone.

---

# What the tutorial demonstrates

The tutorial separates three different ideas.

## Measurement

```text
code_complexity = 4
```

This is an observed value.

## Association

```text
code_complexity is associated with treatment
```

This describes a pattern in the data.

## Causal claim

```text
code_complexity → treatment
```

This says that code complexity affects treatment assignment.

An association does not automatically imply the causal claim.

The causal graph makes these assumptions explicit.

---

# Tutorial sequence

Run the tutorial in this order:

1. Open `00_data_preparation.ipynb`.
2. Run the notebook from top to bottom.
3. Open `01_correlational_analysis.ipynb`.
4. Study the plots and tables.
5. Complete the DAG worksheet.
6. Open `02_causal_inference.ipynb`.
7. Build the causal graph.
8. Freeze the graph.
9. Identify the causal effect.
10. Estimate the ATE.
11. Run the refutation checks.
12. Reveal the synthetic graph and known ATE.
13. Compare the proposed graph with the graph used to create the data.

---

# Project files

```text
ci4se-backdoor-defense-tutorial/
│
├── 00_data_preparation.ipynb
├── 01_correlational_analysis.ipynb
├── 02_causal_inference.ipynb
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw_code.csv
│   └── synthetic_ground_truth_edges.csv
│
├── slides/
│   └── Causal_interpretability.pdf
│
└── src/
    ├── __init__.py
    ├── causal_data_prep.py
    ├── correlational_analysis_utils.py
    ├── causal_graph_ui.py
    └── causal_tutorial_utils.py
```

The notebooks contain the tutorial.

The files in `src/` contain supporting Python code.

The slides are optional.

---

# Setup

From the project directory:

```bash
python -m venv .venv
```

Activate the environment.

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter lab
```

Then begin with:

```text
00_data_preparation.ipynb
```

The causal inference notebook uses DoWhy 0.14.
