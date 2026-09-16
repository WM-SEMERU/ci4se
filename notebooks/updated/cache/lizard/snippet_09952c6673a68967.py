def cubes():
    cubes = []
    for cube in get_manager().list_cubes():
        cubes.append({'name': cube})
    return jsonify({'status': 'ok', 'data': cubes})