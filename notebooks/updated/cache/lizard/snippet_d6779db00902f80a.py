def get_structure_from_id(self, task_id, final_structure=True):
    args = {'task_id': task_id}
    field = 'output.crystal' if final_structure else 'input.crystal'
    results = tuple(self.query([field], args))
    if len(results) > 1:
        raise QueryError('More than one result found for task_id {}!'.
            format(task_id))
    elif len(results) == 0:
        raise QueryError('No structure found for task_id {}!'.format(task_id))
    c = results[0]
    return Structure.from_dict(c[field])