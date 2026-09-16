def _json_to_categories(response_body):
    data = json.loads(response_body)
    categories = []
    for category_data in data.get('categoryList', []):
        categories.append(Category().from_json(data.get('uwNetID'),
            category_data))
    return categories