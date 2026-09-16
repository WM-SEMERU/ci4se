def item_perceel_adapter(obj, request):
    return {'id': obj.id, 'sectie': {'id': obj.sectie.id, 'afdeling': {'id':
        obj.sectie.afdeling.id, 'naam': obj.sectie.afdeling.naam,
        'gemeente': {'id': obj.sectie.afdeling.gemeente.id, 'naam': obj.
        sectie.afdeling.gemeente.naam}}}, 'capakey': obj.capakey, 'percid':
        obj.percid, 'centroid': obj.centroid, 'bounding_box': obj.bounding_box}