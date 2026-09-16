def filename_complete(self, text, line, begidx, endidx):
    try:
        return self.real_filename_complete(text, line, begidx, endidx)
    except:
        traceback.print_exc()