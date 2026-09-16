def calculate_bw(age, weight, height, sex):
    if sex:
        return 0.203 - 0.07 * age + 0.1069 * height + 0.2466 * weight
    else:
        return 2.447 - 0.09516 * age + 0.1074 * height + 0.3362 * weight