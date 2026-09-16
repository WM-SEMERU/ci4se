def get_resource_by_agent(self, agent_id):
    collection = JSONClientValidated('resource', collection='Resource',
        runtime=self._runtime)
    result = collection.find_one(dict({'agentIds': {'$in': [str(agent_id)]}
        }, **self._view_filter()))
    return objects.Resource(osid_object_map=result, runtime=self._runtime,
        proxy=self._proxy)