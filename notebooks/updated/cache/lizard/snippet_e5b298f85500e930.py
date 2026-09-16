def _generate_examples(self, filepath):
    logging.info('generating examples from = %s', filepath)
    with tf.io.gfile.GFile(filepath) as f:
        squad = json.load(f)
        for article in squad['data']:
            if 'title' in article:
                title = article['title'].strip()
            else:
                title = ''
            for paragraph in article['paragraphs']:
                context = paragraph['context'].strip()
                for qa in paragraph['qas']:
                    question = qa['question'].strip()
                    id_ = qa['id']
                    answer_starts = [answer['answer_start'] for answer in
                        qa['answers']]
                    answers = [answer['text'].strip() for answer in qa[
                        'answers']]
                    example = {'title': title, 'context': context,
                        'question': question, 'id': id_, 'answer_starts':
                        answer_starts, 'answers': answers}
                    yield {'question': example['question'], 'first_answer':
                        example['answers'][0], 'context': example['context']}