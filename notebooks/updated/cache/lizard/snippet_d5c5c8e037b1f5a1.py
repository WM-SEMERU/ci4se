def set_temperature(self, temp):
    param = 16 + (temp - 8) * 2
    if param < 16:
        param = 253
        logger.info('Actor ' + self.name + ': Temperature control set to off')
    elif param >= 56:
        param = 254
        logger.info('Actor ' + self.name + ': Temperature control set to on')
    else:
        logger.info('Actor ' + self.name + ': Temperature control set to ' +
            str(temp))
    return self.box.homeautoswitch('sethkrtsoll', self.actor_id, param)