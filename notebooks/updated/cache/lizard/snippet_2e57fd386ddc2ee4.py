def check_path_satisfiability(code_analyzer, path, start_address):
    start_instr_found = False
    sat = False
    for bb_curr, bb_next in zip(path[:-1], path[1:]):
        logger.info('BB @ {:#x}'.format(bb_curr.address))
        for instr in bb_curr:
            if not start_instr_found:
                if instr.address == start_address:
                    start_instr_found = True
                else:
                    continue
            logger.info('{:#x} {}'.format(instr.address, instr))
            for reil_instr in instr.ir_instrs:
                logger.info('{:#x} {:02d} {}'.format(reil_instr.address >> 
                    8, reil_instr.address & 255, reil_instr))
                if reil_instr.mnemonic == ReilMnemonic.JCC:
                    if instr.address + instr.size - 1 != bb_curr.end_address:
                        logger.error(
                            'Unexpected JCC instruction: {:#x} {} ({})'.
                            format(instr.address, instr, reil_instr))
                        continue
                    assert bb_curr.taken_branch == bb_next.address or bb_curr.not_taken_branch == bb_next.address or bb_curr.direct_branch == bb_next.address
                    if bb_curr.taken_branch == bb_next.address:
                        branch_var_goal = 1
                    elif bb_curr.not_taken_branch == bb_next.address:
                        branch_var_goal = 0
                    else:
                        continue
                    code_analyzer.add_constraint(code_analyzer.
                        get_operand_expr(reil_instr.operands[0]) ==
                        branch_var_goal)
                    break
                code_analyzer.add_instruction(reil_instr)
        sat = code_analyzer.check() == 'sat'
        logger.info('BB @ {:#x} sat? {}'.format(bb_curr.address, sat))
        if not sat:
            break
    return sat