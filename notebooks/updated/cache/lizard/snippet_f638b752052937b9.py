def _get_search_text(self, cli):
    if self.preview_search(cli) and cli.buffers[self.search_buffer_name].text:
        return cli.buffers[self.search_buffer_name].text
    else:
        return self.get_search_state(cli).text