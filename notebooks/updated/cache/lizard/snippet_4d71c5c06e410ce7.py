def calc_derivation(passphrase, salt):
    argonhash = argon2.low_level.hash_secret_raw(str.encode(passphrase),
        salt=salt, hash_len=32, time_cost=__argon2_timing_cost__,
        memory_cost=__argon2_memory_cost__, parallelism=
        __argon2_parallelism__, type=argon2.low_level.Type.I)
    return argonhash