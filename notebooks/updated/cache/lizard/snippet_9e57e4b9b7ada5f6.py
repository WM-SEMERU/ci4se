def get_variant(self, identity, experiment_name):
    try:
        match = model.Participant.query.join(model.Experiment).filter(and_(
            model.Participant.identity == identity, model.Experiment.name ==
            experiment_name)).first()
        return match.variant.name if match else None
    finally:
        self.Session.close()