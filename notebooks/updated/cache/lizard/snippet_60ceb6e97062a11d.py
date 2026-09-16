def add_file_metadata(self, fname):
    file_dict = {}
    file_dict['fullfilename'] = fname
    try:
        file_dict['name'] = os.path.basename(fname)
        file_dict['date'] = self.GetDateAsString(fname)
        file_dict['size'] = os.path.getsize(fname)
        file_dict['path'] = os.path.dirname(fname)
    except IOError:
        print('Error getting metadata for file')
    self.fl_metadata.append(file_dict)