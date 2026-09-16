def csv_export(self, csv_dest, fieldnames=None, encoding='UTF-8'):
    close_on_exit = False
    if isinstance(csv_dest, basestring):
        if PY_3:
            csv_dest = open(csv_dest, 'w', newline='', encoding=encoding)
        else:
            csv_dest = open(csv_dest, 'wb')
        close_on_exit = True
    try:
        if fieldnames is None:
            fieldnames = list(_object_attrnames(self.obs[0]))
        if isinstance(fieldnames, basestring):
            fieldnames = fieldnames.split()
        csv_dest.write(','.join(fieldnames) + NL)
        csvout = csv.DictWriter(csv_dest, fieldnames, extrasaction='ignore',
            lineterminator=NL)
        if hasattr(self.obs[0], '__dict__'):
            csvout.writerows(o.__dict__ for o in self.obs)
        else:
            do_all(csvout.writerow(ODict(starmap(lambda obj, fld: (fld,
                getattr(obj, fld)), zip(repeat(o), fieldnames)))) for o in
                self.obs)
    finally:
        if close_on_exit:
            csv_dest.close()