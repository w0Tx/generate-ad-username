"""
This script is based on the following naming convention :

NameSurname
Name.Surname
NamSur (3letters of each)
Nam.Sur
NSurname
N.Surname
SurnameName
Surname.Name
SurnameN
Surname.N
3 random letters and 3 random numbers (abc123) --> This one is not implemented

https://book.hacktricks.wiki/en/windows-hardening/active-directory-methodology/index.html#recon-active-directory-no-credssessions
"""

import csv
import argparse

parser = argparse.ArgumentParser(description='Generate AD username based on Name and Surname')
parser.add_argument('csvfilename', metavar="CSVFile", type=str, help='CSV File containing list of users')
args = parser.parse_args()

def opencsv(csvfilename):
    dict = []
    with open(csvfilename, 'r', encoding='utf-8-sig') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
        	dict.append([row[0],row[1]])
    return dict

def main():
	dict = opencsv(args.csvfilename)
	for row in dict:
		name = row[0].lower()
		surname = row[1].lower()
		#NameSurname
		print(name + surname)
		#Name.Surname
		print(name + "-" + surname)
		#Name-Surname
		print(name + "." + surname)
		#NamSur
		print(name[0:3] + surname[0:3])
		#Nam-Sur
		print(name[0:3] + "-" + surname[0:3])
		#Nam.Sur
		print(name[0:3] + "." + surname[0:3])
		#NSurname
		print(name[0] + surname)
		#N-Surname
		print(name[0] + "-" + surname)
		#N.Surname
		print(name[0] + "." + surname)
		#SurnameName
		print(surname + name)
		#Surname-Name
		print(surname + "-" + name)
		#Surname.Name
		print(surname + "." + name)
		#SurNam
		print(surname[0:3] + name[0:3])
		#Sur-Nam
		print(surname[0:3] + "-" + name[0:3])
		#Sur.Nam
		print(surname[0:3] + "." + name[0:3])
		#Sname
		print(surname[0] + name)
		#S-name
		print(surname[0] + "-" + name)
		#S.name
		print(surname[0] + "." + name)
		#SurnameN
		print(surname + name[0])
		#Surname-N
		print(surname + "-" + name[0])
		#Surname.N
		print(surname + "." + name[0])

if __name__ == "__main__":
    main()
