def RCScan():
    res_re = (
        '^(?:\\s*#\\s*(?:include)|.*?\\s+(?:ICON|BITMAP|CURSOR|HTML|FONT|MESSAGETABLE|TYPELIB|REGISTRY|D3DFX)\\s*.*?)\\s*(<|"| )([^>"\\s]+)(?:[>"\\s])*$'
        )
    resScanner = SCons.Scanner.ClassicCPP('ResourceScanner', '$RCSUFFIXES',
        'CPPPATH', res_re, recursive=no_tlb)
    return resScanner