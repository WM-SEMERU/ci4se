def createLearningRateScheduler(self, params, optimizer):
    lr_scheduler = params.get('lr_scheduler', None)
    if lr_scheduler is None:
        return None
    if lr_scheduler == 'StepLR':
        lr_scheduler_params = "{'step_size': 1, 'gamma':" + str(params[
            'learning_rate_factor']) + '}'
    else:
        lr_scheduler_params = params.get('lr_scheduler_params', None)
        if lr_scheduler_params is None:
            raise ValueError("Missing 'lr_scheduler_params' for {}".format(
                lr_scheduler))
    clazz = eval('torch.optim.lr_scheduler.{}'.format(lr_scheduler))
    lr_scheduler_params = eval(lr_scheduler_params)
    return clazz(optimizer, **lr_scheduler_params)