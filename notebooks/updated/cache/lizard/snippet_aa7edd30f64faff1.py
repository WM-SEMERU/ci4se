def describe_consumer_groups(self, group_ids, group_coordinator_id=None):
    group_descriptions = []
    version = self._matching_api_version(DescribeGroupsRequest)
    for group_id in group_ids:
        if group_coordinator_id is not None:
            this_groups_coordinator_id = group_coordinator_id
        else:
            this_groups_coordinator_id = self._find_group_coordinator_id(
                group_id)
        if version <= 1:
            request = DescribeGroupsRequest[version](groups=(group_id,))
            response = self._send_request_to_node(this_groups_coordinator_id,
                request)
            assert len(response.groups) == 1
            group_description = response.groups[0]
            error_code = group_description[0]
            error_type = Errors.for_code(error_code)
            if error_type is not Errors.NoError:
                raise error_type("Request '{}' failed with response '{}'.".
                    format(request, response))
            group_descriptions.append(group_description)
        else:
            raise NotImplementedError(
                'Support for DescribeGroups v{} has not yet been added to KafkaAdminClient.'
                .format(version))
    return group_descriptions