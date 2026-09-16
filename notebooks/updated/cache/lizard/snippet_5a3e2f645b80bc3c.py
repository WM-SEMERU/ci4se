def __get_metrics(self):
    esfilters_merge = None
    esfilters_abandon = None
    esfilters_submit = None
    if self.esfilters:
        esfilters_merge = self.esfilters.copy()
        esfilters_abandon = self.esfilters.copy()
        esfilters_submit = self.esfilters.copy()
    merged = Merged(self.es_url, self.es_index, start=self.start, end=self.
        end, esfilters=esfilters_merge, interval=self.interval)
    merged.FIELD_DATE = 'closed'
    abandoned = Abandoned(self.es_url, self.es_index, start=self.start, end
        =self.end, esfilters=esfilters_abandon, interval=self.interval)
    abandoned.FIELD_DATE = 'closed'
    submitted = Submitted(self.es_url, self.es_index, start=self.start, end
        =self.end, esfilters=esfilters_submit, interval=self.interval)
    return merged, abandoned, submitted