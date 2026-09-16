def get_dir(self, path):
    try:
        longest = max(m for m in self.mounts if path.startswith(m))
        return self.mounts[longest]
    except ValueError:
        return None