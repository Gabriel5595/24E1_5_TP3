import pandas

def read_csv_files_pandas(file_name):
    file_information = pandas.read_csv(file_name)
    return file_information