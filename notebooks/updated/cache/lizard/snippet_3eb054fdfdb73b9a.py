def getNumDownloads(self, fileInfo):
    downloads = fileInfo[fileInfo.find('FILE INFORMATION'):]
    if -1 != fileInfo.find('not included in ranking'):
        return '0'
    downloads = downloads[:downloads.find('.<BR>')]
    downloads = downloads[downloads.find('</A> with ') + len('</A> with '):]
    return downloads