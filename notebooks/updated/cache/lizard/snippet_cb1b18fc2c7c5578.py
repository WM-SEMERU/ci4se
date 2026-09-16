def isTagEqual(self, other):
    try:
        if self.tagName != other.tagName:
            return False
        myAttributes = self._attributes
        otherAttributes = other._attributes
        attributeKeysSelf = list(myAttributes.keys())
        attributeKeysOther = list(otherAttributes.keys())
    except:
        return False
    if set(attributeKeysSelf) != set(attributeKeysOther):
        return False
    for key in attributeKeysSelf:
        if myAttributes.get(key) != otherAttributes.get(key):
            return False
    return True