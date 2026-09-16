"""
Statistical helpers for 01_correlational_analysis.ipynb.

The functions in this module summarize the observed data. They deliberately
do not infer causal direction or causal roles from correlation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


@dataclass(frozen=True)
class AnalysisColumns:
    treatment: str
    outcome: str
    covariates: list[str]


def load_causal_dataset(params) -> tuple[pd.DataFrame, AnalysisColumns]:
    """Load the prepared dataset and validate the analysis columns."""
    path = Path(params["causal_dataset"])
    if not path.exists():
        raise FileNotFoundError(f"Causal dataset not found: {path}")

    df = pd.read_csv(path)

    treatment = params["treatment_column"]
    outcome = params["outcome_column"]
    covariates = list(params["covariate_columns"])

    required = [treatment, outcome, *covariates]
    if "unit_id" in df.columns:
        required = ["unit_id", *required]

    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    analysis_df = df[required].copy()

    if analysis_df.isna().any().any():
        counts = analysis_df.isna().sum()
        counts = counts[counts > 0]
        raise ValueError(f"Missing values detected:\n{counts}")

    if "unit_id" in analysis_df and analysis_df["unit_id"].duplicated().any():
        raise ValueError("Each unit_id must appear exactly once.")

    treatment_values = set(analysis_df[treatment].unique())
    if not treatment_values.issubset({0, 1}) or len(treatment_values) < 2:
        raise ValueError(
            f"{treatment!r} must contain both 0 and 1; "
            f"found {sorted(treatment_values)}"
        )

    outcome_values = set(analysis_df[outcome].unique())
    if not outcome_values.issubset({0, 1}):
        raise ValueError(
            f"{outcome!r} must be binary in this tutorial; "
            f"found {sorted(outcome_values)}"
        )

    numeric_cols = [treatment, outcome, *covariates]
    numeric = analysis_df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    if numeric.isna().any().any():
        bad = numeric.columns[numeric.isna().any()].tolist()
        raise ValueError(f"Non-numeric analysis columns: {bad}")

    if not np.isfinite(numeric.to_numpy()).all():
        raise ValueError("Infinite values detected in analysis columns.")

    return analysis_df, AnalysisColumns(
        treatment=treatment,
        outcome=outcome,
        covariates=covariates,
    )


def covariate_quality_table(
    df: pd.DataFrame,
    covariates: list[str],
) -> pd.DataFrame:
    """Report whether each covariate contains empirical variation."""
    rows = []
    for variable in covariates:
        series = pd.to_numeric(df[variable], errors="coerce")
        unique_values = int(series.nunique(dropna=True))
        rows.append(
            {
                "variable": variable,
                "unique_values": unique_values,
                "mean": float(series.mean()),
                "std": float(series.std(ddof=1)) if len(series) > 1 else np.nan,
                "has_variation": unique_values > 1,
            }
        )

    return pd.DataFrame(rows)


def correlation_matrix(
    df: pd.DataFrame,
    columns: list[str],
    method: str = "spearman",
) -> pd.DataFrame:
    """Return a pairwise correlation matrix for variables with variation."""
    if method not in {"pearson", "spearman", "kendall"}:
        raise ValueError(
            "correlation_method must be 'pearson', 'spearman', or 'kendall'."
        )

    constant = [c for c in columns if df[c].nunique(dropna=True) <= 1]
    if constant:
        raise ValueError(
            "Correlation is undefined for constant variables. "
            f"Remove these columns first: {constant}"
        )

    return df[columns].corr(method=method)


def standardized_mean_difference(
    treated: pd.Series,
    control: pd.Series,
) -> float:
    """Compute a standardized treated-versus-control mean difference."""
    treated = pd.to_numeric(treated, errors="coerce").dropna()
    control = pd.to_numeric(control, errors="coerce").dropna()

    if len(treated) < 2 or len(control) < 2:
        return np.nan

    pooled_var = (treated.var(ddof=1) + control.var(ddof=1)) / 2.0

    if pooled_var <= 0 or not np.isfinite(pooled_var):
        return 0.0

    return float(
        (treated.mean() - control.mean()) / np.sqrt(pooled_var)
    )


def treatment_balance_table(
    df: pd.DataFrame,
    treatment: str,
    covariates: list[str],
) -> pd.DataFrame:
    """
    Summarize covariate differences between treatment groups.

    SMD describes imbalance. It does not establish that a variable is a
    confounder.
    """
    rows = []
    treated_mask = df[treatment] == 1
    control_mask = df[treatment] == 0

    for variable in covariates:
        treated = df.loc[treated_mask, variable]
        control = df.loc[control_mask, variable]
        varies = df[variable].nunique(dropna=True) > 1

        smd = standardized_mean_difference(treated, control)

        if varies:
            point_biserial = float(
                stats.pointbiserialr(
                    df[treatment],
                    df[variable],
                ).statistic
            )
        else:
            point_biserial = np.nan

        rows.append(
            {
                "variable": variable,
                "mean_treated": float(treated.mean()),
                "mean_control": float(control.mean()),
                "standardized_mean_difference": smd,
                "abs_smd": abs(smd) if np.isfinite(smd) else np.nan,
                "point_biserial_with_treatment": point_biserial,
                "has_variation": varies,
            }
        )

    return (
        pd.DataFrame(rows)
        .sort_values(
            ["has_variation", "abs_smd"],
            ascending=[False, False],
        )
        .reset_index(drop=True)
    )


def variable_association_table(
    df: pd.DataFrame,
    treatment: str,
    outcome: str,
    covariates: list[str],
    method: str = "spearman",
) -> pd.DataFrame:
    """
    Summarize marginal association with treatment and outcome.

    The screening_score is a descriptive prioritization heuristic only:
    |association with treatment| × |association with outcome|.
    """
    corr = correlation_matrix(
        df,
        [treatment, outcome, *covariates],
        method=method,
    )

    rows = []
    for variable in covariates:
        corr_t = float(corr.loc[variable, treatment])
        corr_y = float(corr.loc[variable, outcome])

        rows.append(
            {
                "variable": variable,
                "association_with_treatment": corr_t,
                "association_with_outcome": corr_y,
                "abs_association_with_treatment": abs(corr_t),
                "abs_association_with_outcome": abs(corr_y),
                "screening_score": abs(corr_t) * abs(corr_y),
            }
        )

    return (
        pd.DataFrame(rows)
        .sort_values(
            ["screening_score", "abs_association_with_outcome"],
            ascending=False,
        )
        .reset_index(drop=True)
    )


def outcome_by_treatment_table(
    df: pd.DataFrame,
    treatment: str,
    outcome: str,
) -> pd.DataFrame:
    """Describe the unadjusted treatment-outcome association."""
    return (
        df.groupby(treatment)[outcome]
        .agg(["count", "mean", "std"])
        .rename(
            columns={
                "count": "units",
                "mean": "outcome_mean",
                "std": "outcome_std",
            }
        )
        .reset_index()
    )


def build_dag_worksheet(
    association_table: pd.DataFrame,
    balance_table: pd.DataFrame,
    quality_table: pd.DataFrame,
    treatment: str,
    outcome: str,
) -> pd.DataFrame:
    """
    Build a worksheet that turns statistical patterns into causal questions.

    Constant variables remain visible in the worksheet, but are marked as
    empirically uninformative for association analysis.
    """
    base = quality_table[["variable", "unique_values", "has_variation"]].copy()

    merged = (
        base
        .merge(
            association_table[
                [
                    "variable",
                    "association_with_treatment",
                    "association_with_outcome",
                    "screening_score",
                ]
            ],
            on="variable",
            how="left",
        )
        .merge(
            balance_table[
                [
                    "variable",
                    "standardized_mean_difference",
                ]
            ],
            on="variable",
            how="left",
        )
    )

    def data_note(row):
        if not bool(row["has_variation"]):
            return (
                "No variation in this dataset; correlation and group "
                "association are not estimable."
            )
        return "Use these associations as prompts for causal reasoning."

    def question(row):
        variable = row["variable"]
        if not bool(row["has_variation"]):
            return (
                f"Does {variable} belong in this analysis if it does not vary "
                "across observed units?"
            )
        return (
            f"Could {variable} plausibly cause {treatment}, "
            f"{outcome}, both, or neither?"
        )

    merged["data_note"] = merged.apply(data_note, axis=1)
    merged["causal_question"] = merged.apply(question, axis=1)
    merged["proposed_role"] = ""
    merged["proposed_edges"] = ""
    merged["domain_justification"] = ""

    return merged[
        [
            "variable",
            "unique_values",
            "association_with_treatment",
            "association_with_outcome",
            "standardized_mean_difference",
            "screening_score",
            "data_note",
            "causal_question",
            "proposed_role",
            "proposed_edges",
            "domain_justification",
        ]
    ]
