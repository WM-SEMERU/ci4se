def parse_a1(a1_text):
    entities = {}
    for line in a1_text.split('\n'):
        if len(line) == 0:
            continue
        tokens = line.rstrip().split('\t')
        if len(tokens) != 3:
            raise Exception('Expected three tab-seperated tokens per line ' +
                'in the a1 file output from TEES.')
        identifier = tokens[0]
        entity_info = tokens[1]
        entity_name = tokens[2]
        info_tokens = entity_info.split()
        if len(info_tokens) != 3:
            raise Exception('Expected three space-seperated tokens in the ' +
                'second column of the a2 file output from TEES.')
        entity_type = info_tokens[0]
        first_offset = int(info_tokens[1])
        second_offset = int(info_tokens[2])
        offsets = first_offset, second_offset
        entities[identifier] = TEESEntity(identifier, entity_type,
            entity_name, offsets)
    return entities