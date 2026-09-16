def readfp(self, *args, **kwargs):
    ret = configparser.SafeConfigParser.readfp(self, *args, **kwargs)
    self.parse_flask_section()
    return ret