def is_full(self):
    capacity = self.get_true_capacity()
    if capacity != -1:
        num_signed_up = self.eighthsignup_set.count()
        return num_signed_up >= capacity
    return False