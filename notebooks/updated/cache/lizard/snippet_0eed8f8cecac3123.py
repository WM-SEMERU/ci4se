def partial_to_complete_sha_hex(self, partial_hexsha):
    try:
        hexsha, typename, size = self._git.get_object_header(partial_hexsha)
        return hex_to_bin(hexsha)
    except (GitCommandError, ValueError):
        raise BadObject(partial_hexsha)