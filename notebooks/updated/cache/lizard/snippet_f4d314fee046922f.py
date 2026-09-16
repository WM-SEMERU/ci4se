def _mirror_groups(self):
    target_group_names = frozenset(self._get_groups().get_group_names())
    current_group_names = frozenset(self._user.groups.values_list('name',
        flat=True).iterator())
    if target_group_names != current_group_names:
        existing_groups = list(Group.objects.filter(name__in=
            target_group_names).iterator())
        existing_group_names = frozenset(group.name for group in
            existing_groups)
        new_groups = [Group.objects.get_or_create(name=name)[0] for name in
            target_group_names if name not in existing_group_names]
        self._user.groups = existing_groups + new_groups