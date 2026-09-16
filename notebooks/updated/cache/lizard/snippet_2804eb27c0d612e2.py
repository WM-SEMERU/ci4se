def write_classdesc(self, obj, parent=None):
    if obj not in self.references:
        self.references.append(obj)
        logging.debug('*** Adding ref 0x%X for classdesc %s', len(self.
            references) - 1 + self.BASE_REFERENCE_IDX, obj.name)
        self._writeStruct('>B', 1, (self.TC_CLASSDESC,))
        self._writeString(obj.name)
        self._writeStruct('>qB', 1, (obj.serialVersionUID, obj.flags))
        self._writeStruct('>H', 1, (len(obj.fields_names),))
        for field_name, field_type in zip(obj.fields_names, obj.fields_types):
            self._writeStruct('>B', 1, (self._convert_type_to_char(
                field_type),))
            self._writeString(field_name)
            if field_type[0] in (self.TYPE_OBJECT, self.TYPE_ARRAY):
                try:
                    idx = self.references.index(field_type)
                except ValueError:
                    self.references.append(field_type)
                    logging.debug('*** Adding ref 0x%X for field type %s', 
                        len(self.references) - 1 + self.BASE_REFERENCE_IDX,
                        field_type)
                    self.write_string(field_type, False)
                else:
                    logging.debug('*** Reusing ref 0x%X for %s (%s)', idx +
                        self.BASE_REFERENCE_IDX, field_type, field_name)
                    self.write_reference(idx)
        self._writeStruct('>B', 1, (self.TC_ENDBLOCKDATA,))
        if obj.superclass:
            self.write_classdesc(obj.superclass)
        else:
            self.write_null()
    else:
        self.write_reference(self.references.index(obj))