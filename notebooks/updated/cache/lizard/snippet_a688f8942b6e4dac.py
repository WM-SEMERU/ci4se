def as_list(self, label=1, **kwargs):
    label_to_use = label if self.mode == 'classification' else self.dummy_label
    ans = self.domain_mapper.map_exp_ids(self.local_exp[label_to_use], **kwargs
        )
    ans = [(x[0], float(x[1])) for x in ans]
    return ans