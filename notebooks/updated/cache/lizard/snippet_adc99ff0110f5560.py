def mremove(self, class_name, names):
    if class_name not in self.components:
        logger.error('Component class {} not found'.format(class_name))
        return None
    if not isinstance(names, pd.Index):
        names = pd.Index(names)
    cls_df = self.df(class_name)
    cls_df.drop(names, inplace=True)
    pnl = self.pnl(class_name)
    for df in itervalues(pnl):
        df.drop(df.columns.intersection(names), axis=1, inplace=True)