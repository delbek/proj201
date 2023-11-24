from DataLoader import DataLoader
from DataAnalyzer import DataAnalyzer
from Printer import Printer
from FileWriter import FileWriter


def main():
    districts_2014, ballot_boxes_2014, neighbourhoods_2014 = DataLoader.load_data("2014_data")
    districts_2019, ballot_boxes_2019, neighbourhoods_2019 = DataLoader.load_data("2019_data")

    da_2014 = DataAnalyzer(districts_2014, ballot_boxes_2014, neighbourhoods_2014)
    da_2019 = DataAnalyzer(districts_2019, ballot_boxes_2019, neighbourhoods_2019)

    printer = Printer(82, 10)
    printer.print_districts(da_2014.get_districts_by_margin_of_error(3))
    printer.print_neighbourhoods(da_2019.get_neighbourhoods_by_margin_of_error(3))


    districts_2014_all_results = da_2014.get_districts_by_margin_of_error(100)
    ballot_boxes_2014_all_results = da_2014.get_ballot_boxes_by_margin_of_error(100)
    neighbourhoods_2014_all_results = da_2014.get_neighbourhoods_by_margin_of_error(100)

    districts_2019_all_results = da_2019.get_districts_by_margin_of_error(100)
    ballot_boxes_2019_all_results = da_2019.get_ballot_boxes_by_margin_of_error(100)
    neighbourhoods_2019_all_results = da_2019.get_neighbourhoods_by_margin_of_error(100)

    FileWriter.write_districts(districts_2014_all_results, "Results/districts_2014_results")
    FileWriter.write_ballot_boxes(ballot_boxes_2014_all_results, "Results/ballot_boxes_2014_results")
    FileWriter.write_neighbourhoods(neighbourhoods_2014_all_results, "Results/neighbourhoods_2014_results")

    FileWriter.write_districts(districts_2019_all_results, "Results/districts_2019_results")
    FileWriter.write_ballot_boxes(ballot_boxes_2019_all_results, "Results/ballot_boxes_2019_results")
    FileWriter.write_neighbourhoods(neighbourhoods_2019_all_results, "Results/neighbourhoods_2019_results")


main()
