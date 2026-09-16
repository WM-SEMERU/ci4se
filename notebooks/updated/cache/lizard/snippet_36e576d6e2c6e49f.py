def view_global_gmfs(token, dstore):
    imtls = dstore['oqparam'].imtls
    row = dstore['gmf_data/data']['gmv'].mean(axis=0)
    return rst_table([row], header=imtls)