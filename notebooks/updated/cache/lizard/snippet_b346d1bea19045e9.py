def report(result_pickle_file_path, target_report_csv_path):
    import pandas as pd
    result_dict = pd.read_pickle(result_pickle_file_path)
    from .report import generate_report
    generate_report(result_dict, target_report_csv_path)