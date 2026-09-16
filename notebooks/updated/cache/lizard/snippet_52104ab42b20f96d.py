def loadFile(self, fileName: str=None):
    msg = 'The <b>{}</b> applet has not implemented the <b>LoadFile</b> method'
    self.qteLogger.info(msg.format(self.qteAppletSignature()))