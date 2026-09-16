def parse_prompts(etc_folder):
    prompts_path = os.path.join(etc_folder, 'PROMPTS')
    prompts_orig_path = os.path.join(etc_folder, 'prompts-original')
    prompts = textfile.read_key_value_lines(prompts_path, separator=' ')
    prompts_orig = textfile.read_key_value_lines(prompts_orig_path,
        separator=' ')
    prompts_key_fixed = {}
    for k, v in prompts.items():
        parts = k.split('/')
        key = k
        if len(parts) > 1:
            key = parts[-1]
        prompts_key_fixed[key] = v
    prompts = prompts_key_fixed
    return prompts, prompts_orig