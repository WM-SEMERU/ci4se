def replace(pretty, old_str, new_str):
    out_str = ''
    line_number = 1
    changes = 0
    for line in pretty.splitlines(keepends=True):
        new_line = line.replace(old_str, new_str)
        if line.find(old_str) != -1:
            logging.debug('%s', line_number)
            logging.debug('< %s', line)
            logging.debug('> %s', new_line)
            changes += 1
        out_str += new_line
        line_number += 1
    logging.info('Total changes(%s): %s', old_str, changes)
    return out_str