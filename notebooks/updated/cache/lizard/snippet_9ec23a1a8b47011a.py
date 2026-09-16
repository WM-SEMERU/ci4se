def progress_bar_media():
    if PROGRESSBARUPLOAD_INCLUDE_JQUERY:
        js = ['http://code.jquery.com/jquery-1.8.3.min.js']
    else:
        js = []
    js.append('js/progress_bar.js')
    m = Media(js=js)
    return m.render()