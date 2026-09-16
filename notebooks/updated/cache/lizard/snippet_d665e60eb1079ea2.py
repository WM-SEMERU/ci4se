def _aicc(model_results, nobs):
    aic = model_results.aic
    df_model = model_results.df_model + 1
    return aic + 2.0 * df_model * (nobs / (nobs - df_model - 1.0) - 1.0)