def tie_weights(self):
    if self.sample_softmax > 0:
        if self.config.tie_weight:
            self.out_layer.weight = self.transformer.word_emb.weight
    else:
        if self.config.tie_weight:
            for i in range(len(self.crit.out_layers)):
                self.crit.out_layers[i
                    ].weight = self.transformer.word_emb.emb_layers[i].weight
        if self.config.tie_projs:
            for i, tie_proj in enumerate(self.config.tie_projs):
                if (tie_proj and self.config.div_val == 1 and self.config.
                    d_model != self.config.d_embed):
                    self.crit.out_projs[i
                        ] = self.transformer.word_emb.emb_projs[0]
                elif tie_proj and self.config.div_val != 1:
                    self.crit.out_projs[i
                        ] = self.transformer.word_emb.emb_projs[i]