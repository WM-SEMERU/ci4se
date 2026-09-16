def hybrid_forward(self, F, feature_a):
    tilde_a = self.intra_attn_emb(feature_a)
    e_matrix = F.batch_dot(tilde_a, tilde_a, transpose_b=True)
    alpha = F.batch_dot(e_matrix.softmax(), tilde_a)
    return alpha