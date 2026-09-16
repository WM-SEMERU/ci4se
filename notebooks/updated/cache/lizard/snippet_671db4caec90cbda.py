def userBrowser(self, request, tag):
    f = LocalUserBrowserFragment(self.browser)
    f.docFactory = webtheme.getLoader(f.fragmentName)
    f.setFragmentParent(self)
    return f