def getOriginLocalizedName(self, origin, pchNameArray, unNameArraySize,
    unStringSectionsToInclude):
    fn = self.function_table.getOriginLocalizedName
    result = fn(origin, pchNameArray, unNameArraySize,
        unStringSectionsToInclude)
    return result