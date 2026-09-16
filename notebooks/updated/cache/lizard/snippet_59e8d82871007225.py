def generate(self, data, width, height, padding=(0, 0, 0, 0), output_format
    ='png', inverted=False):
    digest_byte_list = self._data_to_digest_byte_list(data)
    matrix = self._generate_matrix(digest_byte_list)
    if output_format == 'ascii':
        foreground = '+'
        background = '-'
    else:
        background = self.background
        foreground = self.foreground[digest_byte_list[0] % len(self.foreground)
            ]
    if inverted:
        foreground, background = background, foreground
    if output_format == 'ascii':
        return self._generate_ascii(matrix, foreground, background)
    else:
        return self._generate_image(matrix, width, height, padding,
            foreground, background, output_format)