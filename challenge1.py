import csv

with open('problem/sample_input.csv') as csvfile:
    for bond in csv.reader(csvfile):
        print bond
