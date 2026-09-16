def run(self):
    sha = VersionUtils.run_git_command(['rev-parse', 'HEAD'], self.git_dir)
    tag = self.distribution.get_version()
    if self.has_tag(tag, sha):
        tags_sha = VersionUtils.run_git_command(['rev-parse', tag], self.
            git_dir)
        if sha != tags_sha:
            logger.error(
                'git tag {0} sha does not match the sha requesting to be tagged, you need to increment the version number, Skipped Tagging!'
                .format(tag))
            return
        else:
            logger.info(
                'git tag {0} already exists for this repo, Skipped Tagging!'
                .format(tag))
            return
    logger.info('Adding tag {0} for commit {1}'.format(tag, sha))
    if not self.dry_run:
        VersionUtils.run_git_command(['tag', '-m', '""', tag, sha], self.
            git_dir, throw_on_error=True)
        logger.info('Pushing tag {0} to remote {1}'.format(tag, self.remote))
        VersionUtils.run_git_command(['push', self.remote, tag], self.
            git_dir, throw_on_error=True)