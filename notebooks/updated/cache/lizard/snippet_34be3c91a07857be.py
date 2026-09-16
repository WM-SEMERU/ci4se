def prioSort(elements):
    random.shuffle(elements)
    sorted_elems = sorted(elements, key=getPriority)
    return sorted_elems