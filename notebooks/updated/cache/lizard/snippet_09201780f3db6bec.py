def write_document(self, gh_user, doc_id, file_content, branch, author,
    commit_msg=None):
    parent_sha = None
    fc = tempfile.NamedTemporaryFile()
    if is_str_type(file_content):
        fc.write(file_content)
    else:
        write_as_json(file_content, fc)
    fc.flush()
    try:
        doc_filepath = self.path_for_doc(doc_id)
        doc_dir = os.path.split(doc_filepath)[0]
        if parent_sha is None:
            self.checkout_master()
            parent_sha = self.get_master_sha()
        branch = self.create_or_checkout_branch(gh_user, doc_id, parent_sha,
            force_branch_name=True)
        if not os.path.isdir(doc_dir):
            os.makedirs(doc_dir)
        shutil.copy(fc.name, doc_filepath)
        git(self.gitdir, self.gitwd, 'add', doc_filepath)
        if commit_msg is None:
            commit_msg = "Update document '%s' via OpenTree API" % doc_id
        try:
            git(self.gitdir, self.gitwd, 'commit', author=author, message=
                commit_msg)
        except Exception as e:
            if 'nothing to commit' in e.message:
                pass
            else:
                _LOG.exception('"git commit" failed')
                self.reset_hard()
                raise
        new_sha = git(self.gitdir, self.gitwd, 'rev-parse', 'HEAD')
    except Exception as e:
        _LOG.exception('write_document exception')
        raise GitWorkflowError(
            'Could not write to document #%s ! Details: \n%s' % (doc_id, e.
            message))
    finally:
        fc.close()
    return new_sha