def save_voxel_grid(voxel_grid, file_name):
    try:
        with open(file_name, 'wb') as fp:
            for voxel in voxel_grid:
                fp.write(struct.pack('<I', voxel))
    except IOError as e:
        print('An error occurred: {}'.format(e.args[-1]))
        raise e
    except Exception:
        raise