def vsh(cmd, *args, **kw):
    args = '" "'.join(i.replace('"', '\\"') for i in args)
    easy.sh('"%s" "%s"' % (venv_bin(cmd), args))