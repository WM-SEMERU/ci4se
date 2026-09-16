def translate_month_abbr(date_str, source_lang=DEFAULT_DATE_LANG,
    target_lang=DEFAULT_DATE_LANG):
    month_num, month_abbr = get_month_from_date_str(date_str, source_lang)
    with calendar.different_locale(LOCALES[target_lang]):
        translated_abbr = calendar.month_abbr[month_num]
        return re.sub(month_abbr, translated_abbr, date_str, flags=re.
            IGNORECASE)