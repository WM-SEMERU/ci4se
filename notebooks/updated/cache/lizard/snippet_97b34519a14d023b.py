def patch(self, measurementId):
    data = request.get_json()
    if data is not None:
        logger.debug('Received payload for ' + measurementId + ' - ' + str(
            data))
        if self._measurementController.editMeasurement(measurementId, data):
            return None, 200
        else:
            logger.warning('Unable to edit payload ' + measurementId)
            return None, 404
    else:
        logger.error('Invalid data payload received ' + measurementId)
        return None, 400