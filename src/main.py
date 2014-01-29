import sys
import xlrd
import data_handling
from narratives import narrative
import argparse

def print_narratives(file_path):
    book = xlrd.open_workbook(file_path)
    sheet = book.sheet_by_index(0)
    data = data_handling.student_data(sheet)
    
    with open('narratives.txt','w') as output_file:
        for student in data:
            output_file.write('{}: '.format(student['name']) + '\n')
            output_file.write(narrative(student))
            output_file.write('\n\n')
    
def main():
    parser = argparse.ArgumentParser(description='Create narratives')
    parser.add_argument('path')
    args = parser.parse_args()
    
    print_narratives(args.path)

if __name__ == '__main__':
    main()