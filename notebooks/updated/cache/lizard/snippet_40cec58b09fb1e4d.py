def formatWarnings(self, warnings):
    lines = []
    for modulename in sorted(warnings):
        lines.append(self.prefixModuleName + modulename)
        lines.extend(sorted(warnings[modulename], key=lambda x: x.split(':'
            )[1]))
    return '\n'.join(lines)