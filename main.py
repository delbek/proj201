from DataLoader import DataLoader
from DataAnalyzer import DataAnalyzer
from Printer import Printer


def main():
    districts_2014, ballot_boxes_2014, neighbourhoods_2014 = DataLoader.load_data("/Users/denizelbek/Desktop/proj201/2014_data")

    da_2014 = DataAnalyzer(districts_2014, ballot_boxes_2014, neighbourhoods_2014)

    printer = Printer(82, 10)
    printer.print_districts(da_2014.get_districts_by_margin_of_error(100))

main()
