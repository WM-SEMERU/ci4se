def _normalize(self, name):
    name = re.sub(
        "^(Senator|Representative|Sen\\.?|Rep\\.?|Hon\\.?|Right Hon\\.?|Mr\\.?|Mrs\\.?|Ms\\.?|L'hon\\.?|Assembly(member|man|woman)) "
        , '', name)
    return name.strip().lower().replace('.', '')