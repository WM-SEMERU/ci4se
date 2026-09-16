def update_instruction(bet_id, new_persistence_type):
    args = locals()
    return {to_camel_case(k): v for k, v in args.items() if v is not None}