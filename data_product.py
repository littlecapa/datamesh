import csv

class data_product:

    FILEPATH = "/Users/littlecapa/GIT/datascience/datamesh/data_folder/"

    def __init__(self):
        pass

    def register(self, productName, csvSchema, filepath = FILEPATH):

        filename = filepath + productName + '.csv'
        print(filename)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csvSchema)



