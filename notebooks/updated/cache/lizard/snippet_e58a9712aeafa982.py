def validate(self, record, values):
    schema = record.schema()
    columns = self.columns()
    try:
        column_values = [values[col] for col in columns]
    except KeyError as err:
        msg = 'Missing {0} from {1}.{2} index'.format(err[0].name(), record
            .schema().name(), self.name())
        raise errors.InvalidIndexArguments(self.schema(), msg=msg)
    return True