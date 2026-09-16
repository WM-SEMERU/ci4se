def find_apps(name=None, name_mode='exact', category=None, all_versions=
    None, published=None, billed_to=None, created_by=None, developer=None,
    created_after=None, created_before=None, modified_after=None,
    modified_before=None, describe=False, limit=None, return_handler=False,
    first_page_size=100, **kwargs):
    return find_global_executables(dxpy.api.system_find_apps, name=name,
        name_mode=name_mode, category=category, all_versions=all_versions,
        published=published, billed_to=billed_to, created_by=created_by,
        developer=developer, created_after=created_after, created_before=
        created_before, modified_after=modified_after, modified_before=
        modified_before, describe=describe, limit=limit, return_handler=
        return_handler, first_page_size=first_page_size, **kwargs)