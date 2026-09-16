def encode(input, output_filename):
    coder = rs.RSCoder(255, 223)
    output = []
    while True:
        block = input.read(223)
        if not block:
            break
        code = coder.encode_fast(block)
        output.append(code)
        sys.stderr.write('.')
    sys.stderr.write('\n')
    out = Image.new('L', (rowstride, len(output)))
    out.putdata(''.join(output))
    out.save(output_filename)