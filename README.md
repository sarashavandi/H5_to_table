
H5_to_TABLE

Reading a H5 file and converting it to a table.

#Installation:
the default installation is using pip

pip install h5_to_table

you can also install from GitHub.
to do that, you need to clone the repo and then use pip locally

git clone https://github.com/sarashavandi/H5_to_table.git
cd h5_to_table
pip install .


#Usage:
Convert all datasets in an HDF5 file to a dictionary of Pandas DataFrames.
This function reads an HDF5 file and converts each dataset into a Pandas DataFrame.
The resulting DataFrames are stored in a dictionary where the keys are the dataset paths and the values are the corresponding DataFrames.

For more information, check out the documentation for h5_to_dataframe.


#Authors:
H5_To_TABLE Like a Boss-TEAM
