def __html_rep(self, game_key, rep_code):
    seas, gt, num = game_key.to_tuple()
    url = [self.__domain, 'scores/htmlreports/', str(seas - 1), str(seas),
        '/', rep_code, '0', str(gt), '%04i' % num, '.HTM']
    url = ''.join(url)
    return self.__open(url)