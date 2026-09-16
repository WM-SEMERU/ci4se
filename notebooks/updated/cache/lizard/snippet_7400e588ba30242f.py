def chests_per_chunk(chunk):
    chests = []
    for entity in chunk['Entities']:
        eid = entity['id'].value
        if eid == 'Minecart' and entity['type'
            ].value == 1 or eid == 'minecraft:chest_minecart':
            x, y, z = entity['Pos']
            x, y, z = x.value, y.value, z.value
            try:
                items = items_from_nbt(entity['Items'])
            except KeyError:
                items = {}
            chests.append(Chest('Minecart with chest', (x, y, z), items))
    for entity in chunk['TileEntities']:
        eid = entity['id'].value
        if eid == 'Chest' or eid == 'minecraft:chest':
            x, y, z = entity['x'].value, entity['y'].value, entity['z'].value
            try:
                items = items_from_nbt(entity['Items'])
            except KeyError:
                items = {}
            chests.append(Chest('Chest', (x, y, z), items))
    return chests