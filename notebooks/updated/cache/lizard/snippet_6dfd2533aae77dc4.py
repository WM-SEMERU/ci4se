def cut_from_block(html_message):
    block = html_message.xpath(
        "//*[starts-with(mg:text_content(), 'From:')]|//*[starts-with(mg:text_content(), 'Date:')]"
        )
    if block:
        block = block[-1]
        parent_div = None
        while block.getparent() is not None:
            if block.tag == 'div':
                parent_div = block
                break
            block = block.getparent()
        if parent_div is not None:
            maybe_body = parent_div.getparent()
            parent_div_is_all_content = (maybe_body is not None and 
                maybe_body.tag == 'body' and len(maybe_body.getchildren()) == 1
                )
            if not parent_div_is_all_content:
                parent = block.getparent()
                next_sibling = block.getnext()
                while next_sibling is not None:
                    parent.remove(block)
                    block = next_sibling
                    next_sibling = block.getnext()
                if block is not None:
                    parent.remove(block)
                return True
        else:
            return False
    block = html_message.xpath(
        "//*[starts-with(mg:tail(), 'From:')]|//*[starts-with(mg:tail(), 'Date:')]"
        )
    if block:
        block = block[0]
        if RE_FWD.match(block.getparent().text or ''):
            return False
        while block.getnext() is not None:
            block.getparent().remove(block.getnext())
        block.getparent().remove(block)
        return True