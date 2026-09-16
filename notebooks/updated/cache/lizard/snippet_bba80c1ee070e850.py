def write(self, file_or_filename):
    if isinstance(file_or_filename, basestring):
        fname = os.path.basename(file_or_filename)
        logger.info('Pickling case [%s].' % fname)
        file = None
        try:
            file = open(file_or_filename, 'wb')
        except:
            logger.error("Error opening '%s'." % fname)
            return False
        finally:
            if file is not None:
                pickle.dump(self.case, file)
                file.close()
    else:
        file = file_or_filename
        pickle.dump(file, self.case)
    return True