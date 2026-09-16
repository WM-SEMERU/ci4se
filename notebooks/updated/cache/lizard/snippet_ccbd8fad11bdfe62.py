def _clean_file(self, f):
    if os.path.exists(f) and not os.path.islink(f):
        tmp_file = tempfile.TemporaryFile(mode='w+b')
        try:
            fh = open(f, 'r')
            data = fh.readlines()
            fh.close()
            if len(data) > 0:
                for l in data:
                    new_l = self._clean_line(l)
                    tmp_file.write(new_l.encode('utf-8'))
                tmp_file.seek(0)
        except Exception as e:
            self.logger.exception(e)
            raise Exception(
                'CleanFile Error: Cannot Open File For Reading - %s' % f)
        try:
            if len(data) > 0:
                new_fh = open(f, 'wb')
                for line in tmp_file:
                    new_fh.write(line)
                new_fh.close()
        except Exception as e:
            self.logger.exception(e)
            raise Exception(
                'CleanFile Error: Cannot Write to New File - %s' % f)
        finally:
            tmp_file.close()