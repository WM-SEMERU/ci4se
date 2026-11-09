"""
Data preparation for the backdoor-defense causal inference tutorial.

The raw code/docstring corpus supplies heterogeneous software examples. The
backdoor-defense treatment, detection outcome, and a few contextual variables
are synthetic.

The student-facing causal question is:

    To what extent does treatment cause a change in outcome?

where treatment=1 means that the backdoor defense is applied, treatment=0 is
the baseline random-filtering condition, and outcome=1 means successful
backdoor detection.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import io
import keyword
import re
import tokenize

import lizard
import numpy as np
import pandas as pd


DEFAULT_COVARIATES = [
    "code_number_tokens",
    "code_complexity",
    "code_num_identifiers",
    "code_num_strings",
    "reviewer_experience",
    "rollout_eligibility",
    "noise_feature",
    "inspection_intensity",
    "manual_review_flag",
]


def load_source_data(
    path: str | Path,
    required_columns=(
        "input_code",
        "output_docstring",
        "reviewer_experience",
        "rollout_eligibility",
        "noise_feature",
    ),
) -> pd.DataFrame:
    """Load the raw corpus and validate the columns used by the tutorial."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input dataset not found: {path}")

    df = pd.read_csv(path).reset_index(drop=True)
    if df.empty:
        raise ValueError("The input dataset is empty.")

    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required source columns: {missing}")

    return df


def _complexity_from_lizard(source: str, cache_dir: Path, cache: dict) -> int:
    """Compute cyclomatic complexity and cache the result by source hash."""
    digest = hashlib.sha1(source.encode("utf-8")).hexdigest()[:16]
    if digest in cache:
        return cache[digest]

    cache_dir.mkdir(parents=True, exist_ok=True)
    snippet_path = cache_dir / f"snippet_{digest}.py"
    if not snippet_path.exists():
        snippet_path.write_text(source, encoding="utf-8")

    try:
        analysis = lizard.analyze_file(str(snippet_path))
        functions = getattr(analysis, "function_list", None) or []
        if functions:
            complexity = sum(
                int(getattr(function, "cyclomatic_complexity", 0) or 0)
                for function in functions
            )
            complexity = max(1, complexity)
        else:
            average = getattr(analysis, "average_cyclomatic_complexity", None)
            complexity = (
                max(1, int(round(float(average))))
                if average is not None
                else 1
            )
    except Exception:
        complexity = 1

    cache[digest] = complexity
    return complexity


def _lexical_code_features(source: str) -> dict:
    """Extract a few readable code features used in the tutorial."""
    meaningful_tokens = 0
    identifiers = set()
    strings = 0

    ignored = {
        tokenize.ENCODING,
        tokenize.ENDMARKER,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.NEWLINE,
        tokenize.NL,
        tokenize.COMMENT,
    }

    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for token_info in tokens:
            token_type = token_info.type
            token_text = token_info.string

            if token_type not in ignored:
                meaningful_tokens += 1

            if token_type == tokenize.NAME and not keyword.iskeyword(token_text):
                identifiers.add(token_text)
            elif token_type == tokenize.STRING:
                strings += 1

    except (tokenize.TokenError, IndentationError, SyntaxError):
        meaningful_tokens = len(source.split())
        identifiers = set(re.findall(r"\b[A-Za-z_]\w*\b", source))
        strings = len(
            re.findall(
                r"(?s)(?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')",
                source,
            )
        )

    return {
        "code_number_tokens": meaningful_tokens,
        "code_num_identifiers": len(identifiers),
        "code_num_strings": strings,
    }


def engineer_features(
    source_df: pd.DataFrame,
    cache_dir: str | Path = "./cache/lizard",
) -> pd.DataFrame:
    """Create baseline code features while preserving the raw corpus."""
    df = source_df.copy().reset_index(drop=True)
    cache_dir = Path(cache_dir)
    complexity_cache = {}

    code_rows = []
    for code in df["input_code"]:
        source = "" if pd.isna(code) else str(code)
        features = _lexical_code_features(source)
        features["code_complexity"] = _complexity_from_lizard(
            source,
            cache_dir,
            complexity_cache,
        )
        code_rows.append(features)

    engineered = pd.DataFrame(code_rows, index=df.index)
    return pd.concat([df, engineered], axis=1)


def _standardize(frame: pd.DataFrame) -> pd.DataFrame:
    numeric = frame.astype(float)
    scale = numeric.std(ddof=0).replace(0, 1.0)
    return (numeric - numeric.mean()) / scale


def _sigmoid(values):
    return 1.0 / (1.0 + np.exp(-np.clip(values, -30, 30)))


# Coefficients of the synthetic data-generating process. Signs follow the plain-language
# reasons in data/synthetic_ground_truth_edges.csv; magnitudes were retuned so that the
# naive treated-vs-control comparison is visibly confounded.
ORIGINAL_GENERATOR_COEFFICIENTS = {
    "treatment_intercept": -0.45,
    "treatment_code_complexity": 0.50,
    "treatment_code_number_tokens": 0.35,
    "treatment_reviewer_experience": 0.35,
    "treatment_rollout_eligibility": 1.00,
    "inspection_noise_sd": 0.80,
    "inspection_treatment": 0.90,
    "outcome_intercept": -0.80,
    "outcome_treatment": 0.45,
    "outcome_inspection_intensity": 0.65,
    "outcome_code_complexity": -0.35,
    "outcome_code_number_tokens": -0.15,
    "outcome_reviewer_experience": 0.35,
    "outcome_code_num_strings": 0.45,
    "review_intercept": -1.10,
    "review_treatment": 0.90,
    "review_outcome": 1.00,
    "review_noise_sd": 0.25,
}

# Retuned 2026-11 (candidate "D"): reviewer_experience is a strong confounder that inflates the naive
# comparison, code complexity / tokens are confounders that push the other way (omitting either part of the
# adjustment set visibly biases the estimate), most of the effect runs through the mediator, and the collider
# is strong enough that adjusting for post-treatment variables collapses the estimate.
GENERATOR_COEFFICIENTS = {
    **ORIGINAL_GENERATOR_COEFFICIENTS,
    "treatment_code_complexity": 0.35,
    "treatment_code_number_tokens": 0.25,
    "treatment_reviewer_experience": 1.00,
    "inspection_treatment": 1.30,
    "outcome_treatment": 0.10,
    "outcome_inspection_intensity": 0.90,
    "outcome_code_complexity": -0.65,
    "outcome_code_number_tokens": -0.30,
    "outcome_reviewer_experience": 1.00,
    "review_treatment": 1.50,
    "review_outcome": 1.80,
}


@dataclass(frozen=True)
class SyntheticStudyInfo:
    """Summary of one synthetic draw, including the true potential-outcome probabilities.

    Attributes:
        seed: Random seed used for the draw.
        treatment_prevalence: Share of units with treatment=1.
        outcome_prevalence: Share of units with outcome=1.
        propensity: True (clipped) treatment probability per unit.
        p_y0: True detection probability per unit under control (mediator at its control value).
        p_y1: True detection probability per unit under the defense (mediator at its treated value).
        clipped_share: Share of units whose true propensity hit the [0.05, 0.95] bounds.
    """

    seed: int
    treatment_prevalence: float
    outcome_prevalence: float
    propensity: np.ndarray | None = None
    p_y0: np.ndarray | None = None
    p_y1: np.ndarray | None = None
    clipped_share: float = 0.0

    @property
    def true_ate(self) -> float:
        """Average treatment effect E[p_y1 - p_y0] over all units."""
        return float(np.mean(self.p_y1 - self.p_y0))


def make_synthetic_observational_data(
    feature_df: pd.DataFrame,
    seed: int = 42,
    coefficients: dict | None = None,
) -> tuple[pd.DataFrame, SyntheticStudyInfo]:
    """
    Create one observed treatment and one observed detection outcome per unit.

    treatment=0: baseline random filtering
    treatment=1: backdoor defense applied
    outcome=0: backdoor detection failed
    outcome=1: backdoor detection succeeded

    The data-generating process intentionally contains different causal roles
    so that correlation alone is not sufficient to construct the correct DAG.

    Args:
        feature_df: Engineered features (code features plus synthetic context columns).
        seed: Seed for the numpy Generator; the draw order is fixed.
        coefficients: Optional overrides of GENERATOR_COEFFICIENTS (used for tuning).

    Returns:
        The unit-level causal table and a SyntheticStudyInfo with the true potential outcomes.
    """
    coef = {**GENERATOR_COEFFICIENTS, **(coefficients or {})}
    required = [
        "code_number_tokens",
        "code_complexity",
        "code_num_identifiers",
        "code_num_strings",
        "reviewer_experience",
        "rollout_eligibility",
        "noise_feature",
    ]
    missing = sorted(set(required) - set(feature_df.columns))
    if missing:
        raise ValueError(f"Missing features required by the generator: {missing}")

    rng = np.random.default_rng(seed)

    continuous = [
        "code_number_tokens",
        "code_complexity",
        "code_num_identifiers",
        "code_num_strings",
        "reviewer_experience",
    ]
    z = _standardize(feature_df[continuous])
    rollout = feature_df["rollout_eligibility"].astype(int).to_numpy()

    # Treatment assignment is observational rather than randomized. Baseline
    # characteristics affect whether the dedicated defense is applied.
    treatment_logit = (
        coef["treatment_intercept"]
        + coef["treatment_code_complexity"] * z["code_complexity"]
        + coef["treatment_code_number_tokens"] * z["code_number_tokens"]
        + coef["treatment_reviewer_experience"] * z["reviewer_experience"]
        + coef["treatment_rollout_eligibility"] * rollout
    )
    raw_propensity = _sigmoid(treatment_logit)
    propensity = np.clip(raw_propensity, 0.05, 0.95)
    clipped_share = float(np.mean((raw_propensity <= 0.05) | (raw_propensity >= 0.95)))
    treatment = rng.binomial(1, propensity).astype(int)

    # Post-treatment mediator: applying the defense causes deeper inspection.
    inspection_noise = rng.normal(0.0, coef["inspection_noise_sd"], size=len(feature_df))
    inspection_under_control = inspection_noise
    inspection_under_defense = inspection_noise + coef["inspection_treatment"]
    inspection_observed = np.where(
        treatment == 1,
        inspection_under_defense,
        inspection_under_control,
    )

    def detection_probability(treatment_value, inspection_value):
        detection_logit = (
            coef["outcome_intercept"]
            + coef["outcome_treatment"] * treatment_value
            + coef["outcome_inspection_intensity"] * inspection_value
            + coef["outcome_code_complexity"] * z["code_complexity"]
            + coef["outcome_code_number_tokens"] * z["code_number_tokens"]
            + coef["outcome_reviewer_experience"] * z["reviewer_experience"]
            + coef["outcome_code_num_strings"] * z["code_num_strings"]
        )
        return _sigmoid(detection_logit)

    p_y0 = np.asarray(detection_probability(0, inspection_under_control), dtype=float)
    p_y1 = np.asarray(detection_probability(1, inspection_under_defense), dtype=float)

    observed_probability = np.where(treatment == 1, p_y1, p_y0)
    outcome = rng.binomial(1, observed_probability).astype(int)

    # Post-outcome collider: both use of the defense and successful detection
    # make manual review more likely.
    manual_review_logit = (
        coef["review_intercept"]
        + coef["review_treatment"] * treatment
        + coef["review_outcome"] * outcome
        + rng.normal(0.0, coef["review_noise_sd"], size=len(feature_df))
    )
    manual_review_flag = rng.binomial(
        1,
        _sigmoid(manual_review_logit),
    ).astype(int)

    causal_df = pd.DataFrame(
        {
            "unit_id": np.arange(len(feature_df), dtype=int),
            "treatment": treatment,
            "outcome": outcome,
            "code_number_tokens": feature_df["code_number_tokens"].to_numpy(),
            "code_complexity": feature_df["code_complexity"].to_numpy(),
            "code_num_identifiers": feature_df["code_num_identifiers"].to_numpy(),
            "code_num_strings": feature_df["code_num_strings"].to_numpy(),
            "reviewer_experience": feature_df["reviewer_experience"].to_numpy(),
            "rollout_eligibility": rollout,
            "noise_feature": feature_df["noise_feature"].to_numpy(),
            "inspection_intensity": inspection_observed,
            "manual_review_flag": manual_review_flag,
        }
    )

    info = SyntheticStudyInfo(
        seed=seed,
        treatment_prevalence=float(causal_df["treatment"].mean()),
        outcome_prevalence=float(causal_df["outcome"].mean()),
        propensity=np.asarray(propensity, dtype=float),
        p_y0=p_y0,
        p_y1=p_y1,
        clipped_share=clipped_share,
    )
    return causal_df, info


def validate_causal_dataset(
    causal_df: pd.DataFrame,
    covariates=DEFAULT_COVARIATES,
    treatment: str = "treatment",
    outcome: str = "outcome",
    unit_id: str = "unit_id",
) -> pd.DataFrame:
    """Validate the unit-level table used by notebooks 01 and 02."""
    covariates = list(covariates)
    required = [unit_id, treatment, outcome, *covariates]

    missing = sorted(set(required) - set(causal_df.columns))
    if missing:
        raise ValueError(f"Missing required causal-analysis columns: {missing}")

    if causal_df[unit_id].duplicated().any():
        raise ValueError("Each unit must appear exactly once.")

    if causal_df[required].isna().any().any():
        raise ValueError("Missing values detected in analysis columns.")

    if set(causal_df[treatment].unique()) != {0, 1}:
        raise ValueError("Treatment must contain both 0 and 1.")

    if not set(causal_df[outcome].unique()).issubset({0, 1}):
        raise ValueError("Outcome must be binary.")

    numeric = causal_df[covariates].apply(pd.to_numeric, errors="coerce")
    if numeric.isna().any().any():
        bad = numeric.columns[numeric.isna().any()].tolist()
        raise ValueError(f"Non-numeric covariates: {bad}")

    if not np.isfinite(numeric.to_numpy()).all():
        raise ValueError("Infinite values detected in covariates.")

    return pd.DataFrame(
        {
            "check": [
                "rows",
                "unique units",
                "random filtering (treatment=0)",
                "backdoor defense (treatment=1)",
                "detection success rate",
                "varying covariates",
            ],
            "value": [
                len(causal_df),
                causal_df[unit_id].nunique(),
                int((causal_df[treatment] == 0).sum()),
                int((causal_df[treatment] == 1).sum()),
                float(causal_df[outcome].mean()),
                int(
                    sum(
                        causal_df[c].nunique(dropna=True) > 1
                        for c in covariates
                    )
                ),
            ],
        }
    )


def save_causal_dataset(causal_df: pd.DataFrame, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    causal_df.to_csv(path, index=False)
    return path
