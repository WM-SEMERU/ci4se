def __convertChannelMask(self, channelsArray):
    maskSet = 0
    for eachChannel in channelsArray:
        mask = 1 << eachChannel
        maskSet = maskSet | mask
    return maskSet