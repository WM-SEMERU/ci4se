def WriteEventBody(self, event):
    output_string = NativePythonFormatterHelper.GetFormattedEventObject(event)
    self._output_writer.Write(output_string)