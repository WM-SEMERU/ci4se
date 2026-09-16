def step_impl06(context, count):
    fuzz_factor = 11
    context.fuzzed_string_list = fuzz_string(context.seed, count, fuzz_factor)