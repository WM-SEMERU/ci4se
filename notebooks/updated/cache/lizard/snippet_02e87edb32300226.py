def new_station(self, _id, callSign, name, affiliate, fccChannelNumber):
    if self.__v_station:
        print('[Station: %s, %s, %s, %s, %s]' % (_id, callSign, name,
            affiliate, fccChannelNumber))