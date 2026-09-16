def _make_local_question_images(self, question_dict):
    question_dict = question_dict.copy()
    dest_path = 'exerciseimages/'
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    def _process_string(string):
        image_regex = re.compile(MARKDOWN_IMAGE_REGEX, flags=re.IGNORECASE)
        contentstorage_prefix = '${☣ CONTENTSTORAGE}/'
        studio_storage = 'https://studio.learningequality.org/content/storage/'
        matches = image_regex.findall(string)
        for match in matches:
            file_result = match[1]
            file_name = file_result.replace(contentstorage_prefix, '')
            file_url = studio_storage + file_name[0] + '/' + file_name[1
                ] + '/' + file_name
            file_local_path = os.path.join(dest_path, file_name)
            response = requests.get(file_url)
            if response.status_code != 200:
                print('Failed for image ' + str(response.status_code) +
                    ' >> ' + file_url)
                return string
            with open(file_local_path, 'wb') as local_file:
                local_file.write(response.content)
                print('saved image file', file_local_path)
            string = string.replace(file_result, file_local_path)
        return string
    new_question = _process_string(question_dict['question'])
    question_dict['question'] = new_question
    answers = json.loads(question_dict['answers'])
    new_answers = []
    for ans in answers:
        new_ans = ans.copy()
        new_ans['answer'] = _process_string(new_ans['answer'])
        new_answers.append(new_ans)
    question_dict['answers'] = json.dumps(new_answers)
    return question_dict