def _compute_mfcc_c_extension(self):
    self.log('Computing MFCCs using C extension...')
    try:
        self.log('Importing cmfcc...')
        import aeneas.cmfcc.cmfcc
        self.log('Importing cmfcc... done')
        self.__mfcc = aeneas.cmfcc.cmfcc.compute_from_data(self.audio_file.
            audio_samples, self.audio_file.audio_sample_rate, self.rconf[
            RuntimeConfiguration.MFCC_FILTERS], self.rconf[
            RuntimeConfiguration.MFCC_SIZE], self.rconf[
            RuntimeConfiguration.MFCC_FFT_ORDER], self.rconf[
            RuntimeConfiguration.MFCC_LOWER_FREQUENCY], self.rconf[
            RuntimeConfiguration.MFCC_UPPER_FREQUENCY], self.rconf[
            RuntimeConfiguration.MFCC_EMPHASIS_FACTOR], self.rconf[
            RuntimeConfiguration.MFCC_WINDOW_LENGTH], self.rconf[
            RuntimeConfiguration.MFCC_WINDOW_SHIFT])[0].transpose()
        self.log('Computing MFCCs using C extension... done')
        return True, None
    except Exception as exc:
        self.log_exc('An unexpected error occurred while running cmfcc',
            exc, False, None)
    return False, None