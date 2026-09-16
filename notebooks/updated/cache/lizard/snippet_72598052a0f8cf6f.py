def _generate_state_token(self, length=32):
    choices = ascii_letters + digits
    return ''.join(SystemRandom().choice(choices) for _ in range(length))