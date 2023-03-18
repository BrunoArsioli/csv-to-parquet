# csv-to-parquet.py
Python Package to convert .csv files to .parquet. Improve storage efficiency of large .csv files

This Python package converts .csv files to .parquet files using the astropy and pandas libraries. The resulting .parquet files are compressed and can be read faster than uncompressed .csv files, and take much less physical memory to store. 

Installation
To use this package, you will need to have Python 3.7 or higher installed. You will also need to install the following libraries:

```
astropy
pandas
```
You can install these libraries using pip. Open a terminal or command prompt and type the following commands:

```
pip install astropy
pip install pandas
pip install git+https://github.com/BrunoArsioli/csv-to-parquet.py.git
#Import my gitbhu libraries
from csv_to_parquet.csv_to_parquet import csv_to_parquet
```

Or, in Google Colab

```
!pip install astropy
!pip install pandas
#Import the csv_to_parquet gitbhu libraries
!pip install git+https://github.com/BrunoArsioli/csv-to-parquet.py.git
```

Usage
To use this package, simply call the csv_to_parquet function and pass in the path to the .csv file:

```
python
from csv_to_parquet.csv_to_parquet import csv_to_parquet

# convert a .csv file to a .parquet file
csv_to_parquet('path/to/csv/file.csv')
```

The resulting .parquet file will be saved in the same directory as the input .csv file.

Examples
Here are some examples of how to use this script:

python
Copy code
# convert a single .csv file to a .parquet file
csv_to_parquet('path/to/csv/file.csv')

# convert multiple .csv files to .parquet files
csv_list = ['path/to/csv/file1.csv', 'path/to/csv/file2.csv', 'path/to/csv/file3.csv']
for csv_file in csv_list:
    csv_to_parquet(csv_file)
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
This script was developed by Bruno Arsioli.
