def delete_extra_files(self, relpaths, cloud_objs):
    for cloud_obj in cloud_objs:
        if cloud_obj not in relpaths:
            if not self.test_run:
                self.delete_cloud_obj(cloud_obj)
            self.delete_count += 1
            if not self.quiet or self.verbosity > 1:
                print('Deleted: {0}'.format(cloud_obj))