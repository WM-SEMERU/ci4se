def search_mosaics(name, bbox, rbox, limit, pretty):
    bbox = bbox or rbox
    cl = clientv1()
    mosaic, = cl.get_mosaic_by_name(name).items_iter(1)
    response = call_and_wrap(cl.get_quads, mosaic, bbox)
    echo_json_response(response, pretty, limit)