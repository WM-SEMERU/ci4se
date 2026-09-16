def check_tubing_TEMA(NPS=None, BWG=None):
    if NPS in TEMA_tubing:
        if BWG in TEMA_tubing[NPS]:
            return True
    return False