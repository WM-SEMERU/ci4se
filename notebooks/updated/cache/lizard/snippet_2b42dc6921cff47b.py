def deepvalidation(self):
    if (self.doc and self.doc.deepvalidation and self.parent.set and self.
        parent.set[0] != '_'):
        try:
            self.doc.setdefinitions[self.parent.set].testsubclass(self.
                parent.cls, self.subset, self.cls)
        except KeyError as e:
            if self.parent.cls and not self.doc.allowadhocsets:
                raise DeepValidationError('Set definition ' + self.parent.
                    set + ' for ' + self.parent.XMLTAG +
                    ' not loaded (feature validation failed)!')
        except DeepValidationError as e:
            errormsg = str(e
                ) + ' (in set ' + self.parent.set + ' for ' + self.parent.XMLTAG
            if self.parent.id:
                errormsg += ' with ID ' + self.parent.id
            errormsg += ')'
            raise DeepValidationError(errormsg)