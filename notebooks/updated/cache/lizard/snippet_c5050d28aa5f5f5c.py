def _classify(self, gadget, classifier, gadget_type, iters):
    instrs = [ir_instr for asm_instr in gadget.instrs for ir_instr in
        asm_instr.ir_instrs]
    results = []
    for _ in range(iters):
        self._ir_emulator.reset()
        regs_initial = self._init_regs_random()
        try:
            regs_final, mem_final = self._ir_emulator.execute_lite(instrs,
                regs_initial)
        except:
            results += [([], [])]
            continue
        regs_initial_full = self._compute_full_context(regs_initial)
        regs_final_full = self._compute_full_context(regs_final)
        regs_written = self._ir_emulator.written_registers
        regs_read = self._ir_emulator.read_registers
        mod_regs = self._compute_mod_regs(regs_initial_full, regs_final_full)
        matches = classifier(regs_initial_full, regs_final_full, mem_final,
            regs_written, regs_read)
        results += [(matches, mod_regs)]
    candidates, mod_regs = self._analyze_execution_results(results)
    classified = self._create_typed_gadgets(gadget, candidates, mod_regs,
        gadget_type)
    return classified