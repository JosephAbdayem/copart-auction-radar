import pandas as pd


def open_csv(path):
    """Opens a CSV file and returns a DataFrame."""
    try:
        return pd.read_csv(path, sep=';')
    except Exception as e:
        print(f"Error opening the file: {e}")
        return None


def save_csv(data, path):
    """Saves a DataFrame as a CSV file."""
    data.to_csv(path, index=False)
    print(f"File saved at: {path}")
