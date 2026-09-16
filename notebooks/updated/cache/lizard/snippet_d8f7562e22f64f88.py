def contrast(colour1, colour2):
    r
    colour_for_type = Colour()
    if type(colour1) is type(colour_for_type):
        mycolour1 = colour1
    else:
        try:
            mycolour1 = Colour(colour1)
        except:
            raise TypeError('colour1 must be a colourettu.colour')
    if type(colour2) is type(colour_for_type):
        mycolour2 = colour2
    else:
        try:
            mycolour2 = Colour(colour2)
        except:
            raise TypeError('colour2 must be a colourettu.colour')
    lum1 = mycolour1.luminance()
    lum2 = mycolour2.luminance()
    minlum = min(lum1, lum2)
    maxlum = max(lum1, lum2)
    return (maxlum + 0.05) / (minlum + 0.05)