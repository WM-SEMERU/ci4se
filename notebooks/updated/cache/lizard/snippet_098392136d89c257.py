def __buttonEvent(event):
    global boxRoot, __widgetTexts, __replyButtonText
    __replyButtonText = __widgetTexts[event.widget]
    boxRoot.quit()