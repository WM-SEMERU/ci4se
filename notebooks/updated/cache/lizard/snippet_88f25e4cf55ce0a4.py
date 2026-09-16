def read_csv(text, sep='\t'):
    import pandas as pd
    return pd.read_csv(StringIO(text), sep='\t')