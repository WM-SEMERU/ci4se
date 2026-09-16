def _is_gs_folder(cls, result):
    return cls.is_key(result) and result.size == 0 and result.name.endswith(cls
        ._gs_folder_suffix)