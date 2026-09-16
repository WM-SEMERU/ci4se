def unique_event_labels(event_list):
    if isinstance(event_list, dcase_util.containers.MetaDataContainer):
        return event_list.unique_event_labels
    else:
        labels = []
        for event in event_list:
            if 'event_label' in event and event['event_label'] not in labels:
                labels.append(event['event_label'])
        labels.sort()
        return labels