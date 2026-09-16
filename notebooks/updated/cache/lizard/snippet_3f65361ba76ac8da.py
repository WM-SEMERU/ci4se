def count_generated_adv_examples(self):
    result = {}
    for v in itervalues(self.data):
        s_id = v['submission_id']
        result[s_id] = result.get(s_id, 0) + len(v['images'])
    return result