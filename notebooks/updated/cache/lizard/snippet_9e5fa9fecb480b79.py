def detect_interval(self, min_head_length=None, max_head_length=None,
    min_tail_length=None, max_tail_length=None):
    head = self.detect_head(min_head_length, max_head_length)
    tail = self.detect_tail(min_tail_length, max_tail_length)
    begin = head
    end = self.real_wave_mfcc.audio_length - tail
    self.log(['Audio length: %.3f', self.real_wave_mfcc.audio_length])
    self.log(['Head length:  %.3f', head])
    self.log(['Tail length:  %.3f', tail])
    self.log(['Begin:        %.3f', begin])
    self.log(['End:          %.3f', end])
    if begin >= TimeValue('0.000') and end > begin:
        self.log(['Returning %.3f %.3f', begin, end])
        return begin, end
    self.log('Returning (0.000, 0.000)')
    return TimeValue('0.000'), TimeValue('0.000')