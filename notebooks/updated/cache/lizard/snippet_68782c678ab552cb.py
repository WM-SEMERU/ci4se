def PDFEmitter(target, source, env):

    def strip_suffixes(n):
        return not SCons.Util.splitext(str(n))[1] in ['.aux', '.log']
    source = [src for src in source if strip_suffixes(src)]
    return target, source