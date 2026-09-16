def process_block(self, block):
    ret = []
    output = None
    input_lines = None
    lineno = self.IP.execution_count
    input_prompt = self.promptin % lineno
    output_prompt = self.promptout % lineno
    image_file = None
    image_directive = None
    for token, data in block:
        if token == COMMENT:
            out_data = self.process_comment(data)
        elif token == INPUT:
            (out_data, input_lines, output, is_doctest, decorator,
                image_file, image_directive) = self.process_input(data,
                input_prompt, lineno)
        elif token == OUTPUT:
            out_data = self.process_output(data, output_prompt, input_lines,
                output, is_doctest, decorator, image_file)
        if out_data:
            ret.extend(out_data)
    if image_file is not None:
        self.save_image(image_file)
    return ret, image_directive