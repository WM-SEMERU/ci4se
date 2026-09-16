def make_github_markdown_writer(opts):
    assert hasattr(opts, 'wrapper_regex')
    atx = MarkdownATXWriterStrategy(opts, 'ATX headers')
    setext = MarkdownSetextWriterStrategy(opts, 'Setext headers')
    inline = MarkdownInlineLinkWriterStrategy(opts, 'inline links')
    ref = MarkdownReferenceLinkWriterStrategy(opts, 'reference links')
    code_block_switch = ghswitches.code_block_switch
    strategies = [atx, setext, inline, ref]
    switches = [code_block_switch]
    return Writer(strategies, switches=switches)