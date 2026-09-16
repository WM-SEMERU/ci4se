# Causal Inference Tutorial: Backdoor Defense

This tutorial uses a backdoor-defense example to teach the difference between **correlation** and **causation**.

Run the notebooks in order:

```text
00_data_preparation.ipynb
        ↓
01_correlational_analysis.ipynb
        ↓
02_causal_inference.ipynb
```

Each notebook answers a different question:

| Notebook | Main question |
|---|---|
| 00 — Data preparation | **What was observed for each unit?** |
| 01 — Correlational analysis | **What patterns are visible in the observed data?** |
| 02 — Causal inference | **To what extent does treatment cause outcome?** |

---

## The causal question

The central causal question is:

> **To what extent does `treatment` cause a change in `outcome`?**

In the backdoor-defense setting:

> **To what extent does applying the backdoor defense, instead of baseline random filtering, cause the probability of successful backdoor detection to change?**

### Treatment

`treatment` is binary:

| Value | Meaning |
|---|---|
| `0` | **Random filtering** — the baseline/control condition |
| `1` | **Backdoor defense** — the dedicated defense is applied |

The tutorial does not depend on the implementation details of a particular defense algorithm. The treatment variable represents the contrast between **using the dedicated backdoor defense** and **using the baseline random-filtering procedure**.

### Outcome

`outcome` is also binary:

| Value | Meaning |
|---|---|
| `0` | the backdoor was **not detected successfully** |
| `1` | the backdoor was **detected successfully** |

The mean of `outcome` is the **Detection Success Rate (DSR)**.

For example, if 70% of units have `outcome = 1`, then the DSR is `0.70` or 70%.

---

## What does “causal effect” mean here?

For each unit, imagine two potential outcomes:

- **Y(1):** detection success if the backdoor defense were applied;
- **Y(0):** detection success if random filtering were used instead.

We never observe both for the same unit. We observe only the outcome under the treatment that the unit actually received.

The tutorial targets the **Average Treatment Effect (ATE)**:

```text
ATE = E[Y(1) - Y(0)]
```

Because the outcome is binary, the ATE is a difference in detection-success probability.

For example:

```text
ATE = 0.10
```

means an estimated **10 percentage-point increase in detection success rate** caused by using the backdoor defense rather than random filtering, on average.

That is the quantity notebook 02 tries to estimate.

---

## What is real and what is synthetic?

The raw data contain code/docstring examples that provide realistic variation in software characteristics.

For this teaching exercise, the following are synthetic:

- assignment to random filtering or backdoor defense;
- detection success/failure;
- several context/process variables used to create different causal structures.

This is deliberate. A synthetic data-generating process lets us know the true causal graph and true ATE, so after completing the analysis we can compare our reasoning with the answer.

The generated values should therefore be interpreted as a **teaching study**, not as empirical evidence about the effectiveness of a real backdoor-defense system.

---

## Do not reveal the answer too early

The project contains:

```text
data/synthetic_ground_truth_edges.csv
```

Notebook 00 also generates:

```text
data/synthetic_study_metadata.json
```

These files contain information used in the final reveal.

**Do not inspect them before the reveal section in notebook 02** if you want to complete the causal-graph exercise yourself.

The implementation in `src/causal_data_prep.py` also contains the synthetic generator, so avoid reading that implementation until after the exercise if you want the full challenge.

---

# Project structure

```text
ci4se-master/
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
├── cache/
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

The notebooks are the student-facing learning material. The `src/` folder keeps implementation details out of the main narrative.

The slide deck is optional background material and is not required to run the notebooks.

---

# Setup

From the project directory, create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### macOS or Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter lab
```

Then run the notebooks in numerical order.

The causal-inference notebook targets **DoWhy 0.14**.

---

# 00 — Data Preparation

Open:

```text
00_data_preparation.ipynb
```

## Goal

Create a valid unit-level dataset for the backdoor-defense causal study.

Each row represents one software example with:

- one observed treatment;
- one observed detection outcome;
- measured variables that may be relevant to the causal graph.

## What happens in this notebook?

The notebook:

1. loads the code/docstring examples;
2. extracts readable code features such as token count and cyclomatic complexity;
3. generates the synthetic observational backdoor-defense study;
4. validates the resulting causal table;
5. saves the dataset used by the next notebooks.

The output is:

```text
data/causal_data.csv
```

## Important idea

Each unit appears **once** with one observed treatment and one observed outcome.

We do not duplicate a unit under both treatment conditions. The unobserved alternative is a **counterfactual**.

## Transition to notebook 01

After notebook 00, we know:

> **what was observed.**

We still do not know:

> **which observed relationships are causal.**

Notebook 01 explores those relationships without making causal claims.

---

# 01 — Correlational Analysis

Open:

```text
01_correlational_analysis.ipynb
```

## Goal

Understand the observed data before constructing the causal graph.

The notebook examines:

- the raw DSR under random filtering and backdoor defense;
- pairwise correlations;
- treatment-group imbalance;
- standardized mean differences;
- association with treatment;
- association with outcome;
- selected pairwise relationships.

All plots use **Seaborn**.

## The most important rule

A variable associated with both treatment and outcome is **not automatically a confounder**.

The observed pattern

```text
X is associated with treatment
X is associated with outcome
```

can arise from several different causal structures.

For example:

```text
X → treatment
X → outcome
```

is one possibility, but so is:

```text
treatment → X → outcome
```

or:

```text
treatment → X ← outcome
```

The correlations alone cannot tell us which graph is correct.

## Why timing matters

Notebook 01 explicitly distinguishes variables known **before treatment** from variables measured **after treatment**.

This is causal knowledge from the study design, not something estimated from the correlation matrix.

A post-treatment variable should not be treated as an ordinary baseline confounder simply because it is strongly associated with treatment and outcome.

## The DAG worksheet

Notebook 01 creates:

```text
data/dag_worksheet.csv
```

The worksheet contains statistical evidence and known timing, plus blank fields for:

- proposed causal role;
- proposed edges;
- domain justification.

For every proposed edge, try to complete the sentence:

> **I believe A causes B because ...**

“Because A and B are correlated” is not enough.

## Transition to notebook 02

Notebook 01 answers:

> **What patterns are visible?**

Notebook 02 asks:

> **What causal structure could explain those patterns, and what does it imply about the effect of treatment on outcome?**

---

# 02 — Causal Inference

Open:

```text
02_causal_inference.ipynb
```

## Goal

Estimate the causal effect of backdoor defense on detection success.

The workflow is:

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

## Step 1: Build the DAG

The interactive graph starts with:

```text
treatment → outcome
```

This arrow represents the causal effect we want to study.

Use the worksheet, temporal ordering, and plausible mechanisms to decide what other edges belong in the graph.

The node colors represent structural roles. The default graph palette is Seaborn's **`colorblind`** categorical palette so different roles are easy to distinguish.

## Step 2: Identification

DoWhy asks:

> **If this DAG is correct, can the effect of treatment on outcome be expressed using the observed data?**

Identification determines **what** should be estimated.

## Step 3: Estimation

The tutorial uses inverse propensity-score weighting to estimate the ATE.

An estimated ATE should always be interpreted in the original domain:

> **How many percentage points does the backdoor defense change detection success, on average, relative to random filtering?**

## Step 4: Refutation

The tutorial runs selected robustness checks, including:

- placebo treatment;
- random common cause.

These checks can reveal fragile estimates, but passing them does **not** prove that the DAG is correct or that all unmeasured confounding is absent.

## Step 5: Reveal the synthetic truth

Only after you freeze your DAG and estimate the effect does the notebook reveal:

- the DAG used to generate the synthetic study;
- the known synthetic ATE;
- missing and extra edges in your proposed graph.

This is where the main lesson becomes concrete.

---

# The three levels of reasoning

The tutorial deliberately separates three kinds of statements.

## 1. Measurement

```text
code_complexity = 4
```

This records what was observed.

## 2. Association

```text
code_complexity is associated with treatment and outcome
```

This describes a pattern in the observed data.

## 3. Causal claim

```text
code_complexity → treatment
code_complexity → outcome
```

This is an assumption about how the data were generated.

The third statement does **not** follow automatically from the second.

That distinction is the core of the tutorial.

---

# Recommended student workflow

1. Run `00_data_preparation.ipynb` from top to bottom.
2. Do not inspect the hidden synthetic DAG or generator.
3. Run `01_correlational_analysis.ipynb`.
4. Study the plots and fill in the DAG worksheet.
5. Run `02_causal_inference.ipynb`.
6. Build and freeze your proposed DAG.
7. Identify and estimate the ATE.
8. Run the refutation checks.
9. Reveal the synthetic DAG and true ATE.
10. Compare what correlation suggested with what the causal data-generating process actually was.

A good final question to ask yourself is:

> **Which mistakes would I have made if I had selected adjustment variables using correlation alone?**

If you can answer that clearly, you have understood the central lesson of the tutorial.
