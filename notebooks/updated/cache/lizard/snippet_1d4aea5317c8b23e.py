def set_val(self, nval):
    with open(os.path.join(self._base, self._attr), 'w') as file_obj:
        file_obj.write(str(nval) + '\n')