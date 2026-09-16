def __get_verb(counts):
    cursor = CONN.cursor()
    check_query = 'select verb_id from surverbs'
    cursor.execute(check_query)
    check_result = cursor.fetchall()
    id_list = []
    for row in check_result:
        id_list.append(row[0])
    rand = random.randint(1, counts['max_verb'])
    while rand not in id_list:
        rand = random.randint(1, counts['max_verb'])
    query = 'select * from surverbs where verb_id = {0}'.format(rand)
    cursor.execute(query)
    result = cursor.fetchone()
    return result[1]