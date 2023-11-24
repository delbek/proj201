class FileWriter:
    @staticmethod
    def write_districts(districts_dict: dict, file_path):
        sorted_dictionary = FileWriter.sort_dictionary(districts_dict)

        with open(file_path, 'w') as file:
            for entry in sorted_dictionary.keys():
                file.write("District: {} has an error margin of {}\n".format(entry.name, sorted_dictionary[entry]))

    @staticmethod
    def write_ballot_boxes(ballot_box_dict: dict, file_path):
        sorted_dictionary = FileWriter.sort_dictionary(ballot_box_dict)

        with open(file_path, 'w') as file:
            for entry in sorted_dictionary.keys():
                file.write("No: {} ballot box located in {}/{} has an error margin of {}\n".format(entry.ballot_box_no, entry.neighbourhood, entry.district, sorted_dictionary[entry]))

    @staticmethod
    def write_neighbourhoods(neighbourhood_dict: dict, file_path):
        sorted_dictionary = FileWriter.sort_dictionary(neighbourhood_dict)

        with open(file_path, 'w') as file:
            for entry in sorted_dictionary.keys():
                file.write("{} has an error margin of {}\n".format(entry.neighbourhood_name, sorted_dictionary[entry]))

    @staticmethod
    def sort_dictionary(dictionary: dict) -> dict:
        # Sorting the dictionary by its values in ascending order
        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
        return sorted_dict
