def attachviewers(self, profiles):
    if self.metadata:
        template = None
        for profile in profiles:
            if isinstance(self, CLAMInputFile):
                for t in profile.input:
                    if self.metadata.inputtemplate == t.id:
                        template = t
                        break
            elif isinstance(self, CLAMOutputFile
                ) and self.metadata and self.metadata.provenance:
                for t in profile.outputtemplates():
                    if self.metadata.provenance.outputtemplate_id == t.id:
                        template = t
                        break
            else:
                raise NotImplementedError
            if template:
                break
        if template and template.viewers:
            for viewer in template.viewers:
                self.viewers.append(viewer)
        if template and template.converters:
            for converter in template.converters:
                self.converters.append(converter)