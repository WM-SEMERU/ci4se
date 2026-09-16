def drive_enclosures(self):
    if not self.__drive_enclures:
        self.__drive_enclures = DriveEnclosures(self.__connection)
    return self.__drive_enclures