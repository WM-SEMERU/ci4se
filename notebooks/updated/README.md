# Causal inference tutorial

A three-notebook tutorial built around one question:

> **How do we move from observed association to a defensible causal effect?**

The example uses real code/docstring text plus a controlled synthetic observational study. The synthetic part gives the tutorial a known causal ground truth, including variables with deliberately different roles.

## Run in this order

```text
00_data_preparation_tutorial.ipynb
        │
        │ creates data/causal_data.csv
        ▼
01_correlational_analysis.ipynb
        │
        │ creates data/dag_worksheet.csv
        ▼
02_causal_inference_tutorial.ipynb
        │
        │ build DAG → identify → estimate → refute
        ▼
reveal and compare with synthetic ground truth
```

## Why this version is a better teaching example

The raw code/docstring strings are unchanged.

The bundled raw CSV adds three clearly synthetic baseline/context variables:

- `developer_experience`
- `rollout_eligibility`
- `noise_feature`

Notebook 00 then generates a study containing several distinct causal roles:

| Variable | Hidden teaching role |
|---|---|
| `code_number_tokens` | confounder |
| `code_complexity` | confounder |
| `developer_experience` | confounder |
| `rollout_eligibility` | instrument candidate |
| `code_num_strings` | outcome predictor |
| `docstring_detail_score` | mediator |
| `review_flag` | collider |
| `code_num_identifiers` | correlated/proxy-like measurement |
| `noise_feature` | irrelevant variable |

**Do not use this table while attempting notebook 01 or the first part of notebook 02** if you want the intended exercise. Notebook 02 reveals the actual edge list after you freeze your proposed DAG.

The purpose is to show that variables with similar correlations can have very different causal roles.

## Project structure

```text
causal_inference_tutorial_project/
│
├── 00_data_preparation_tutorial.ipynb
├── 01_correlational_analysis.ipynb
├── 02_causal_inference_tutorial.ipynb
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw_code_docstrings_enriched.csv
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

`causal_data.csv` and `dag_worksheet.csv` are generated when you run notebooks 00 and 01.

## Install

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

The notebooks use project-relative paths, so no path edits are required if Jupyter is started from the project directory.

---

# 00 — Data preparation

Notebook 00 answers:

> **What variables are observed for each unit?**

It extracts baseline code measurements and creates one observed treatment and one observed outcome per unit.

The synthetic treatment assignment depends on baseline variables, creating confounding.

The generator also creates:

- a post-treatment mediator (`docstring_detail_score`);
- a collider (`review_flag`);
- an instrument-like baseline variable (`rollout_eligibility`);
- an irrelevant variable (`noise_feature`).

The exact generating DAG is written to `data/synthetic_ground_truth_edges.csv`, but the tutorial saves its reveal for notebook 02.

Output:

```text
data/causal_data.csv
```

---

# 01 — Correlational analysis

Notebook 01 answers:

> **What patterns are visible if we only look at the observed data?**

It uses Seaborn to show:

- raw outcome differences by treatment;
- a signed correlation heatmap;
- standardized mean differences;
- an association map with treatment on one axis and outcome on the other;
- focused pairplots.

It then creates:

```text
data/dag_worksheet.csv
```

The worksheet contains descriptive evidence and blank fields for causal reasoning.

The key rule is:

> **Association determines which questions to ask, not which arrows to draw.**

A variable associated with treatment and outcome might be a confounder—but it might also be a mediator, collider, proxy, or something else.

---

# 02 — Causal inference

Notebook 02 answers:

> **What causal assumptions are we willing to make, and what effect follows from them?**

It loads the DAG worksheet and opens the interactive graph editor.

The graph starts from:

```text
treatment → output
```

You add edges using:

- temporal order;
- domain knowledge;
- plausible mechanisms;
- the statistical clues from notebook 01.

After freezing the graph, DoWhy 0.14 is used to:

1. identify the estimand;
2. estimate the Average Treatment Effect with inverse propensity weighting;
3. run placebo-treatment and random-common-cause refuters.

Only after this exercise does the notebook reveal the synthetic ground-truth DAG and compare its edges with your proposed graph.

---

# The main lesson

These three statements are different:

### Measurement

```text
code_complexity = 4
```

### Association

```text
code_complexity is associated with treatment and outcome
```

### Causal assumption

```text
code_complexity → treatment
code_complexity → output
```

Notebook 00 creates measurements.

Notebook 01 measures associations.

Notebook 02 requires causal assumptions.

DoWhy can identify and estimate an effect **conditional on those assumptions**. It cannot infer the scientifically correct DAG from correlation alone.

## `default_params()`

Every notebook keeps `default_params()` near the top.

The defaults use relative paths:

```python
"causal_dataset": "data/causal_data.csv"
"dag_worksheet_output": "data/dag_worksheet.csv"
"dag_worksheet_path": "data/dag_worksheet.csv"
```

Plot and graph styling are also configurable:

```python
"plot_palette": "mako"
"heatmap_palette": "vlag"
"graph_palette": "mako"
"graph_edge_opacity": 0.35
```

## Suggested classroom exercise

1. Run notebook 00.
2. Do not inspect the ground-truth edge CSV.
3. Run notebook 01 and fill in the DAG worksheet.
4. In notebook 02, build your DAG.
5. Freeze it.
6. Estimate the causal effect.
7. Reveal the synthetic DAG.
8. Discuss why some statistical clues were useful and others were misleading.

That final comparison is the reason the synthetic causal roles were designed explicitly.
