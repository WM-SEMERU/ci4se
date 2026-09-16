def XOR(classical_reg1, classical_reg2):
    left, right = unpack_reg_val_pair(classical_reg1, classical_reg2)
    return ClassicalExclusiveOr(left, right)