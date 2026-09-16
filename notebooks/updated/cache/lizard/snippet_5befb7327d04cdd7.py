def WritePathInfos(self, client_id, path_infos):
    try:
        self._MultiWritePathInfos({client_id: path_infos})
    except MySQLdb.IntegrityError as error:
        raise db.UnknownClientError(client_id=client_id, cause=error)