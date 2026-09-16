def partition_scripts(scripts, start_type1, start_type2):
    match, other = [], []
    for script in scripts:
        if HairballPlugin.script_start_type(script
            ) == start_type1 or HairballPlugin.script_start_type(script
            ) == start_type2:
            match.append(script)
        else:
            other.append(script)
    return match, other