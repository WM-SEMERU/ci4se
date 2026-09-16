"""
Data preparation for the backdoor-defense causal inference tutorial.

The raw code/docstring corpus supplies heterogeneous software examples. The
backdoor-defense treatment, detection outcome, and a few contextual variables
are synthetic so that the tutorial has a known data-generating process.

The student-facing causal question is:

    To what extent does treatment cause a change in outcome?

where treatment=1 means that the backdoor defense is applied, treatment=0 is
the baseline random-filtering condition, and outcome=1 means successful
backdoor detection.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import hashlib
import io
import json
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


# Hidden teaching DAG. Students are asked not to inspect this until the reveal
# section of notebook 02.
GROUND_TRUTH_EDGES = [
    (
        "code_number_tokens",
        "treatment",
        "larger code examples are more likely to receive the defense",
    ),
    (
        "code_number_tokens",
        "outcome",
        "larger code examples can make backdoor detection harder",
    ),
    (
        "code_complexity",
        "treatment",
        "more complex code is more likely to receive the defense",
    ),
    (
        "code_complexity",
        "outcome",
        "greater complexity can make backdoor detection harder",
    ),
    (
        "reviewer_experience",
        "treatment",
        "reviewer experience influences whether the defense is used",
    ),
    (
        "reviewer_experience",
        "outcome",
        "reviewer experience can improve detection success",
    ),
    (
        "rollout_eligibility",
        "treatment",
        "eligibility for the defense rollout increases defense use",
    ),
    (
        "code_num_strings",
        "outcome",
        "string-heavy code changes how easy a backdoor is to detect",
    ),
    (
        "treatment",
        "inspection_intensity",
        "the defense causes a deeper inspection process",
    ),
    (
        "inspection_intensity",
        "outcome",
        "deeper inspection increases detection success",
    ),
    (
        "treatment",
        "outcome",
        "the defense also has a direct effect on detection success",
    ),
    (
        "treatment",
        "manual_review_flag",
        "defense use changes the probability of manual review",
    ),
    (
        "outcome",
        "manual_review_flag",
        "detected cases are more likely to be reviewed manually",
    ),
]


GROUND_TRUTH_ROLES = {
    "code_number_tokens": "confounder",
    "code_complexity": "confounder",
    "reviewer_experience": "confounder",
    "rollout_eligibility": "instrument_candidate",
    "code_num_strings": "outcome_predictor",
    "inspection_intensity": "mediator",
    "manual_review_flag": "collider",
    "code_num_identifiers": "proxy_or_correlated_measurement",
    "noise_feature": "irrelevant",
    "treatment": "treatment",
    "outcome": "outcome",
}


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


@dataclass(frozen=True)
class SyntheticStudyInfo:
    seed: int
    true_average_treatment_effect: float
    treatment_prevalence: float
    outcome_prevalence: float


def make_synthetic_observational_data(
    feature_df: pd.DataFrame,
    seed: int = 42,
) -> tuple[pd.DataFrame, SyntheticStudyInfo]:
    """
    Create one observed treatment and one observed detection outcome per unit.

    treatment=0: baseline random filtering
    treatment=1: backdoor defense applied
    outcome=0: backdoor detection failed
    outcome=1: backdoor detection succeeded

    The data-generating process intentionally contains different causal roles
    so that correlation alone is not sufficient to construct the correct DAG.
    """
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
        -0.45
        + 0.50 * z["code_complexity"]
        + 0.35 * z["code_number_tokens"]
        + 0.35 * z["reviewer_experience"]
        + 1.00 * rollout
    )
    propensity = np.clip(_sigmoid(treatment_logit), 0.05, 0.95)
    treatment = rng.binomial(1, propensity).astype(int)

    # Post-treatment mediator: applying the defense causes deeper inspection.
    inspection_noise = rng.normal(0.0, 0.80, size=len(feature_df))
    inspection_under_control = inspection_noise
    inspection_under_defense = inspection_noise + 0.90
    inspection_observed = np.where(
        treatment == 1,
        inspection_under_defense,
        inspection_under_control,
    )

    def detection_probability(treatment_value, inspection_value):
        detection_logit = (
            -0.80
            + 0.45 * treatment_value
            + 0.65 * inspection_value
            - 0.35 * z["code_complexity"]
            - 0.15 * z["code_number_tokens"]
            + 0.35 * z["reviewer_experience"]
            + 0.45 * z["code_num_strings"]
        )
        return _sigmoid(detection_logit)

    p_y0 = detection_probability(0, inspection_under_control)
    p_y1 = detection_probability(1, inspection_under_defense)

    observed_probability = np.where(treatment == 1, p_y1, p_y0)
    outcome = rng.binomial(1, observed_probability).astype(int)

    # Post-outcome collider: both use of the defense and successful detection
    # make manual review more likely.
    manual_review_logit = (
        -1.10
        + 0.90 * treatment
        + 1.00 * outcome
        + rng.normal(0.0, 0.25, size=len(feature_df))
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
        true_average_treatment_effect=float(np.mean(p_y1 - p_y0)),
        treatment_prevalence=float(causal_df["treatment"].mean()),
        outcome_prevalence=float(causal_df["outcome"].mean()),
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


def save_study_metadata(info: SyntheticStudyInfo, path: str | Path) -> Path:
    """Save hidden synthetic-study metadata for the reveal in notebook 02."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(info), indent=2), encoding="utf-8")
    return path


def save_ground_truth_dag(path: str | Path) -> Path:
    """Save the hidden synthetic DAG used for the notebook-02 reveal."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    rows = [
        {
            "source": source,
            "target": target,
            "reason": reason,
            "source_role": GROUND_TRUTH_ROLES.get(source, ""),
        }
        for source, target, reason in GROUND_TRUTH_EDGES
    ]
    pd.DataFrame(rows).to_csv(path, index=False)
    return path
