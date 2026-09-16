def bourgain_embedding_matrix(distance_matrix):
    distance_matrix = np.array(distance_matrix)
    n = len(distance_matrix)
    if n == 1:
        return distance_matrix
    np.random.seed(123)
    distort_elements = []
    r = range(n)
    k = int(math.ceil(math.log(n) / math.log(2) - 1))
    t = int(math.ceil(math.log(n)))
    counter = 0
    for i in range(0, k + 1):
        for t in range(t):
            s = np.random.choice(r, 2 ** i)
            for j in r:
                d = min([distance_matrix[j][s] for s in s])
                counter += len(s)
                if i == 0 and t == 0:
                    distort_elements.append([d])
                else:
                    distort_elements[j].append(d)
    return rbf_kernel(distort_elements, distort_elements)