def detectOperaMobile(self):
    return UAgentInfo.engineOpera in self.__userAgent and (UAgentInfo.mini in
        self.__userAgent or UAgentInfo.mobi in self.__userAgent)