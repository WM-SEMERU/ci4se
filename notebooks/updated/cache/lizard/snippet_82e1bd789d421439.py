def get_layer(self, name: str=None):
    if name is None:
        name = self.__last_layer_name
    return self.__layers[name]