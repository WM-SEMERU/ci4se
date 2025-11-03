# Causal Interpretability for Backdoor Defenses 
This folder contains two short, hands-on notebooks to build a causal dataset and estimate causal effects.

Order of execution:
1) `data_preparation_tutorial.ipynb` (first)
2) `causal_interpretability_tutorial.ipynb` (second)

## Example studied
Causal question: What is the causal effect of an implemented backdoor defense technique on Detection Success Rate (DSR)?

You will:
- Prepare a causal analysis table with features, treatment indicator (defense enabled), outcome (DSR), and covariates.
- Estimate causal effects (e.g., ATE/ATT) and interpret results.

## Environment setup
Requirements file: `requirements.txt` (at repo root)

- Create and activate a virtual environment (bash):
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
- If using VS Code, select the `.venv` Python interpreter as the notebook kernel.

## How to run
Open and run the notebooks in order. Adjust the first cell in each notebook if you want different paths.

- `notebooks/data_preparation_tutorial.ipynb`
  - Defaults (from the notebook parameters):
    - Input dataset: `data/test.csv`
    - Lizard cache: `/workspaces/ci4sesci/datax/lizard_cache` (change)
    - Produces: `data/causal_analysis/causal_data.csv`

- `notebooks/causal_interpretability_tutorial.ipynb`
  - Defaults (from the notebook parameters):
    - Consumes: `data/causal_analysis/causal_data.csv`
    - Produces (effects CSV): `data/causal_analysis/causal_effects.csv`
    - Produces (graph image): `notebooks/causal_model.png` (saved next to this notebook)

## Required customization for the assignment
Before running your final analysis, make these modifications:

- In `data_preparation_tutorial.ipynb`:
  - Add more measurable variables to the engineered feature set (e.g., additional code metrics, lexical/structural features, docstring/text metrics). Ensure new columns are persisted in the final `causal_data.csv`.
  - Add detection outcomes using your implemented defense technique, (modify cell#3 backdoor_defense_outcome with the detection results from your technique) Ensure values are persisted in the final `causal_data.csv`.

- In `causal_interpretability_tutorial.ipynb`:
  - Define or complement a different set of confounders by updating `params['confounder_columns']` to include your newly added variables. Make sure the names match the columns in `causal_data.csv`.

## Deliverables (Kaggle Challenge)
Submit the following for grading:
- From `data_preparation_tutorial`: `data/causal_analysis/causal_data.csv` (or the path you used; ensure the file is included)
- From `causal_interpretability_tutorial`: `data/causal_analysis/causal_effects.csv`
- The generated causal graph image: `causal_model.png` (include the image file produced by the notebook; if saved elsewhere, include that file and keep the name `causal_model.png`)

Notes:
- Paths above reflect notebook defaults at the time of writing. Adjust in the first cell of each notebook as needed and keep paths consistent across steps.
- Ensure the active kernel is the same environment where you installed the requirements.

