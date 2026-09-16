def execute(self, conn, daoinput, transaction=False):
    binds = {}
    bindlist = []
    if isinstance(daoinput, dict) and 'block_name' in daoinput.keys():
        binds = {'block_name': daoinput['block_name']}
        r = self.dbi.processData(self.sql_sel, binds, conn, False)
        bfile = self.format(r)
        bfile_list = []
        for f in bfile:
            bfile_list.append(f[0])
        if 'child_parent_id_list' in daoinput.keys():
            files = []
            for i in daoinput['child_parent_id_list']:
                files.append(i[0])
            if set(files) - set(bfile_list):
                dbsExceptionHandler('dbsException-invalid-input2',
                    'Files required in the same block for FileParent/insert2 dao.'
                    , self.logger.exception)
        else:
            dbsExceptionHandler('dbsException-invalid-input2',
                'child_parent_id_list required for FileParent/insert2 dao.',
                self.logger.exception)
    else:
        dbsExceptionHandler('dbsException-invalid-input2',
            'Block_name required in the same block for FileParent/insert2 dao.'
            , self.logger.exception)
    binds = {}
    for pf in daoinput['child_parent_id_list']:
        binds = {'this_file_id': pf[0], 'parent_file_id': pf[1]}
        bindlist.append(binds)
    self.dbi.processData(self.sql, bindlist, conn, transaction)