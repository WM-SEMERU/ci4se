def _process_element(self, pos, e):
    tag, class_attr = _tag_and_class_attr(e)
    start_of_message = (tag == 'div' and class_attr == 'message' and pos ==
        'start')
    end_of_thread = tag == 'div' and 'thread' in class_attr and pos == 'end'
    if start_of_message and not self.messages_started:
        self.messages_started = True
    elif tag == 'span' and pos == 'end':
        if 'user' in class_attr:
            self.current_sender = self.name_resolver.resolve(e.text)
        elif 'meta' in class_attr:
            self.current_timestamp = parse_timestamp(e.text, self.use_utc,
                self.timezone_hints)
    elif tag == 'p' and pos == 'end':
        if not self.current_text:
            self.current_text = e.text.strip() if e.text else ''
    elif tag == 'img' and pos == 'start':
        self.current_text = '(image reference: {})'.format(e.attrib['src'])
    elif (start_of_message or end_of_thread) and self.messages_started:
        if not self.current_timestamp:
            raise UnsuitableParserError
        if not self.current_sender:
            if not self.no_sender_warning_status:
                sys.stderr.write(
                    "\rWARNING: The sender was missing in one or more parsed messages. This is an error on Facebook's end that unfortunately cannot be recovered from. Some or all messages in the output may show the sender as 'Unknown' within each thread.\n"
                    )
                self.no_sender_warning_status = True
            self.current_sender = 'Unknown'
        cm = ChatMessage(timestamp=self.current_timestamp, sender=self.
            current_sender, content=self.current_text or '', seq_num=self.
            seq_num)
        self.messages += [cm]
        self.seq_num -= 1
        self.current_sender, self.current_timestamp, self.current_text = (
            None, None, None)
    return end_of_thread