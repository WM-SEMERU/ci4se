def next_instruction_is_function_or_class(lines):
    for i, line in enumerate(lines):
        if not line.strip():
            if i > 0 and not lines[i - 1].strip():
                return False
            continue
        if line.startswith('def ') or line.startswith('class '):
            return True
        if line.startswith(('#', '@', ' ')):
            continue
        return False
    return False