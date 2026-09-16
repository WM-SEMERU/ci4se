def update(self, instance, validated_data):
    partitions = validated_data.pop('relationpartition_set', None)
    with transaction.atomic():
        instance = super().update(instance, validated_data)
        if partitions is not None:
            instance.relationpartition_set.all().delete()
            self._create_partitions(instance, partitions)
    return instance