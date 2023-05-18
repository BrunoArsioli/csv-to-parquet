import os
import pandas 
import astropy
from astropy.table import Table

def csv_to_parquet(csv_path):
    """
    Converts a CSV file to a parquet file.
    Parameters
    ----------
    csv_path : str
        Path to the CSV file.
    Returns
    -------
    str
        Path to the parquet file.
    """
    
    # Check that the input file exists 
    if not os.path.isfile(csv_path):
        raise ValueError("Input file does not exist")    
    
    # read .csv to pandas dataframe
    try:
        datadf = pd.read_csv(f"{csv_path}")
    except ValueError:
        raise ValueError("Input file is not a valid .csv file.")  

    # define function to decode byte strings in the DataFrame
    def decode_bytes(value):
        return value.decode('utf-8') if isinstance(value, bytes) else value    
        
    # decode byte columns 
    datadf = datadf.applymap(decode_bytes)    
                
    # help user deal with exception in case input file is not .csv file.
    if not csv_path.endswith('.csv'):
        raise ValueError("Input file has wrong extension. Must be .csv")
        
    # remove extention from csv_path
    if csv_path.endswith('.csv'):
        parquet_path = csv_path.replace(".csv", ".parquet")

    # check if .parquet file already exist
    if os.path.isfile(parquet_path):
        raise ValueError("Output file already exists") 
        
    # df to .parquet
    datadf.to_parquet(f"{parquet_path}")

    return print(f".csv to .parquet is done! \n.parquet saved at: {parquet_path}")
