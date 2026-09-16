def _es_margin(settings):
    return {k: settings[k] for k in (ConsoleWidget.SETTING_MARGIN,
        ConsoleWidget.SETTING_MARGIN_LEFT, ConsoleWidget.
        SETTING_MARGIN_RIGHT, ConsoleWidget.SETTING_MARGIN_CHAR)}