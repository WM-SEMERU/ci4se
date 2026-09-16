def on_tomlkit_dumps(self, tomlkit, config, dictionary, **kwargs):
    inline_tables = set(kwargs.get('inline_tables', []))

    def _dump_dict(dictionary, source, source_path=[]):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                is_inline = any([fnmatch.fnmatch('.'.join(source_path + [
                    key]), pattern) for pattern in inline_tables])
                if is_inline:
                    table = tomlkit.inline_table()
                    for inline_key, inline_value in value.items():
                        if isinstance(inline_value, dict):
                            table[inline_key] = _dump_dict(inline_value,
                                tomlkit.inline_table(), source_path=
                                source_path + [inline_key])
                        else:
                            table[inline_key] = inline_value
                    source[key] = table
                else:
                    source[key] = _dump_dict(value, tomlkit.table(),
                        source_path=source_path + [key])
            else:
                source[key] = value
        return source
    return tomlkit.dumps(_dump_dict(dictionary, tomlkit.document()))