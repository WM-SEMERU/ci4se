def append(self, element):
    if is_valid_type(element, Element):
        self._class_collection_map[element.__class__].setdefault(element.id,
            element)