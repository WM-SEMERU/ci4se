def merge(self, session, checksums, title):
    calc = Output(calcset=checksums)
    cur_depth = 0
    for nested_depth, grid_item, download_size in session.query(model.
        Calculation.nested_depth, model.Grid.info, model.Metadata.download_size
        ).filter(model.Calculation.checksum == model.Grid.checksum, model.
        Grid.checksum == model.Metadata.checksum, model.Calculation.
        checksum.in_(checksums)).all():
        if nested_depth > cur_depth:
            cur_depth = nested_depth
        grid_item = json.loads(grid_item)
        for entity in self.hierarchy:
            topic = grid_item.get(entity['source'])
            if not topic:
                continue
            if not isinstance(topic, list):
                topic = [topic]
            calc.info[entity['source']] = list(set(calc.info.get(entity[
                'source'], []) + topic))
        calc.download_size += download_size
    if not calc.download_size:
        return None, 'Wrong parameters provided!'
    calc._nested_depth = cur_depth + 1
    calc.info['standard'] = title
    calc._checksum = calc.get_collective_checksum()
    return calc, None