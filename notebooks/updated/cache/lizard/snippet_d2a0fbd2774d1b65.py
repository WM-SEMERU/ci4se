def infer_newX(self, Y_new, optimize=True):
    from ..inference.latent_function_inference.inferenceX import infer_newX
    return infer_newX(self, Y_new, optimize=optimize)