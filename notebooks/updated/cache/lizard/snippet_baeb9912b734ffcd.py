def getLayerName(url):
    urlInfo = None
    urlSplit = None
    try:
        urlInfo = urlparse.urlparse(url)
        urlSplit = str(urlInfo.path).split('/')
        name = urlSplit[len(urlSplit) - 3]
        return name
    except:
        return url
    finally:
        urlInfo = None
        urlSplit = None
        del urlInfo
        del urlSplit
        gc.collect()