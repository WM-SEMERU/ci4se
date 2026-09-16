def _upgrade(self):
    logging.debug('[FeedbackResults]._upgrade()')
    if hasattr(self, 'version'):
        version = Version.fromstring(self.version)
    else:
        version = Version(0)
    logging.debug('[FeedbackResults] version=%s, class_version=%s' % (str(
        version), self.class_version))
    if version > Version.fromstring(self.class_version):
        logging.debug('[FeedbackResults] version>class_version')
        raise FutureVersionError(Version.fromstring(self.class_version),
            version)
    elif version < Version.fromstring(self.class_version):
        if version < Version(0, 1):
            self.calibration = FeedbackCalibration()
        if version < Version(0, 2):
            self.version = str(Version(0, 2))
            self.fb_resistor[self.V_fb > 5] = -1
            self.hv_resistor[self.V_hv > 5] = -1
        if version < Version(0, 3):
            self.attempt = 0
        if version < Version(0, 4):
            del self.sampling_time_ms
            del self.delay_between_samples_ms
            self.voltage = self.options.voltage
            del self.options
            del self.attempt
        if version < Version(0, 5):
            self.area = 0
            self.version = str(Version(0, 5))
        if version < Version(0, 6):
            self.amplifier_gain = None
            self.vgnd_hv = None
            self.vgnd_fb = None
            self.version = str(Version(0, 6))
            logging.info('[FeedbackResults] upgrade to version %s' % self.
                version)
    else:
        pass