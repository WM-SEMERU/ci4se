def pre_check(self, data):
    sentences = len(re.findall('[\\.!?]+\\W+', data)) or 1
    chars = len(data) - len(re.findall('[^a-zA-Z0-9]', data))
    num_words = len(re.findall('\\s+', data))
    data = re.split('[^a-zA-Z]+', data)
    return data, sentences, chars, num_words