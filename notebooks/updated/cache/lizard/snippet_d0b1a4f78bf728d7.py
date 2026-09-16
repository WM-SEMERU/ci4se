def analyze(self, scratch, **kwargs):
    errors = Counter()
    for script in self.iter_scripts(scratch):
        prev_name, prev_depth, prev_block = '', 0, script.blocks[0]
        gen = self.iter_blocks(script.blocks)
        for name, depth, block in gen:
            if prev_depth == depth:
                if prev_name in self.SAY_THINK:
                    if name == 'play sound %s until done':
                        if not self.is_blank(prev_block.args[0]):
                            errors += self.check(gen)
                elif prev_name in self.SAY_THINK_DURATION and 'play sound %s' in name:
                    errors['1'] += 1
                elif prev_name == 'play sound %s':
                    if name in self.SAY_THINK:
                        errors[self.INCORRECT] += 1
                    elif name in self.SAY_THINK_DURATION:
                        if self.is_blank(block.args[0]):
                            errors[self.ERROR] += 1
                        else:
                            errors[self.HACKISH] += 1
                elif prev_name == 'play sound %s until done' and name in self.ALL_SAY_THINK:
                    if not self.is_blank(block.args[0]):
                        errors[self.INCORRECT] += 1
            prev_name, prev_depth, prev_block = name, depth, block
    return {'sound': errors}