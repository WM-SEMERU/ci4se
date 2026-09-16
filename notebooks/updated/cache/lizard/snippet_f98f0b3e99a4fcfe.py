def detect_language(self, text):
    infos_translate = TextDetectLanguageModel(text).to_dict()
    mode_translate = TranslatorMode.Detect.value
    return self._get_content(infos_translate, mode_translate)