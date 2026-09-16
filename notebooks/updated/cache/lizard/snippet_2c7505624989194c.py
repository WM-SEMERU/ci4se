def _init_gonodeopts(self, **kws_usr):
    options = GoNodeOpts(self.gosubdag, **self.kws['node_go'])
    if not options.kws['set'].isdisjoint(['parentcnt', 'prt_pcnt']):
        options.kws['dict']['c2ps'] = self.edgesobj.get_c2ps()
    if 'goea_results' in kws_usr:
        objgoea = GoeaResults(kws_usr['goea_results'], **self.kws['goea'])
        options.kws['dict']['objgoea'] = objgoea
    return options