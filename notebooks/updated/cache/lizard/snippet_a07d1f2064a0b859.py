def load_file(self):
    daychunks = self.__split_file()
    if daychunks:
        maxcount = len(self.__splitpointers)
        for i in range(maxcount):
            start = self.__splitpointers[i]
            end = None
            if i < maxcount - 1:
                end = self.__splitpointers[i + 1]
            chunk = self.__get_chunk(start, end)
            parser = sarparse.Parser()
            cpu_usage, mem_usage, swp_usage, io_usage = parser._parse_file(
                parser._split_file(chunk))
            self.__sarinfos[self.__get_part_date(chunk)] = {'cpu':
                cpu_usage, 'mem': mem_usage, 'swap': swp_usage, 'io': io_usage}
            del cpu_usage
            del mem_usage
            del swp_usage
            del io_usage
            del parser
        return True