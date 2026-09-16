def adj_par_names(self):
    if self.__pst is not None:
        return self.pst.adj_par_names
    else:
        return self.jco.par_names