def flatten_container(self, container):
    for names in ARG_MAP.values():
        if names[TransformationTypes.MARATHON.value]['name'] and '.' in names[
            TransformationTypes.MARATHON.value]['name']:
            marathon_dotted_name = names[TransformationTypes.MARATHON.value][
                'name']
            parts = marathon_dotted_name.split('.')
            if parts[-2] == 'parameters':
                common_type = names[TransformationTypes.MARATHON.value].get(
                    'type')
                result = self._lookup_parameter(container, parts[-1],
                    common_type)
                if result:
                    container[marathon_dotted_name] = result
            else:
                result = lookup_nested_dict(container, *parts)
                if result:
                    container[marathon_dotted_name] = result
    return container