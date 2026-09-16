def _write_temp(content, suffix):
    with NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as out:
        out.write(content)
        return out.name