def create_tables(args):
    from bob.db.utils import create_engine_try_nolock
    engine = create_engine_try_nolock(args.type, args.files[0], echo=args.
        verbose > 2)
    Base.metadata.create_all(engine)