import csv

def modeltocsv(objects, fields):

    filename = "data.csv"
    

    for obj in objects:
        row = []
        for field in fields:
            row.append(getattr(obj, str(field), 'null'))
        
        with open(filename, 'a') as csvfile:# a for append, and every value null check field name!
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(row)