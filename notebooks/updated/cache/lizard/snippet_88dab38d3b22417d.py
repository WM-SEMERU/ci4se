def cmd_antenna(self, args):
    if len(args) != 2:
        if self.gcs_location is None:
            print('GCS location not set')
        else:
            print('GCS location %s' % str(self.gcs_location))
        return
    self.gcs_location = float(args[0]), float(args[1])