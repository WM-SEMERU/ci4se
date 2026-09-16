def can_produce_rules(self):
    if not self.check_type(self.jobject,
        'weka.associations.AssociationRulesProducer'):
        return False
    return javabridge.call(self.jobject, 'canProduceRules', '()Z')