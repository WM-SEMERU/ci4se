def hazard_notes(self):
    notes = []
    hazard = definition(self.hazard.keywords.get('hazard'))
    if 'notes' in hazard:
        notes += hazard['notes']
    if self.hazard.keywords['layer_mode'] == 'classified':
        if 'classified_notes' in hazard:
            notes += hazard['classified_notes']
    if self.hazard.keywords['layer_mode'] == 'continuous':
        if 'continuous_notes' in hazard:
            notes += hazard['continuous_notes']
    if self.hazard.keywords['hazard_category'] == 'single_event':
        if 'single_event_notes' in hazard:
            notes += hazard['single_event_notes']
    if self.hazard.keywords['hazard_category'] == 'multiple_event':
        if 'multi_event_notes' in hazard:
            notes += hazard['multi_event_notes']
    return notes