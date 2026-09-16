def Main(url):
    web_scrape = WebScraping()
    document = web_scrape.scrape(url)
    nlp_base = NlpBase()
    nlp_base.tokenizable_doc = MeCabTokenizer()
    sentence_list = nlp_base.listup_sentence(document)
    batch_size = 10
    if len(sentence_list) < batch_size:
        raise ValueError('The number of extracted sentences is insufficient.')
    all_token_list = []
    for i in range(len(sentence_list)):
        nlp_base.tokenize(sentence_list[i])
        all_token_list.extend(nlp_base.token)
        sentence_list[i] = nlp_base.token
    vectorlizable_sentence = LSTMRTRBM()
    vectorlizable_sentence.learn(sentence_list=sentence_list,
        token_master_list=list(set(all_token_list)), hidden_neuron_count=
        1000, batch_size=batch_size, learning_rate=0.001, seq_len=5)
    test_list = sentence_list[:batch_size]
    feature_points_arr = vectorlizable_sentence.vectorize(test_list)
    print('Feature points (Top 5 sentences):')
    print(feature_points_arr)