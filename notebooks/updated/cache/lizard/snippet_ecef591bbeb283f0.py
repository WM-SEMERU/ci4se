def _get_completions_for_match(self, match, complete_event):
    for match_variable in match.end_nodes():
        varname = match_variable.varname
        start = match_variable.start
        completer = self.completers.get(varname)
        if completer:
            text = match_variable.value
            unwrapped_text = self.compiled_grammar.unescape(varname, text)
            document = Document(unwrapped_text, len(unwrapped_text))
            for completion in completer.get_completions(document,
                complete_event):
                new_text = unwrapped_text[:len(text) + completion.
                    start_position] + completion.text
                yield Completion(text=self.compiled_grammar.escape(varname,
                    new_text), start_position=start - len(match.string),
                    display=completion.display, display_meta=completion.
                    display_meta)