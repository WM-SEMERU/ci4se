def invisible_canvas():
    with preserve_current_canvas():
        with preserve_batch_state():
            ROOT.gROOT.SetBatch()
            c = ROOT.TCanvas()
        try:
            c.cd()
            yield c
        finally:
            c.Close()
            c.IsA().Destructor(c)