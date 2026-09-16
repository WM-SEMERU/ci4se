def fisher_vector_product(self, vector, kl_divergence_gradient, model):
    assert not vector.requires_grad, 'Vector must not propagate gradient'
    dot_product = vector @ kl_divergence_gradient
    double_gradient = torch.autograd.grad(dot_product, model.
        policy_parameters(), retain_graph=True)
    fvp = p2v(x.contiguous() for x in double_gradient)
    return fvp + vector * self.cg_damping