def close_on_esc_or_middlemouse(event, x, y, obj):
    if (event == ROOT.kButton2Down or event == ROOT.kMouseMotion and x == y ==
        0 and ROOT.gROOT.IsEscaped()):
        obj._py_closetimer = ROOT.TTimer()
        obj._py_closetimer.Connect('Timeout()', 'TCanvas', obj, 'Close()')
        obj._py_closetimer.Start(10, ROOT.kTRUE)