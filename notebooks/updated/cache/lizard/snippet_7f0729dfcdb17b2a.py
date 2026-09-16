def _handle_negatives(numbers):
    min_number = min(filter(lambda x: type(x) == int, numbers))
    if min_number < 0:
        return [(x + abs(min_number) if type(x) == int else x) for x in numbers
            ]
    else:
        return numbers