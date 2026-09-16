def saabas(model, data):
    return lambda X: TreeExplainer(model).shap_values(X, approximate=True)