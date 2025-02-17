import pandas as pd


def convert_to_numeric(value):
    """Converts monetary values to numeric format."""
    value = value.replace('BRL', '').replace('.', '').replace(',', '.').strip()
    return pd.to_numeric(value, errors='coerce')


def analyze_opportunities(data):
    """Analyzes data and returns filtered opportunities."""
    if data.empty:
        return None
    return data
