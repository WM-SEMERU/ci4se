def merge_profile(mean_profile, new_profile):
    for i in range(0, len(mean_profile)):
        if new_profile[i] is None:
            continue
        mean_profile[i].add(new_profile[i])