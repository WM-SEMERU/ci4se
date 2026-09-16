def validate(self):
    super().validate()
    nb_entities = len(self.entities)
    if nb_entities != self.rows:
        raise self.error('Number of entities: %s != number of rows: %s' % (
            nb_entities, self.rows))