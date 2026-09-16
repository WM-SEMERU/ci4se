def load_movies(data_home, size):
    all_genres = ['Action', 'Adventure', 'Animation', "Children's",
        'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
        'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
        'War', 'Western']
    n_genre = len(all_genres)
    movies = {}
    if size == '100k':
        with open(os.path.join(data_home, 'u.item'), encoding='ISO-8859-1'
            ) as f:
            lines = list(map(lambda l: l.rstrip().split('|'), f.readlines()))
        for line in lines:
            movie_vec = np.zeros(n_genre)
            for i, flg_chr in enumerate(line[-n_genre:]):
                if flg_chr == '1':
                    movie_vec[i] = 1.0
            movie_id = int(line[0])
            movies[movie_id] = movie_vec
    elif size == '1m':
        with open(os.path.join(data_home, 'movies.dat'), encoding='ISO-8859-1'
            ) as f:
            lines = list(map(lambda l: l.rstrip().split('::'), f.readlines()))
        for item_id_str, title, genres in lines:
            movie_vec = np.zeros(n_genre)
            for genre in genres.split('|'):
                i = all_genres.index(genre)
                movie_vec[i] = 1.0
            item_id = int(item_id_str)
            movies[item_id] = movie_vec
    return movies