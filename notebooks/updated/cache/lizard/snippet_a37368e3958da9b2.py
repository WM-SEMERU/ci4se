def managed_reader(reader, catalog=None):
    if catalog is None:
        catalog = SymbolTableCatalog()
    ctx = _ManagedContext(catalog)
    symbol_trans = Transition(None, None)
    ion_event = None
    while True:
        if (symbol_trans.delegate is not None and ion_event is not None and
            not ion_event.event_type.is_stream_signal):
            delegate = symbol_trans.delegate
            symbol_trans = delegate.send(Transition(ion_event, delegate))
            if symbol_trans.delegate is None:
                ctx = symbol_trans.event
                data_event = NEXT_EVENT
            else:
                data_event = symbol_trans.event
        else:
            data_event = None
            if ion_event is not None:
                event_type = ion_event.event_type
                ion_type = ion_event.ion_type
                depth = ion_event.depth
                if depth == 0:
                    if event_type is IonEventType.VERSION_MARKER:
                        if ion_event != ION_VERSION_MARKER_EVENT:
                            raise IonException('Invalid IVM: %s' % (ion_event,)
                                )
                        ctx = _ManagedContext(ctx.catalog)
                        data_event = NEXT_EVENT
                    elif ion_type is IonType.SYMBOL and len(ion_event.
                        annotations
                        ) == 0 and ion_event.value is not None and ctx.resolve(
                        ion_event.value).text == TEXT_ION_1_0:
                        assert symbol_trans.delegate is None
                        data_event = NEXT_EVENT
                    elif event_type is IonEventType.CONTAINER_START and ion_type is IonType.STRUCT and ctx.has_symbol_table_annotation(
                        ion_event.annotations):
                        assert symbol_trans.delegate is None
                        delegate = _local_symbol_table_handler(ctx)
                        symbol_trans = Transition(None, delegate)
                        data_event = NEXT_EVENT
            if data_event is None:
                if ion_event is not None:
                    ion_event = _managed_thunk_event(ctx, ion_event)
                data_event = yield ion_event
        ion_event = reader.send(data_event)