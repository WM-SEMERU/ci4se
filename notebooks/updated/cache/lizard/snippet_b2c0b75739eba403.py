def GE(classical_reg1, classical_reg2, classical_reg3):
    classical_reg1, classical_reg2, classical_reg3 = prepare_ternary_operands(
        classical_reg1, classical_reg2, classical_reg3)
    return ClassicalGreaterEqual(classical_reg1, classical_reg2, classical_reg3
        )