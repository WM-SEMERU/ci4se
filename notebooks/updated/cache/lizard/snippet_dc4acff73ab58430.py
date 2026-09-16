def heading(self):
    if self._heading is None:
        self._heading = Heading()
    if not self._heading:
        if self.connection is None:
            raise DataJointError(
                'DataJoint class is missing a database connection. Missing schema decorator on the class? (e.g. @schema)'
                )
        else:
            self._heading.init_from_database(self.connection, self.database,
                self.table_name)
    return self._heading