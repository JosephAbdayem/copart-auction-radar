from modules.analysis import convert_to_numeric


class VehicleFilter:
    """Class to apply filters on vehicles."""

    def __init__(self, data):
        self.original_data = data.copy()
        self.filtered_data = data.copy()

    def reset_filters(self):
        """Restores the data to its original state."""
        self.filtered_data = self.original_data.copy()

    def filter_by_year(self, min_year):
        """Filters vehicles by minimum model year."""
        self.filtered_data = self.filtered_data[self.filtered_data['Ano Modelo'] >= min_year]
        return self

    def filter_by_fipe_percentage(self, percentage):
        """Filters vehicles based on a minimum FIPE discount percentage."""
        self.filtered_data['Valor FIPE'] = self.filtered_data['Valor FIPE'].apply(
            convert_to_numeric)
        self.filtered_data['Lance atual'] = self.filtered_data['Lance atual'].apply(
            convert_to_numeric)
        self.filtered_data = self.filtered_data.dropna(
            subset=['Valor FIPE', 'Lance atual'])

        self.filtered_data['DiferencaPercentual'] = (
            (self.filtered_data['Valor FIPE'] - self.filtered_data['Lance atual']) / self.filtered_data['Valor FIPE']) * 100

        self.filtered_data = self.filtered_data[self.filtered_data['DiferencaPercentual'] > percentage]
        return self

    def apply_filters(self):
        """Returns the filtered dataset."""
        return self.filtered_data
