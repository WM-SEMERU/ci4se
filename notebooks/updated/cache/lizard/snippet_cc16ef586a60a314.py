def extractClips(self, specsFilePathOrStr, outputDir=None, zipOutput=False):
    clips = SpecsParser.parse(specsFilePathOrStr)
    if not outputDir:
        outputDir = os.path.abspath('.')
    zipFile = None
    if zipOutput:
        bname = os.path.splitext(os.path.basename(specsFilePathOrStr))[0]
        zipPath = '%s_clips.zip' % bname
        zipFile = zipfile.ZipFile(os.path.join(outputDir, zipPath), mode='w')
    for i, clip in enumerate(clips):
        filenameFormat = 'clip%%0%dd.mp3' % len(str(len(clips)))
        filepath = os.path.join(outputDir, filenameFormat % (i + 1))
        clipData = self._extractClipData(clip)
        with open(filepath, 'wb') as f_out:
            f_out.write(clipData)
        if zipFile:
            zipFile.write(filepath, arcname=os.path.basename(filepath))
            os.unlink(filepath)
    if zipFile:
        zipFile.close()