def main(args=None):
    for arg in args:
        glyphsLib.dump(load(open(arg, 'r', encoding='utf-8')), sys.stdout)