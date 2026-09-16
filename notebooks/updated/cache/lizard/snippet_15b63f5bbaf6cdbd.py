def AllFonts(sortOptions=None):
    fontList = FontList(dispatcher['AllFonts']())
    if sortOptions is not None:
        fontList.sortBy(sortOptions)
    return fontList