def substances_to_frame(substances, properties=None):
    import pandas as pd
    if isinstance(substances, Substance):
        substances = [substances]
    properties = set(properties) | set(['sid']) if properties else None
    return pd.DataFrame.from_records([s.to_dict(properties) for s in
        substances], index='sid')