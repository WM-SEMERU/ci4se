def generate_entropy(strength, internal_entropy, external_entropy):
    if strength not in (128, 192, 256):
        raise ValueError('Invalid strength')
    if not internal_entropy:
        raise ValueError('Internal entropy is not provided')
    if len(internal_entropy) < 32:
        raise ValueError('Internal entropy too short')
    if not external_entropy:
        raise ValueError('External entropy is not provided')
    if len(external_entropy) < 32:
        raise ValueError('External entropy too short')
    entropy = hashlib.sha256(internal_entropy + external_entropy).digest()
    entropy_stripped = entropy[:strength // 8]
    if len(entropy_stripped) * 8 != strength:
        raise ValueError('Entropy length mismatch')
    return entropy_stripped