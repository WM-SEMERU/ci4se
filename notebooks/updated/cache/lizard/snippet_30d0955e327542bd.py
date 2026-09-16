def write_u2d(self, u2d):
    filename = os.path.split(u2d.filename)[-1]
    np.savetxt(os.path.join(self.m.model_ws, self.arr_org, filename), u2d.
        array, fmt='%15.6E')
    return filename