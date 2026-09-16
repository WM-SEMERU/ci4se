def merge_from_master(git_action, doc_id, auth_info, parent_sha,
    doctype_display_name='document'):
    gh_user = get_user_author(auth_info)[0]
    acquire_lock_raise(git_action, fail_msg=
        'Could not acquire lock to merge %s #%s' % (doctype_display_name,
        doc_id))
    try:
        git_action.checkout_master()
        written_fp = git_action.path_for_doc(doc_id)
        if os.path.exists(written_fp):
            master_file_blob_sha = git_action.get_blob_sha_for_file(written_fp)
        else:
            raise GitWorkflowError('{t} "{i}" does not exist on master'.
                format(t=doctype_display_name, i=doc_id))
        branch = git_action.create_or_checkout_branch(gh_user, doc_id,
            parent_sha)
        new_sha = git_action.merge('master', branch)
    finally:
        git_action.release_lock()
    return {'error': 0, 'resource_id': doc_id, 'branch_name': branch,
        'description': 'Updated %s #%s' % (doctype_display_name, doc_id),
        'sha': new_sha, 'merged_sha': master_file_blob_sha}