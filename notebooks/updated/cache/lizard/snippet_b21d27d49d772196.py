def _list_audio_files(self, sub_dir=''):
    audio_files = list()
    for possibly_audio_file in os.listdir('{}/{}'.format(self.src_dir, sub_dir)
        ):
        file_format = ''.join(possibly_audio_file.split('.')[-1])
        if file_format.lower() == 'wav':
            audio_files.append(possibly_audio_file)
    return audio_files