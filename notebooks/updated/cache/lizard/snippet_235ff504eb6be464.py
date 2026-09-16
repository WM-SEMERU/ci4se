def infer_type(self, in_type):
    return in_type, [in_type[0]] * len(self.list_outputs()), [in_type[0]
        ] * len(self.list_auxiliary_states())