def symmetrize(C):
    C_symm = {}
    for i, v in C.items():
        if i in C_symm_keys[0]:
            C_symm[i] = v.real
        elif i in C_symm_keys[1] + C_symm_keys[3]:
            C_symm[i] = v
        elif i in C_symm_keys[2]:
            C_symm[i] = symmetrize_2(C[i])
        elif i in C_symm_keys[4]:
            C_symm[i] = symmetrize_4(C[i])
        elif i in C_symm_keys[5]:
            C_symm[i] = symmetrize_5(C[i])
        elif i in C_symm_keys[6]:
            C_symm[i] = symmetrize_6(C[i])
        elif i in C_symm_keys[7]:
            C_symm[i] = symmetrize_7(C[i])
        elif i in C_symm_keys[8]:
            C_symm[i] = symmetrize_8(C[i])
        elif i in C_symm_keys[9]:
            C_symm[i] = symmetrize_9(C[i])
    return C_symm