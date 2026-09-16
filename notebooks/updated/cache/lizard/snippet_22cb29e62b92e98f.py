def diropenbox(msg=None, title=None, default=None):
    if sys.platform == 'darwin':
        _bring_to_front()
    title = getFileDialogTitle(msg, title)
    localRoot = Tk()
    localRoot.withdraw()
    if not default:
        default = None
    f = tk_FileDialog.askdirectory(parent=localRoot, title=title,
        initialdir=default, initialfile=None)
    localRoot.destroy()
    if not f:
        return None
    return os.path.normpath(f)