def make_lib(self, version):
    if os.path.exists(POETRY_LIB_BACKUP):
        shutil.rmtree(POETRY_LIB_BACKUP)
    if os.path.exists(POETRY_LIB):
        shutil.copytree(POETRY_LIB, POETRY_LIB_BACKUP)
        shutil.rmtree(POETRY_LIB)
    try:
        self._make_lib(version)
    except Exception:
        if not os.path.exists(POETRY_LIB_BACKUP):
            raise
        shutil.copytree(POETRY_LIB_BACKUP, POETRY_LIB)
        shutil.rmtree(POETRY_LIB_BACKUP)
        raise
    finally:
        if os.path.exists(POETRY_LIB_BACKUP):
            shutil.rmtree(POETRY_LIB_BACKUP)