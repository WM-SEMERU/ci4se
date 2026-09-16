def patch(self):
    json = request.get_json()
    logger.info('Updating target state with ' + str(json))
    self._targetStateController.updateTargetState(json)
    return None, 200