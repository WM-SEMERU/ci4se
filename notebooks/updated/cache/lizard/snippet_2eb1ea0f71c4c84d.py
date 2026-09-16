def create_assets_if_needed(corpus, path, entry):
    file_idx = entry[1]
    if file_idx not in corpus.utterances.keys():
        speaker_idx = entry[0]
        transcription = entry[2]
        age = CommonVoiceReader.map_age(entry[5])
        gender = CommonVoiceReader.map_gender(entry[6])
        file_path = os.path.join(path, 'clips', '{}.wav'.format(file_idx))
        corpus.new_file(file_path, file_idx)
        if speaker_idx in corpus.issuers.keys():
            issuer = corpus.issuers[speaker_idx]
        else:
            issuer = issuers.Speaker(speaker_idx, gender=gender, age_group=age)
            corpus.import_issuers(issuer)
        utterance = corpus.new_utterance(file_idx, file_idx, issuer.idx)
        utterance.set_label_list(annotations.LabelList.create_single(
            transcription, idx=audiomate.corpus.LL_WORD_TRANSCRIPT))
    return file_idx