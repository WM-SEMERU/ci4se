def get_example():
    features = random.sample(string.ascii_letters, NUM_SAMPLES)
    num_capitalized = len([letter for letter in features if letter in
        string.ascii_uppercase])
    num_lowercase = len([letter for letter in features if letter in string.
        ascii_lowercase])
    if num_capitalized > num_lowercase:
        label = 1
    else:
        label = -1
    return label, features