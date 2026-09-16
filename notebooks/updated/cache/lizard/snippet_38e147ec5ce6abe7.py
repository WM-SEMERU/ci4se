def analysis(self):
    if self._analysis is not None:
        return self._analysis
    if self.cache_dir is not None:
        path = os.path.join(self.cache_dir, self.checksum)
        try:
            if self.refresh_cache:
                raise IOError
            with open(path + '.pickle', 'rb') as pickle_file:
                self._analysis = pickle.load(pickle_file)
        except IOError:
            self._analysis = librosa_analysis.analyze_frames(self.
                all_as_mono(), self.samplerate)
            with open(path + '.pickle', 'wb') as pickle_file:
                pickle.dump(self._analysis, pickle_file, pickle.
                    HIGHEST_PROTOCOL)
    else:
        self._analysis = librosa_analysis.analyze_frames(self.all_as_mono(),
            self.samplerate)
    return self._analysis