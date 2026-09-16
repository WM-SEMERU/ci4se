def item_gewest_adapter(obj, request):
    return {'id': obj.id, 'namen': obj._namen, 'centroid': obj.centroid,
        'bounding_box': obj.bounding_box}