def make_item_class_for_custom_generator(obj):
    clsname = obj.__tohu_items_name__
    attr_names = obj.field_gens.keys()
    return make_item_class(clsname, attr_names)