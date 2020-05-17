import csv

def modeltocsv(objects, fields):

    filename = "data.csv"
    

    for obj in objects:
        row = []
        for field in fields:
            row.append(getattr(obj, str(field), 'null'))
        
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(row)