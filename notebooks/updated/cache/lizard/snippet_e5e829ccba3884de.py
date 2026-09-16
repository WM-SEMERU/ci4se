def is_chinese(name):
    if not name:
        return False
    for ch in name:
        ordch = ord(ch)
        if (not 13312 <= ordch <= 40959 and not 131072 <= ordch <= 183983 and
            not 63744 <= ordch <= ordch and not 194560 <= ordch <= 195103):
            return False
    return True