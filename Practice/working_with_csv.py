import csv
import io

def csv_reader(file_obj):
	"""
	Read a csv file
	"""

	reader = csv.reader(file_obj)
	for row in reader:
		print(" ".join(row))

def csv_dict_reader(file_obj):
	"""
	Read a csv file using DictReader
	"""
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print("First name: " + line["first_name"])
		print("Last name: " + line["last_name"])

def csv_writer(data, path):
	"""
	Write csv data to a file path
	"""
	# open file in binary format for this fucking operating system :-)
	with open(path, "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for line in data:
			writer.writerow(line)


if __name__ == "__main__":
	# csv_path = r"F:\Github\Python\Practice\Files\data\MDR_RR_TB_burden_estimates_2016-12-04.csv"
	# with open(csv_path, "r") as f_obj:
	# 	csv_reader(f_obj)
	
	# csv_path = r"F:\Github\Python\Practice\Files\data\data.csv"
	# with open(csv_path, "r") as f_obj:
	# 	csv_dict_reader(f_obj)

	data = ["first_name,last_name,city".split(","),
			"Thang, Duong, Ngoc".split(","),
			"Duong, Ngoc, Thang".split(",")
	]
	path = r"F:\Github\Python\Practice\Files\data\output.csv"
	csv_writer(data, path)