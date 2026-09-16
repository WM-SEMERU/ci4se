def count_characters(root, out):
    if os.path.isfile(root):
        with open(root, 'rb') as in_f:
            for line in in_f:
                for char in line:
                    if char not in out:
                        out[char] = 0
                    out[char] = out[char] + 1
    elif os.path.isdir(root):
        for filename in os.listdir(root):
            count_characters(os.path.join(root, filename), out)