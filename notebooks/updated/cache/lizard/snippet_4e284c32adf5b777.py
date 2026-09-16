def TreeCollectionStore(repos_dict=None, repos_par=None, with_caching=True,
    assumed_doc_version=None, git_ssh=None, pkey=None, git_action_class=
    TreeCollectionsGitAction, mirror_info=None,
    infrastructure_commit_author='OpenTree API <api@opentreeoflife.org>'):
    global _THE_TREE_COLLECTION_STORE
    if _THE_TREE_COLLECTION_STORE is None:
        _THE_TREE_COLLECTION_STORE = _TreeCollectionStore(repos_dict=
            repos_dict, repos_par=repos_par, with_caching=with_caching,
            assumed_doc_version=assumed_doc_version, git_ssh=git_ssh, pkey=
            pkey, git_action_class=git_action_class, mirror_info=
            mirror_info, infrastructure_commit_author=
            infrastructure_commit_author)
    return _THE_TREE_COLLECTION_STORE