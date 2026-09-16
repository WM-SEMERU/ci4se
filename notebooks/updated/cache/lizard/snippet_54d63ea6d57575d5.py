def _render_content(self, content, **settings):
    result = []
    bars = settings[self.SETTING_BARS]
    label_width = self.chart_measure(bars)
    if not settings[self.SETTING_BAR_WIDTH]:
        settings[self.SETTING_BAR_WIDTH] = TERMINAL_WIDTH - label_width - 3
    max_value = max(content)
    i = 0
    for bar in content:
        result.append(self._render_bar(bars[i], bar, max_value, label_width,
            **settings))
        i += 1
    return result