def cdf_info(self):
    mycdf_info = {}
    mycdf_info['CDF'] = self.file
    mycdf_info['Version'] = self._version
    mycdf_info['Encoding'] = self._encoding
    mycdf_info['Majority'] = self._majority
    mycdf_info['rVariables'], mycdf_info['zVariables'] = self._get_varnames()
    mycdf_info['Attributes'] = self._get_attnames()
    mycdf_info['Copyright'] = self._copyright
    mycdf_info['Checksum'] = self._md5
    mycdf_info['Num_rdim'] = self._num_rdim
    mycdf_info['rDim_sizes'] = self._rdim_sizes
    mycdf_info['Compressed'] = self._compressed
    if self.cdfversion > 2:
        mycdf_info['LeapSecondUpdated'] = self._leap_second_updated
    return mycdf_info