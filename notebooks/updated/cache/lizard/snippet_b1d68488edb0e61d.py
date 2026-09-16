def list_group_users(self, group_id, **kwargs):
    kwargs['group_id'] = group_id
    kwargs = self._verify_sort_options(kwargs)
    api = self._get_api(iam.AccountAdminApi)
    return PaginatedResponse(api.get_users_of_group, lwrap_type=User, **kwargs)