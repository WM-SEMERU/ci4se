def dump_dict_of_nested_lists_to_h5(fname, data):
    print('writing to file: %s' % fname)
    f = h5py.File(fname)
    for i, ivalue in list(data.items()):
        igrp = f.create_group(str(i))
        for j, jvalue in enumerate(ivalue):
            jgrp = igrp.create_group(str(j))
            for k, kvalue in enumerate(jvalue):
                if kvalue.size > 0:
                    dset = jgrp.create_dataset(str(k), data=kvalue,
                        compression='gzip')
                else:
                    dset = jgrp.create_dataset(str(k), data=kvalue,
                        maxshape=(None,), compression='gzip')
    f.close()