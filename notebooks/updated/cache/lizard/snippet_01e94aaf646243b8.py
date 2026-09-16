def metabolite_id_check(metabolites, errors, columns, row_number):
    message = (
        "Metabolite '{value}' in column {col} and row {row} does not appear in the metabolic model."
        )
    for column in columns:
        if 'metabolite' in column['header'] and column['value'
            ] not in metabolites:
            message = message.format(value=column['value'], row=row_number,
                col=column['number'])
            errors.append({'code': 'bad-value', 'message': message,
                'row-number': row_number, 'column-number': column['number']})