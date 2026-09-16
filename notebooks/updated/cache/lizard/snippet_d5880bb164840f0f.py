def instantiate(self, **extra_args):
    input_block = self.input_block.instantiate()
    backbone = self.backbone.instantiate(**extra_args)
    return QDistributionalModel(input_block=input_block, backbone=backbone,
        action_space=extra_args['action_space'], vmin=self.vmin, vmax=self.
        vmax, atoms=self.atoms)