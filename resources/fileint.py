import csv

def extract_csv(dict_list, file_csv):
    '''
    extract results in csv
    '''
    with open(file_csv,'w') as FILE:
        f = csv.DictWriter(FILE, fieldnames = dict_list[0].keys())
        f.writeheader()
        f.writerows(dict_list)

def load_csv(file_csv):
    '''
    load a csv in nuar format - ready to create endpoint object
    '''
    with open(file_csv) as FILE:
        f = csv.DictReader(FILE)
        return [row for row in f]