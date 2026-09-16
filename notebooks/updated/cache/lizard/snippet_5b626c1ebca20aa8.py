def showMessageOverlay(self, pchText, pchCaption, pchButton0Text,
    pchButton1Text, pchButton2Text, pchButton3Text):
    fn = self.function_table.showMessageOverlay
    result = fn(pchText, pchCaption, pchButton0Text, pchButton1Text,
        pchButton2Text, pchButton3Text)
    return result