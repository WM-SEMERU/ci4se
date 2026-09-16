# Causal Inference Tutorial

This tutorial introduces causal inference through a three-stage workflow:

```text
00 — Prepare the data
        ↓
01 — Explore correlations
        ↓
02 — Build a causal model
```

The main idea is simple:

> **Correlation can show us patterns in the data. Causal inference asks what would happen under an intervention.**

The notebooks are designed to be completed in order. Each notebook prepares the reasoning needed for the next one.

---

# What you will learn

By the end of the tutorial, you should be able to explain the difference between:

- an **observed association**;
- a **causal assumption**;
- a **causal graph**;
- an **identified estimand**;
- and an **estimated causal effect**.

You will also practice identifying variables that may play different roles in a causal graph, such as:

- common causes;
- mediators;
- colliders;
- treatment predictors;
- outcome predictors;
- instrument candidates;
- proxy variables;
- irrelevant variables.

The goal is **not** to memorize these labels.

The goal is to learn how to ask:

> **What causal mechanism would justify this arrow?**

---

# The tutorial question

The synthetic study asks:

> **Does enabling a documentation intervention improve the probability of a successful documentation outcome?**

The example begins with real code and docstring text. The tutorial then adds a controlled synthetic observational study so that the true data-generating process is known.

That lets us compare:

1. what we can observe from correlations;
2. what causal graph we would propose;
3. and what actually generated the synthetic data.

This comparison is one of the most important parts of the tutorial.

---

# Important: do not inspect the answer too early

The project contains:

```text
data/synthetic_ground_truth_edges.csv
```

This file contains the causal graph used to generate the synthetic study.

**Do not open it before the reveal section in notebook 02** if you want to complete the graph-construction exercise yourself.

The purpose of the exercise is to discover that correlation alone does not reliably reveal causal roles.

---

# Project structure

```text
causal_inference_tutorial_project/
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
└── src/
    ├── __init__.py
    ├── causal_data_prep.py
    ├── correlational_analysis_utils.py
    ├── causal_graph_ui.py
    └── causal_tutorial_utils.py
```

The notebooks are the learning material.

The `src/` directory contains implementation details so that the notebooks can stay focused on the causal concepts.

---

# Setup

From the project directory, create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

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

The causal-inference notebook uses **DoWhy 0.14**.

---

# 00 — Data Preparation

Open:

```text
00_data_preparation.ipynb
```

## Purpose

The first notebook answers:

> **What exactly is one observation in our study?**

Before doing any causal analysis, we need a valid unit-level dataset.

Each row should represent one observational unit with:

- one observed treatment;
- one observed outcome;
- measured variables describing that unit.

The notebook starts from code and docstring data and extracts useful numeric features.

It then creates a synthetic observational study for teaching purposes.

## Why synthetic treatment and outcome?

In a real observational study, the treatment and outcome would come from the real system being studied.

Here we generate them because this gives us a known causal data-generating process.

That means later we can ask:

> Did our causal analysis recover the effect that was actually built into the data?

## Output

Notebook 00 creates:

```text
data/causal_data.csv
```

This becomes the input to notebooks 01 and 02.

## What to think about

While working through notebook 00, ask:

- What is the observational unit?
- Which variables exist before treatment?
- Which variables could only exist after treatment?
- Which variables might plausibly influence treatment assignment?
- Which variables might plausibly influence the outcome?

Do not worry about drawing the graph yet.

Notebook 01 will first show what the observed data look like.

---

# Transition: from measurement to association

After notebook 00, we know:

> **what was observed for each unit.**

We do **not** yet know which variables should be adjusted for.

The next step is to inspect the data and ask:

> **Which variables move together?**

That is the role of notebook 01.

---

# 01 — Correlational Analysis

Open:

```text
01_correlational_analysis.ipynb
```

## Purpose

Notebook 01 explores relationships in the observed data.

It does **not** perform causal inference.

You will examine:

- the raw treatment–outcome difference;
- correlations among measured variables;
- differences between treated and untreated groups;
- standardized mean differences;
- variables associated with treatment;
- variables associated with outcome;
- pairwise relationships among selected variables.

All plots use **Seaborn**.

## The most important rule in this notebook

A variable that is associated with both treatment and outcome is **not automatically a confounder**.

For example, the pattern

```text
X is associated with treatment
X is associated with outcome
```

can occur under several different causal structures.

Possible explanations include:

```text
X → treatment
X → outcome
```

but also:

```text
treatment → X → outcome
```

or:

```text
treatment → X ← outcome
```

or other structures.

The observed correlation does not tell us which structure is correct.

---

# A useful way to read the plots

When you see a strong association, do not immediately ask:

> “Should I adjust for this variable?”

First ask:

> “What causal process could have produced this association?”

Useful questions include:

- Was the variable measured before treatment?
- Could treatment cause this variable?
- Could the outcome cause this variable?
- Could another variable cause both?
- Could this variable simply be a proxy for something else?
- Is there a plausible mechanism for a causal arrow?

---

# Standardized mean difference

Notebook 01 also compares covariates between treated and untreated units.

The standardized mean difference (SMD) describes how different the two groups are on a variable.

Roughly:

```text
SMD near 0
→ treated and control groups look similar

larger |SMD|
→ treated and control groups differ more
```

But remember:

> **Imbalance is evidence of a difference between groups, not proof of confounding.**

A post-treatment variable can also be highly imbalanced.

---

# The association map

One of the most useful plots in notebook 01 places:

```text
association with treatment
```

on one axis and:

```text
association with outcome
```

on the other.

This helps identify variables that deserve closer investigation.

However, two variables located in similar parts of the plot may have completely different causal roles.

That ambiguity is intentional.

---

# The DAG worksheet

At the end of notebook 01, you create:

```text
data/dag_worksheet.csv
```

The worksheet combines the statistical evidence with space for causal reasoning.

You will see columns such as:

```text
variable
association_with_treatment
association_with_outcome
standardized_mean_difference
```

and blank columns such as:

```text
proposed_role
proposed_edges
domain_justification
```

The blank columns are the important part.

Try to fill them using **causal reasoning**, not correlation ranking.

For every proposed arrow, try to complete this sentence:

> “I believe `A → B` because __________.”

“Because A and B are correlated” is not sufficient.

---

# Transition: from association to causation

Notebook 01 answers:

> **What patterns can we observe?**

Notebook 02 asks a fundamentally different question:

> **What causal assumptions are we willing to make?**

This is where the DAG enters the analysis.

---

# 02 — Causal Inference

Open:

```text
02_causal_inference.ipynb
```

## Purpose

Notebook 02 converts your causal assumptions into a formal causal model.

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

You will use **DoWhy** for the identification and estimation steps.

---

# Step 1 — Review the DAG worksheet

Notebook 02 first loads the worksheet created in notebook 01.

Use it as a reminder of:

- what the data showed;
- what questions remained unresolved;
- what causal mechanisms you think are plausible.

The worksheet is evidence for discussion.

It is not the graph.

---

# Step 2 — Build the causal graph

The interactive graph begins with:

```text
treatment → output
```

This represents the causal effect we want to study.

You then decide which other arrows should be added.

The graph editor can display structural roles such as:

- common cause;
- mediator;
- instrument candidate;
- outcome predictor;
- collider candidate.

These labels are calculated from the **graph you draw**.

They are not learned from the correlation matrix.

---

# Before adding an arrow

Ask three questions.

### 1. Time

Does the proposed cause occur before the proposed effect?

### 2. Mechanism

Can you describe a plausible process by which the cause changes the effect?

### 3. Alternatives

Could the observed association instead be explained by:

- reverse causation?
- a common cause?
- mediation?
- a collider?
- a proxy variable?

If you cannot explain an arrow without referring only to correlation, reconsider it.

---

# Step 3 — Identification

After freezing the DAG, DoWhy performs **identification**.

Identification asks:

> **If this graph is correct, what observable quantity corresponds to the causal effect we want?**

This is different from estimation.

Identification determines the causal estimand.

Estimation computes a number from the observed data.

---

# Step 4 — Estimation

The tutorial estimates the:

```text
Average Treatment Effect (ATE)
```

using inverse propensity-score weighting.

Conceptually, the ATE asks:

> On average, how would the outcome change if the same population were treated instead of untreated?

For a binary outcome, an estimated ATE of:

```text
0.10
```

means an estimated:

```text
10 percentage-point increase
```

in outcome probability.

---

# Step 5 — Refutation

The notebook also runs causal refuters.

These are robustness checks.

Examples include:

### Placebo treatment

Treatment is randomly permuted.

The estimated placebo effect should usually be close to zero.

### Random common cause

An irrelevant random variable is added.

A stable estimate should not change substantially.

Passing these tests is useful, but:

> **Refutation does not prove that the DAG is correct.**

Important unmeasured confounding can still exist.

---

# The reveal

After you have:

1. built your DAG;
2. frozen it;
3. identified the effect;
4. estimated the ATE;

notebook 02 reveals the synthetic data-generating graph.

You can then compare:

```text
your proposed edges
```

with:

```text
the edges that actually generated the synthetic data
```

This is where many of the most interesting lessons appear.

Ask:

- Which variables did correlation make easy to understand?
- Which variables were misleading?
- Did any post-treatment variable look like a confounder?
- Did an irrelevant variable appear important by chance?
- Did a proxy tempt you to add an unnecessary causal arrow?
- Did you miss a real common cause because its marginal correlation was small?

---

# The key lesson

The tutorial intentionally separates three statements.

## Measurement

```text
X = 4
```

This describes an observation.

## Association

```text
X is associated with treatment and outcome.
```

This describes a pattern in the observed data.

## Causal claim

```text
X → treatment
X → outcome
```

This describes an assumption about how the world works.

These are not interchangeable.

A causal analysis becomes possible only after the causal assumptions are made explicit.

---

# A useful mental model

Think of the three notebooks as answering three questions.

| Notebook | Question |
|---|---|
| 00 | **What did we observe?** |
| 01 | **What patterns do we see?** |
| 02 | **What causal structure could explain those patterns?** |

Then DoWhy asks:

> **Given that causal structure, what effect can we identify and estimate?**

---

# Configuration

Each notebook contains a `default_params()` function near the top.

You normally should not need to edit the source files in `src/`.

For example:

```python
def default_params():
    return {
        ...
    }
```

The current bundle uses project-relative paths such as:

```python
"causal_dataset": "data/causal_data.csv"
```

so the notebooks should work when Jupyter is launched from the project directory.

Plot settings can also be changed from `default_params()`.

For example:

```python
"plot_palette": "mako",
"heatmap_palette": "vlag",
```

The causal graph also exposes palette and edge-opacity settings.

---

# Suggested workflow for students

### First

Run notebook 00 from top to bottom.

Do not inspect the hidden DAG.

### Second

Run notebook 01.

Study the plots carefully.

Fill in the DAG worksheet.

### Third

Run notebook 02.

Build your causal graph from your reasoning.

Freeze the graph.

Run identification and estimation.

### Finally

Reveal the synthetic DAG.

Compare your assumptions with the actual data-generating process.

Then ask:

> **Which mistakes would I have made if I had chosen adjustment variables using correlation alone?**

If you can answer that question clearly, you have understood the central lesson of the tutorial.

---

# Final reminder

A statistical model can estimate an effect.

A causal model explains **what that effect means**.

And that meaning depends on the assumptions encoded in the graph.
