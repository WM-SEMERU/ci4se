def calculate_last_common_level(k, b1, b2):
    l1 = calculate_bucket_level(k, b1)
    l2 = calculate_bucket_level(k, b2)
    while l1 > l2:
        b1 = (b1 - 1) // k
        l1 -= 1
    while l2 > l1:
        b2 = (b2 - 1) // k
        l2 -= 1
    while b1 != b2:
        b1 = (b1 - 1) // k
        b2 = (b2 - 1) // k
        l1 -= 1
    return l1