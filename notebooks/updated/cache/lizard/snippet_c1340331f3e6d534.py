def blockstack_backup_restore(working_dir, block_number):
    db = BlockstackDB.get_readwrite_instance(working_dir, restore=True,
        restore_block_height=block_number)
    try:
        db.db_restore(block_number=block_number)
    except Exception as e:
        raise e
    finally:
        db.close()
    return True