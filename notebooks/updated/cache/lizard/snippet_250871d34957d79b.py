def copy_region_to_clipboard(self):
    u
    if self.enable_win32_clipboard:
        mark = min(self.mark, len(self.line_buffer))
        cursor = min(self.point, len(self.line_buffer))
        if self.mark == -1:
            return
        begin = min(cursor, mark)
        end = max(cursor, mark)
        toclipboard = ''.join(self.line_buffer[begin:end])
        clipboard.SetClipboardText(toclipboard)