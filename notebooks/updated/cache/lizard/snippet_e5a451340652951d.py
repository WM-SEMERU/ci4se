def get_context(self, max_frames=None, missing_entities=[]):
    if not max_frames or max_frames > len(self.frame_stack):
        max_frames = len(self.frame_stack)
    missing_entities = list(missing_entities)
    context = []
    for i in xrange(max_frames):
        frame_entities = [entity.copy() for entity in self.frame_stack[i].
            entities]
        for entity in frame_entities:
            entity['confidence'] = entity.get('confidence', 1.0) / (2.0 + i)
        context += frame_entities
    result = []
    if len(missing_entities) > 0:
        for entity in context:
            if entity.get('data') in missing_entities:
                result.append(entity)
                missing_entities.remove(entity.get('data'))
    else:
        result = context
    return result