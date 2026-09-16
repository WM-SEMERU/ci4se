"""
Small validation and loading helpers for 02_causal_inference_tutorial.ipynb.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

import numpy as np
import pandas as pd
from packaging.version import Version


def check_dowhy_version(min_version: str = "0.14") -> str:
    """Confirm that a compatible DoWhy installation is available."""
    try:
        installed = version("dowhy")
    except PackageNotFoundError as exc:
        raise RuntimeError(
            f'DoWhy is not installed. Install dependencies with '
            f'`pip install -r requirements.txt`.'
        ) from exc

    if Version(installed) < Version(min_version):
        raise RuntimeError(
            f"This tutorial requires DoWhy >= {min_version}; found {installed}."
        )

    return installed


def load_analysis_data(params):
    """
    Load the causal dataset and remove covariates with no empirical variation.

    Zero-variance variables cannot help identify statistical relationships and
    can make diagnostics harder to interpret, so they are reported separately.
    """
    causal_df = pd.read_csv(params["causal_dataset"])

    treatment = params["treatment_column"]
    outcome = params["outcome_column"]
    requested_covariates = list(params["covariate_columns"])

    required = [treatment, outcome, *requested_covariates]
    missing = sorted(set(required) - set(causal_df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if causal_df[required].isna().any().any():
        counts = causal_df[required].isna().sum()
        counts = counts[counts > 0]
        raise ValueError(f"Missing analysis values detected:\n{counts}")

    numeric = causal_df[required].apply(pd.to_numeric, errors="coerce")
    if numeric.isna().any().any():
        bad = numeric.columns[numeric.isna().any()].tolist()
        raise ValueError(f"Non-numeric analysis columns: {bad}")

    if not np.isfinite(numeric.to_numpy()).all():
        raise ValueError("Infinite values detected in analysis columns.")

    treatment_values = set(causal_df[treatment].unique())
    if not treatment_values.issubset({0, 1}) or len(treatment_values) < 2:
        raise ValueError(
            "This tutorial uses a binary treatment and requires both 0 and 1; "
            f"found {sorted(treatment_values)}."
        )

    outcome_values = set(causal_df[outcome].unique())
    if not outcome_values.issubset({0, 1}):
        raise ValueError(
            "This tutorial uses a binary outcome; "
            f"found {sorted(outcome_values)}."
        )

    excluded_covariates = [
        c for c in requested_covariates
        if causal_df[c].nunique(dropna=True) <= 1
    ]
    covariates = [
        c for c in requested_covariates
        if c not in excluded_covariates
    ]

    if not covariates:
        raise ValueError("No varying covariates remain for the causal analysis.")

    analysis_df = causal_df[[treatment, outcome, *covariates]].copy()

    return (
        analysis_df,
        treatment,
        outcome,
        covariates,
        excluded_covariates,
    )
