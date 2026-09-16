def switch(stage):
    stage = stage.lower()
    local('git pull')
    if stage in ['dev', 'devel', 'develop']:
        branch_name = 'develop'
    elif stage in ['qa', 'release']:
        branches = local('git branch -r', capture=True)
        possible_branches = []
        for b in branches.split('\n'):
            b_parts = b.split('/')
            if b_parts[1] == 'release':
                possible_branches.append(b_parts[2])
        if len(possible_branches) == 0:
            raise Exception(
                'No release branches found. Please create a new release first.'
                )
        possible_branches = sorted(possible_branches, reverse=True)
        branch_name = 'release/%s' % possible_branches[0]
    elif stage in ['production', 'master']:
        branch_name = 'master'
    else:
        raise NotImplemented
    local('git checkout %s' % branch_name)
    local('git pull')