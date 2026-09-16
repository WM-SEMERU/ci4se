def is_suspicious(pe):
    relocations_overlap_entry_point = False
    sequential_relocs = 0
    if hasattr(pe, 'DIRECTORY_ENTRY_BASERELOC'):
        for base_reloc in pe.DIRECTORY_ENTRY_BASERELOC:
            last_reloc_rva = None
            for reloc in base_reloc.entries:
                if (reloc.rva <= pe.OPTIONAL_HEADER.AddressOfEntryPoint <= 
                    reloc.rva + 4):
                    relocations_overlap_entry_point = True
                if (last_reloc_rva is not None and last_reloc_rva <= reloc.
                    rva <= last_reloc_rva + 4):
                    sequential_relocs += 1
                last_reloc_rva = reloc.rva
    warnings_while_parsing = False
    warnings = pe.get_warnings()
    if warnings:
        warnings_while_parsing
    pass