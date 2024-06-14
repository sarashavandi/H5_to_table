import os
import h5py
import pandas as pd

def h5_to_dataframe(h5_file_path):
    """
    Convert all datasets in an HDF5 file to a dictionary of Pandas DataFrames.

    This function reads an HDF5 file and converts each dataset into a Pandas DataFrame.
    The resulting DataFrames are stored in a dictionary where the keys are the dataset paths
    and the values are the corresponding DataFrames.

    Args:
        h5_file_path (str): Path to the HDF5 file.

    Returns:
        dict: A dictionary where keys are dataset paths (str) and values are Pandas DataFrames.
        
    Raises:
        OSError: If the file cannot be opened.
        KeyError: If there is an issue accessing a dataset.
        Exception: For any other issues encountered during dataset reading.

    Example:
        >>> dfs = h5_to_dataframe('path_to_your_file.h5')
        >>> for path, df in dfs.items():
        >>>     print(f"Dataset {path} has shape {df.shape}")
    """
    dataframes = {}

    try:
        with h5py.File(h5_file_path, 'r') as h5file:
            def extract_dataset(name, obj):
                if isinstance(obj, h5py.Dataset):
                    try:
                        data = obj[()]
                        if data.ndim == 1:
                            df = pd.DataFrame(data, columns=[name.split('/')[-1]])
                        elif data.ndim == 2:
                            df = pd.DataFrame(data)
                        else:
                            df = pd.DataFrame(data.reshape(-1, data.shape[-1]))
                        dataframes[name] = df
                    except Exception as e:
                        print(f"Failed to read dataset {name}: {e}")

            h5file.visititems(extract_dataset)
    except OSError as e:
        print(f"Error opening file: {e}")
        raise
    except KeyError as e:
        print(f"Dataset path error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

    return dataframes