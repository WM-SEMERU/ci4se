def update_branch(profile, name, sha):
    ref = 'heads/' + name
    data = refs.update_ref(profile, ref, sha)
    return data