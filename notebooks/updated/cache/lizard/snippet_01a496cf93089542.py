def markdown(self, dirPath=None):
    if dirPath:
        p = self._file_prefix()
        markdownSources = self.sourceResults.markdown(filepath=dirPath +
            '/' + p + 'sources.md')
        markdownPhot = self.photResults.markdown(filepath=dirPath + '/' + p +
            'phot.md')
        markdownSpec = self.specResults.markdown(filepath=dirPath + '/' + p +
            'spec.md')
        markdownFiles = self.relatedFilesResults.markdown(filepath=dirPath +
            '/' + p + 'relatedFiles.md')
    else:
        markdownSources = self.sourceResults.markdown()
        markdownPhot = self.photResults.markdown()
        markdownSpec = self.specResults.markdown()
        markdownFiles = self.relatedFilesResults.markdown()
    return markdownSources, markdownPhot, markdownSpec, markdownFiles