def sia_concept_style(subsystem):
    unpartitioned_ces = _ces(subsystem)
    sia_cause = directional_sia(subsystem, Direction.CAUSE, unpartitioned_ces)
    sia_effect = directional_sia(subsystem, Direction.EFFECT, unpartitioned_ces
        )
    return SystemIrreducibilityAnalysisConceptStyle(sia_cause, sia_effect)