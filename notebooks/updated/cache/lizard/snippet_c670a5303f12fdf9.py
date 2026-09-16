def tag_patches_branch(package, local_patches_branch, patches_branch, force
    =False, push=False):
    vr = specfile.Spec().get_vr(epoch=False)
    nvr_tag = package + '-' + vr
    tag_cmd = ['tag', nvr_tag, local_patches_branch]
    if force:
        tag_cmd.append('-f')
    git(*tag_cmd)
    if push:
        patches_remote = patches_branch.partition('/')[0]
        git('push', patches_remote, nvr_tag)
    else:
        print('Not pushing tag. Run "git push patches %s" by hand.' % nvr_tag)