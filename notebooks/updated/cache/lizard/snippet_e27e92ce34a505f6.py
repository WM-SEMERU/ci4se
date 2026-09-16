def get_vars_dataframe(self, *varnames):
    import pandas as pd
    if self.is_task:
        df = pd.DataFrame([{v: self.input.get(v, None) for v in varnames}],
            index=[self.name], columns=varnames)
        df['class'] = self.__class__.__name__
        return df
    elif self.is_work:
        frames = [task.get_vars_dataframe(*varnames) for task in self]
        return pd.concat(frames)
    elif self.is_flow:
        frames = [work.get_vars_dataframe(*varnames) for work in self]
        return pd.concat(frames)
    else:
        return pd.DataFrame(index=[self.name])