def print_header(self):
    lines_to_print = []
    lines_to_print.append('##fileformat=' + self.fileformat)
    if self.filedate:
        lines_to_print.append('##fileformat=' + self.fileformat)
    for filt in self.filter_dict:
        lines_to_print.append(self.filter_dict[filt])
    for form in self.format_dict:
        lines_to_print.append(self.format_dict[form])
    for info in self.info_dict:
        lines_to_print.append(self.info_dict[info])
    for contig in self.contig_dict:
        lines_to_print.append(self.contig_dict[contig])
    for alt in self.alt_dict:
        lines_to_print.append(self.alt_dict[alt])
    for other in self.other_dict:
        lines_to_print.append(self.other_dict[other])
    lines_to_print.append('#' + '\t'.join(self.header))
    return lines_to_print