def get_subdomain_history_neighbors(self, cursor, subdomain_rec):
    hist = self.subdomain_db.get_subdomain_history(subdomain_rec.get_fqn(),
        include_unaccepted=True, start_sequence=subdomain_rec.n - 1,
        end_sequence=subdomain_rec.n, cur=cursor)
    hist.sort(lambda h1, h2: -1 if h1.n < h2.n or h1.n == h2.n and h1.
        parent_zonefile_index < h2.parent_zonefile_index else 0 if h1.n ==
        h2.n and h1.parent_zonefile_index == h2.parent_zonefile_index else 1)
    fut = self.subdomain_db.get_subdomain_history(subdomain_rec.get_fqn(),
        include_unaccepted=True, start_sequence=subdomain_rec.n,
        end_sequence=subdomain_rec.n + 2, cur=cursor)
    fut.sort(lambda h1, h2: -1 if h1.n < h2.n or h1.n == h2.n and h1.
        parent_zonefile_index < h2.parent_zonefile_index else 0 if h1.n ==
        h2.n and h1.parent_zonefile_index == h2.parent_zonefile_index else 1)
    cur = []
    tmp_fut = []
    for f in fut:
        if f.n == subdomain_rec.n:
            cur.append(f)
        else:
            tmp_fut.append(f)
    fut = tmp_fut
    ret = {'prev': hist, 'cur': cur, 'fut': fut}
    return ret