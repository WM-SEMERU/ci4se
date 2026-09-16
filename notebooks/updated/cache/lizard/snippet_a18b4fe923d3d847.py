def _move_file_with_sizecheck(tx_file, final_file):
    tmp_file = final_file + '.bcbiotmp'
    open(tmp_file, 'wb').close()
    want_size = utils.get_size(tx_file)
    shutil.move(tx_file, final_file)
    transfer_size = utils.get_size(final_file)
    assert want_size == transfer_size, 'distributed.transaction.file_transaction: File copy error: file or directory on temporary storage ({}) size {} bytes does not equal size of file or directory after transfer to shared storage ({}) size {} bytes'.format(
        tx_file, want_size, final_file, transfer_size)
    utils.remove_safe(tmp_file)