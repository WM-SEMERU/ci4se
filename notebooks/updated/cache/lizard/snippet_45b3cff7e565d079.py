def bvlpdu_contents(self, use_dict=None, as_class=dict):
    if use_dict is None:
        use_dict = as_class()
    key_value_contents(use_dict=use_dict, as_class=as_class, key_values=((
        'function', 'DistributeBroadcastToNetwork'),))
    PDUData.dict_contents(self, use_dict=use_dict, as_class=as_class)
    return use_dict