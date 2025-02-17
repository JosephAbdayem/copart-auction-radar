from modules.file_handler import open_csv, save_csv
from modules.filters import VehicleFilter
from modules.analysis import analyze_opportunities


def request_input(message, input_type=int):
    """Requests user input and converts it to the specified type."""
    while True:
        try:
            return input_type(input(message))
        except ValueError:
            print("Invalid input. Please try again.")


def apply_filters(filter_obj):
    """Executes the filter application flow."""
    while True:
        print("\n===== FILTER MENU =====")
        print("1 - Filter by minimum vehicle year")
        print("2 - Filter by FIPE discount percentage")
        print("3 - Reset filters")
        print("4 - Apply analysis and save results")
        print("5 - Exit")
        option = request_input("Choose an option: ", str)

        if option == '1':
            year = request_input("Enter the minimum allowed vehicle year: ")
            filter_obj.filter_by_year(year)
            print("Filter successfully applied.")
        elif option == '2':
            percentage = request_input(
                "Enter the minimum FIPE discount percentage: ", float)
            filter_obj.filter_by_fipe_percentage(percentage)
            print("Filter successfully applied.")
        elif option == '3':
            filter_obj.reset_filters()
            print("Filters reset to original state.")
        elif option == '4':
            return filter_obj.apply_filters()
        elif option == '5':
            return None
        else:
            print("Invalid option. Please try again.")


def menu():
    """Interactive menu for users to apply filters and view opportunities."""
    path = input(
        "Enter the name of the CSV file inside the data/input/ folder: ")
    data = open_csv(f"data/input/{path}")

    if data is None:
        return

    filter_obj = VehicleFilter(data)
    filtered_data = apply_filters(filter_obj)

    if filtered_data is not None:
        opportunities = analyze_opportunities(filtered_data)
        output_path = "data/output/filtered.csv"
        save_csv(
            opportunities if opportunities is not None else filtered_data, output_path)
        print(f"File saved at {output_path}")
        if opportunities is None:
            print("No opportunities found, empty file saved.")
    else:
        print("Operation canceled by the user.")
