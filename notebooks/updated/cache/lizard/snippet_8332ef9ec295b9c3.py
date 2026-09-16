def update_qa(quietly=False):
    switch('dev')
    switch('qa')
    local('git merge --no-edit develop')
    local('git push')
    if not quietly:
        print(red('PLEASE DEPLOY CODE: fab deploy:all'))