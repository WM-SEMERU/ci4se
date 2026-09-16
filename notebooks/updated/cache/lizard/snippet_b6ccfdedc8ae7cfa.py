def main():
    listname = sys.argv[2]
    hostname = sys.argv[1]
    mlist = MailList.MailList(listname, lock=False)
    f = StringIO(sys.stdin.read())
    msg = email.message_from_file(f, Message.Message)
    h = HyperArch.HyperArchive(mlist)
    sequence = h.sequence
    h.processUnixMailbox(f)
    f.close()
    archive = h.archive
    msgno = '%06d' % sequence
    filename = msgno + '.html'
    filepath = os.path.join(h.basedir, archive, filename)
    h.close()
    url = '%s%s/%s' % (mlist.GetBaseArchiveURL(), archive, filename)
    ext_process(listname, hostname, url, filepath, msg)