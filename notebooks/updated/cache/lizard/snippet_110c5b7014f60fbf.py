def transaction(commit=True):
    try:
        yield SessionContext.session
        if commit:
            SessionContext.session.commit()
    except Exception:
        if SessionContext.session:
            SessionContext.session.rollback()
        raise