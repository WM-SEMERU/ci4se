def add_location(self, location, sync=True):
    LOGGER.debug('RoutingArea.add_location')
    if not sync:
        self.loc_2_add.append(location)
    else:
        if location.id is None:
            location.save()
        if self.id is not None and location.id is not None:
            params = {'id': self.id, 'locationID': location.id}
            args = {'http_operation': 'GET', 'operation_path':
                'update/locations/add', 'parameters': params}
            response = RoutingAreaService.requester.call(args)
            if response.rc != 0:
                LOGGER.warning(
                    'RoutingArea.add_location - Problem while updating routing area '
                     + self.name + '. Reason: ' + str(response.
                    response_content) + '-' + str(response.error_message) +
                    ' (' + str(response.rc) + ')')
            else:
                self.loc_ids.append(location.id)
                location.routing_area_ids.append(self.id)
        else:
            LOGGER.warning(
                'RoutingArea.add_location - Problem while updating routing area '
                 + self.name + '. Reason: location ' + location.name +
                ' id is None or self.id is None')