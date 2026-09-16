def create_tag(note_store, new_tag):
    try:
        return note_store.createTag(new_tag).guid
    except EDAMUserException as e:
        if e.errorCode == EDAMErrorCode.DATA_CONFLICT:
            logger.info('Evernote Data Conflict Err {0}'.format(e))
        elif e.errorCode == EDAMErrorCode.BAD_DATA_FORMAT:
            logger.critical('Evernote Err {0}'.format(e))
        return False