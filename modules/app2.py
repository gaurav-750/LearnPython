from pathlib import Path
from zipfile import ZipFile

#! Opening zip file in write mode:
# zip = ZipFile("files.zip", "w")
# for path in Path("ecommerce").rglob("*.*"):
#     # print(path.name)
#     zip.write(path)

# zip.close()


#! In read mode
# zip = ZipFile("files.zip")
# print(zip.namelist())

# info = zip.getinfo('ecommerce/__init__.py')
# print('info:', info)
# print(info.file_size)

# * to extract the zip:
# just provide the folder where it is to be extracted
# zip.extractall("extract")


#! Working with csv files:
import csv

# * Write into csv file:
# with open("data.csv", "w") as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(["t_id", "prod_id", "price"])
#     writer.writerow([1, 1, 1100])
#     writer.writerow([2, 2, 500])
#     writer.writerow([3, 3, 1200])
#     writer.writerow([4, 2, 1010])


# * Read from the csv file:
with open("data.csv") as csvFile:
    reader = csv.reader(csvFile)
    # print(reader)
    # print(list(reader))

    for row in reader:
        print(row)

    # line_count = 0
    # for row in reader:
    #     if line_count == 0:
    #         print('Column names are', row)
    #         line_count += 1
    #     else:
    #         print(row)
