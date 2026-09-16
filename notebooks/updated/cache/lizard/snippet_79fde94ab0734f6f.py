def process_calibration(self, save=True):
    if not self.save_data:
        raise Exception('Cannot process an unsaved calibration')
    avg_signal = np.mean(self.datafile.get_data(self.current_dataset_name +
        '/signal'), axis=0)
    diffdB = attenuation_curve(self.stimulus.signal()[0], avg_signal, self.
        stimulus.samplerate(), self.calf)
    logger = logging.getLogger('main')
    logger.debug('The maximum dB attenuation is {}, caldB {}'.format(max(
        diffdB), self.caldb))
    self.datafile.init_data(self.current_dataset_name, mode='calibration',
        dims=diffdB.shape, nested_name='calibration_intensities')
    self.datafile.append(self.current_dataset_name, diffdB, nested_name=
        'calibration_intensities')
    relevant_info = {'frequencies': 'all', 'calibration_dB': self.caldb,
        'calibration_voltage': self.calv, 'calibration_frequency': self.calf}
    self.datafile.set_metadata('/'.join([self.current_dataset_name,
        'calibration_intensities']), relevant_info)
    mean_reftone = np.mean(self.datafile.get_data(self.current_dataset_name +
        '/reference_tone'), axis=0)
    tone_amp = signal_amplitude(mean_reftone, self.player.get_aifs())
    db = calc_db(tone_amp, self.mphonesens, self.mphonedb)
    self.protocol_model.remove(0)
    return diffdB, self.current_dataset_name, self.calf, db