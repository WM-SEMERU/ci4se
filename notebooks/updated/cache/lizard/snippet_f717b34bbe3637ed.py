def replace_substitutes(string):
    for non_ipa, ipa in chart.replacements.items():
        string = string.replace(non_ipa, ipa)
    return string