def _is_saccharide_arrow(self, before, after):
    if before and after and before[-1].isdigit() and after[0].isdigit(
        ) and before.rstrip('0123456789').endswith('(') and after.lstrip(
        '0123456789').startswith(')-'):
        return True
    else:
        return False