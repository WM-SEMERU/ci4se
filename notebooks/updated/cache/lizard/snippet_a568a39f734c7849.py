def _get_targets_by_declared_platform_with_placeholders(self,
    targets_by_platform):
    if not targets_by_platform:
        for platform in self._python_setup.platforms:
            targets_by_platform[platform] = [
                '(No target) Platform inherited from either the --platforms option or a pants.ini file.'
                ]
    return targets_by_platform