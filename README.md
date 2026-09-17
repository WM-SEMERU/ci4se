# Causal Inference Tutorial

Estimate the causal effect of a backdoor defense on backdoor detection.

The causal question:

> **To what extent does applying the backdoor defense, instead of baseline random filtering, change the probability of successful backdoor detection?**

The tutorial assumes no background in causal inference. Each notebook introduces the concepts it needs, and the glossary below collects them in one place.

---

## Setup

Create and activate a Python environment:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS and Linux
.venv\Scripts\Activate.ps1       # Windows PowerShell
```

Install the packages and start Jupyter:

```bash
pip install -r requirements.txt
jupyter lab
```

Then open `00_data_preparation.ipynb` and work through the notebooks in order.

---

## The three notebooks

Run them in order. Each one produces a file the next one needs.

| Notebook | Question it answers | Produces |
|---|---|---|
| `00_data_preparation.ipynb` | What did we observe for each unit? | `data/causal_data.csv` |
| `01_correlational_analysis.ipynb` | What patterns appear in the data? | `data/dag_worksheet.csv` |
| `02_causal_inference.ipynb` | What is the causal effect? | your DAG and the estimated ATE |

A program generates the treatment assignment and the detection outcome, so the numbers serve as a teaching exercise rather than as results about any real defense.

---

## Key terms

**Unit.** One thing you observe and could apply the treatment to. Here, one code example.

**Treatment.** The action whose effect you want to measure. The word comes from medicine, but it covers any intervention. Here it is the backdoor defense.

**Outcome.** The result you measure afterwards. Here, whether the pipeline detected the backdoor.

**Covariate.** Any other variable you record about a unit, such as code complexity.

**Association**, also called correlation. Two variables move together. You can compute this from data.

**Causation.** Changing one variable makes the other change. You cannot compute this from data alone, because it rests on assumptions.

**Confounder.** A variable that causes both the treatment and the outcome. It creates association that is not a causal effect, and it is the main reason raw comparisons mislead you.

**Mediator.** A variable on the path `treatment → X → outcome`. It carries part of the effect, so adjusting for it hides what you want to measure.

**Collider.** A variable that both the treatment and the outcome cause, as in `treatment → X ← outcome`. Adjusting for it creates bias where none existed.

**Counterfactual.** What would have happened to a unit under the other condition. You never observe it, and that absence is the central difficulty of the field.

**DAG**, short for directed acyclic graph. A diagram of your causal assumptions. Each variable is a node, and an arrow `A → B` claims that A directly causes B.

**ATE**, short for average treatment effect. The average causal effect across all units.

---

## Where the variables come from

Each example moves through a pipeline, one stage at a time. The stage that produces a variable decides what causal role that variable can possibly have.

```text
  STAGE 1  the example arrives
           code_number_tokens, code_complexity,
           code_num_identifiers, code_num_strings,
           reviewer_experience, rollout_eligibility, noise_feature
                    |
                    v
  STAGE 2  a method is chosen                    treatment (0 or 1)
                    |
                    v
  STAGE 3  the chosen method runs                inspection_intensity
                    |
                    v
  STAGE 4  it reports a verdict                  outcome (0 or 1)
                    |
                    v
  STAGE 5  the case may go to a human            manual_review_flag
```

Stage 1 variables either come from the corpus or follow from parsing the code. The four `code_*` features come from `input_code`: a token count, cyclomatic complexity, the number of distinct identifiers, and the number of string literals. The `reviewer_experience` column scores the reviewer handling the example, from 0 to 12. The `rollout_eligibility` column marks whether policy has cleared an example for the new defense, which is a scheduling decision that policy makes before the pipeline processes anything. All of these exist before anyone chooses a method, so any of them could have influenced that choice.

Stages 3 and 5 produce variables that do not exist until after someone chooses a method. The `inspection_intensity` column measures work that the chosen method performed, so before stage 2 there is nothing to measure. The `manual_review_flag` column records an escalation that happens after the verdict, so both the method and the result are already known when anyone sets it.

This is why we describe those two as measured after treatment. It is not a convention. It follows from the order of the stages, and no correlation overrides it.

---

## Treatment and outcome

| `treatment` | Meaning |
|---:|---|
| `0` | baseline random filtering, the control condition |
| `1` | backdoor defense, the treated condition |

| `outcome` | Meaning |
|---:|---|
| `0` | detection failed |
| `1` | detection succeeded |

Since `outcome` only ever takes the value 0 or 1, its mean gives the fraction of successes, which we call the detection success rate. So `mean(outcome) = 0.70` means the pipeline detected 70 percent of the examples.

---

## What you are estimating

Each example has two potential outcomes:

- **Y(1)**, the detection result if the pipeline applies the backdoor defense;
- **Y(0)**, the detection result under baseline random filtering.

You only ever observe one of the two per example, which is exactly why causal inference exists.

The tutorial estimates the average treatment effect:

**ATE = E[Y(1) - Y(0)]**

An ATE of `0.10` means the defense raises successful detection by about 10 percentage points on average.

---

## The idea to keep straight

Three kinds of statement look similar and mean different things.

| Kind | Example | What it is |
|---|---|---|
| Measurement | `code_complexity = 4` | a value in the data |
| Association | `code_complexity` correlates with `treatment` | a pattern in the observed data |
| Causal claim | `code_complexity → treatment` | a claim that changing one changes the other |

An association never promotes itself to a causal claim. Before you draw any edge `A → B`, answer one question:

> **Why would A cause B?**

"They are correlated" does not answer it. Deciding which variables to adjust for is a reasoning problem, not a correlation ranking problem.

---

## Files

```text
bowen_class/
├── 00_data_preparation.ipynb
├── 01_correlational_analysis.ipynb
├── 02_causal_inference.ipynb
├── README.md
├── requirements.txt
│
├── data/
│   └── raw_code.csv          # source examples; notebook 00 generates causal_data.csv
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

The notebooks carry the tutorial. The `src/` folder holds the supporting Python code.
