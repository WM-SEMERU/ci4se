def _get_summary_struct(self):
    model_fields = [('Number of coefficients', 'num_coefficients'), (
        'Number of examples', 'num_examples'), ('Number of classes',
        'num_classes'), ('Number of feature columns', 'num_features'), (
        'Number of unpacked features', 'num_unpacked_features')]
    hyperparam_fields = [('L1 penalty', 'l1_penalty'), ('L2 penalty',
        'l2_penalty')]
    solver_fields = [('Solver', 'solver'), ('Solver iterations',
        'training_iterations'), ('Solver status', 'training_solver_status'),
        ('Training time (sec)', 'training_time')]
    training_fields = [('Log-likelihood', 'training_loss')]
    coefs = self.coefficients
    top_coefs, bottom_coefs = _toolkit_get_topk_bottomk(coefs, k=5)
    coefs_list, titles_list = _summarize_coefficients(top_coefs, bottom_coefs)
    return [model_fields, hyperparam_fields, solver_fields, training_fields
        ] + coefs_list, ['Schema', 'Hyperparameters', 'Training Summary',
        'Settings'] + titles_list