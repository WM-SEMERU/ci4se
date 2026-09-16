def create(model, discount_factor: float, tau: float, max_grad_norm: float=None
    ):
    return DeepDeterministicPolicyGradient(tau=tau, discount_factor=
        discount_factor, model_factory=model, max_grad_norm=max_grad_norm)