"""
Data preparation for the three-notebook causal inference tutorial.

The raw code/docstring corpus is enriched with three synthetic baseline/context
variables:

- developer_experience
- rollout_eligibility
- noise_feature

The synthetic observational study then creates distinct causal roles so the
later notebooks can demonstrate why correlation alone does not determine a DAG.
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


# Variables exposed to notebooks 01 and 02.
DEFAULT_COVARIATES = [
    "code_number_tokens",
    "code_complexity",
    "code_num_identifiers",
    "code_num_strings",
    "developer_experience",
    "rollout_eligibility",
    "noise_feature",
    "docstring_detail_score",
    "review_flag",
]


GROUND_TRUTH_EDGES = [
    ("code_number_tokens", "treatment", "larger code increases intervention use"),
    ("code_number_tokens", "output", "larger code makes successful documentation harder"),
    ("code_complexity", "treatment", "more complex code increases intervention use"),
    ("code_complexity", "output", "more complex code makes the outcome harder"),
    ("developer_experience", "treatment", "experience influences intervention uptake"),
    ("developer_experience", "output", "experience improves documentation success"),
    ("rollout_eligibility", "treatment", "eligibility encourages intervention use"),
    ("code_num_strings", "output", "string-heavy code affects documentation difficulty"),
    ("treatment", "docstring_detail_score", "the intervention increases documentation detail"),
    ("docstring_detail_score", "output", "more detailed documentation improves success"),
    ("treatment", "output", "the intervention also has a direct effect"),
    ("treatment", "review_flag", "intervention use changes review probability"),
    ("output", "review_flag", "the observed outcome also changes review probability"),
]


GROUND_TRUTH_ROLES = {
    "code_number_tokens": "confounder",
    "code_complexity": "confounder",
    "developer_experience": "confounder",
    "rollout_eligibility": "instrument_candidate",
    "code_num_strings": "outcome_predictor",
    "docstring_detail_score": "mediator",
    "review_flag": "collider",
    "code_num_identifiers": "proxy_or_correlated_measurement",
    "noise_feature": "irrelevant",
    "treatment": "treatment",
    "output": "outcome",
}


def load_source_data(
    path: str | Path,
    required_columns=(
        "input_code",
        "output_docstring",
        "developer_experience",
        "rollout_eligibility",
        "noise_feature",
    ),
) -> pd.DataFrame:
    """Load the enriched raw corpus and validate the required columns."""
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
    """Extract lightweight lexical features from Python source."""
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


def _docstring_features(text: str) -> dict:
    text = text.strip()
    return {
        "reference_docstring_words": len(text.split()),
        "reference_docstring_sentences": len(re.findall(r"[.!?]+", text)),
    }


def engineer_features(
    source_df: pd.DataFrame,
    cache_dir: str | Path = "./cache/lizard",
) -> pd.DataFrame:
    """Create baseline code/text features while preserving context variables."""
    df = source_df.copy().reset_index(drop=True)
    cache_dir = Path(cache_dir)
    complexity_cache = {}

    code_rows = []
    doc_rows = []

    for code in df["input_code"]:
        source = "" if pd.isna(code) else str(code)
        features = _lexical_code_features(source)
        features["code_complexity"] = _complexity_from_lizard(
            source,
            cache_dir,
            complexity_cache,
        )
        code_rows.append(features)

    for docstring in df["output_docstring"]:
        text = "" if pd.isna(docstring) else str(docstring)
        doc_rows.append(_docstring_features(text))

    engineered = pd.concat(
        [
            pd.DataFrame(code_rows, index=df.index),
            pd.DataFrame(doc_rows, index=df.index),
        ],
        axis=1,
    )

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
    Generate an observational dataset with deliberately different causal roles.

    Ground-truth structure:
    - code size, complexity, and developer experience are confounders;
    - rollout eligibility is an instrument candidate;
    - code_num_strings predicts outcome only;
    - docstring_detail_score is a mediator;
    - review_flag is a collider;
    - code_num_identifiers is a correlated proxy-like measurement;
    - noise_feature is irrelevant.
    """
    required = [
        "code_number_tokens",
        "code_complexity",
        "code_num_identifiers",
        "code_num_strings",
        "reference_docstring_words",
        "developer_experience",
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
        "reference_docstring_words",
        "developer_experience",
    ]
    z = _standardize(feature_df[continuous])

    rollout = feature_df["rollout_eligibility"].astype(int).to_numpy()

    # Treatment assignment: intentionally confounded.
    treatment_logit = (
        -0.35
        + 0.50 * z["code_complexity"]
        + 0.35 * z["code_number_tokens"]
        - 0.50 * z["developer_experience"]
        + 1.00 * rollout
    )
    propensity = np.clip(_sigmoid(treatment_logit), 0.05, 0.95)
    treatment = rng.binomial(1, propensity).astype(int)

    # Post-treatment mediator. Keep the same latent noise for potential outcomes.
    mediator_noise = rng.normal(0.0, 0.80, size=len(feature_df))
    mediator_base = (
        0.40 * z["reference_docstring_words"]
        - 0.20 * z["code_complexity"]
        + mediator_noise
    )
    mediator_observed = mediator_base + 0.80 * treatment

    def outcome_probability(treatment_value, mediator_value):
        outcome_logit = (
            -0.70
            + 0.50 * treatment_value
            + 0.55 * mediator_value
            - 0.40 * z["code_complexity"]
            - 0.20 * z["code_number_tokens"]
            + 0.40 * z["developer_experience"]
            + 0.55 * z["code_num_strings"]
        )
        return _sigmoid(outcome_logit)

    p_y0 = outcome_probability(0, mediator_base)
    p_y1 = outcome_probability(1, mediator_base + 0.80)

    observed_probability = np.where(treatment == 1, p_y1, p_y0)
    output = rng.binomial(1, observed_probability).astype(int)

    # Collider: both treatment and the realized outcome affect review.
    review_logit = (
        -1.10
        + 0.90 * treatment
        + 1.00 * output
        + rng.normal(0.0, 0.25, size=len(feature_df))
    )
    review_flag = rng.binomial(1, _sigmoid(review_logit)).astype(int)

    causal_df = pd.DataFrame(
        {
            "unit_id": np.arange(len(feature_df), dtype=int),
            "treatment": treatment,
            "output": output,
            "code_number_tokens": feature_df["code_number_tokens"].to_numpy(),
            "code_complexity": feature_df["code_complexity"].to_numpy(),
            "code_num_identifiers": feature_df["code_num_identifiers"].to_numpy(),
            "code_num_strings": feature_df["code_num_strings"].to_numpy(),
            "developer_experience": feature_df["developer_experience"].to_numpy(),
            "rollout_eligibility": rollout,
            "noise_feature": feature_df["noise_feature"].to_numpy(),
            "docstring_detail_score": mediator_observed,
            "review_flag": review_flag,
        }
    )

    info = SyntheticStudyInfo(
        seed=seed,
        true_average_treatment_effect=float(np.mean(p_y1 - p_y0)),
        treatment_prevalence=float(causal_df["treatment"].mean()),
        outcome_prevalence=float(causal_df["output"].mean()),
    )

    return causal_df, info


def validate_causal_dataset(
    causal_df: pd.DataFrame,
    covariates=DEFAULT_COVARIATES,
    treatment: str = "treatment",
    outcome: str = "output",
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
                "treatment=0",
                "treatment=1",
                "outcome mean",
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


def save_ground_truth_dag(path: str | Path) -> Path:
    """
    Save the synthetic DAG used to generate the teaching data.

    This is intended to be revealed only after the learner has attempted the
    graph-construction exercise.
    """
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
