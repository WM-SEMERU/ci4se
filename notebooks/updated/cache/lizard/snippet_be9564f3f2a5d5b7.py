def do_memory(self, arg):
    if arg:
        raise CmdError('too many arguments')
    process = self.get_process_from_prefix()
    try:
        memoryMap = process.get_memory_map()
        mappedFilenames = process.get_mapped_filenames()
        print('')
        print(CrashDump.dump_memory_map(memoryMap, mappedFilenames))
    except WindowsError:
        msg = "can't get memory information for process (%d)"
        raise CmdError(msg % process.get_pid())