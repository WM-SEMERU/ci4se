def _is_valid(self, s):
    return (s[0] >= s[1] or s[0] == 0) and (3 - s[0] >= 3 - s[1] or s[0] == 3
        ) and 0 <= s[0] <= 3 and 0 <= s[1] <= 3