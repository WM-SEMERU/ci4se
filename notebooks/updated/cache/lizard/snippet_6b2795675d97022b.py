def neural_networks(self):
    result = []
    for models in self.allele_to_allele_specific_models.values():
        result.extend(models)
    result.extend(self.class1_pan_allele_models)
    return result