def smudgeraw(target, offset, magicbytes):
    magicbytes = magicbytes.replace('\\x', '').decode('hex')
    _backup_bytes(target, offset, len(magicbytes))
    _smudge_bytes(target, offset, magicbytes)