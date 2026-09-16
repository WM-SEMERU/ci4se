def decode(self, probs, sizes=None):
    _, max_probs = torch.max(probs.transpose(0, 1), 2)
    strings = self.convert_to_strings(max_probs.view(max_probs.size(0),
        max_probs.size(1)), sizes)
    return self.process_strings(strings, remove_repetitions=True)