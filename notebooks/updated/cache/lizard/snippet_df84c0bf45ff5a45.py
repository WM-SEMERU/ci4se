def _write_to_file(self, fileinfo, filename):
    txt = to_text_string(fileinfo.editor.get_text_with_eol())
    fileinfo.encoding = encoding.write(txt, filename, fileinfo.encoding)