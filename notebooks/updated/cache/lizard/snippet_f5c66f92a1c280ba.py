def highlight_line(self, payload):
    index_of_payload = self.target_line.lower().index(payload.lower())
    end_of_payload = index_of_payload + len(payload)
    self.target_line = '{}{}{}'.format(self.target_line[:index_of_payload],
        self.apply_highlight(self.target_line[index_of_payload:
        end_of_payload]), self.target_line[end_of_payload:])
    return self