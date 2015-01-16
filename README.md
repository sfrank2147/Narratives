Narratives
==========
Usage instructions:

* Install the dependencies.  If you're using pip, you can just use the Requirements file that's in the repo.

* Create an excel spreadsheet with the same structure as sample_narratives.xlsx.  Note: the column headers must be EXACTLY the same, or the program will not parse it correctly

* Usage: python src/main.py path/to/excel_file.xlsx

* The program will output the narratives in a file "narratives.txt".  If that file already exists, it will be overwritten.