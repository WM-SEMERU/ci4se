def delete(name):
    with Session() as session:
        try:
            session.VFolder(name).delete()
            print_done('Deleted.')
        except Exception as e:
            print_error(e)
            sys.exit(1)