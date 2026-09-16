def initDeviceScan(self):
    self.__isIphone = self.detectIphoneOrIpod()
    self.__isAndroidPhone = self.detectAndroidPhone()
    self.__isTierTablet = self.detectTierTablet()
    self.__isTierIphone = self.detectTierIphone()
    self.__isTierRichCss = self.detectTierRichCss()
    self.__isTierGenericMobile = self.detectTierOtherPhones()