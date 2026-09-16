def select_where(self, table, cols, pk_att, pk):
    if self.orng_tables:
        data = []
        for ex in self.orng_tables[table]:
            if str(ex[str(pk_att)]) == str(pk):
                data.append([ex[str(col)] for col in cols])
        return data
    else:
        return self.src.select_where(table, cols, pk_att, pk)