def construct_graph(args):
    app = Core(args)
    setup_root(app)
    if args['debug']:
        from circuits import Debugger
        hfoslog('Starting circuits debugger', lvl=warn, emitter='GRAPH')
        dbg = Debugger().register(app)
        dbg.IgnoreEvents.extend(['read', '_read', 'write', '_write',
            'stream_success', 'stream_complete', 'serial_packet',
            'raw_data', 'stream', 'navdatapush', 'referenceframe',
            'updateposition', 'updatesubscriptions', 'generatevesseldata',
            'generatenavdata', 'sensordata', 'reset_flood_offenders',
            'reset_flood_counters', 'task_success', 'task_done', 'keepalive'])
    hfoslog('Beginning graph assembly.', emitter='GRAPH')
    if args['drawgraph']:
        from circuits.tools import graph
        graph(app)
    if args['opengui']:
        import webbrowser
        webbrowser.open('http://%s:%i/' % (args['host'], args['port']))
    hfoslog('Graph assembly done.', emitter='GRAPH')
    return app