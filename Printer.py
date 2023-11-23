class Printer:
    def __init__(self, frame_length: int, left_space_length: int):
        self.frame_length = frame_length  # the width of the frame to be generated
        self.left_space_length = left_space_length  # the left space that is given for each of the body string

    def print_ballot_boxes(self, ballot_box_dict: dict):
        print()
        print(self.generate_frame("BALLOT BOXES"))
        for key in ballot_box_dict.keys():
            print(self.generate_body("No: {} ballot box located in {}/{} has an error margin of {}".format(key.ballot_box_no, key.neighbourhood, key.district, ballot_box_dict[key])))
        print(self.generate_frame("BALLOT BOXES ENDS"))
        print()

    def print_districts(self, district_dict: dict):
        print()
        print(self.generate_frame("DISTRICTS"))
        for key in district_dict.keys():
            print(self.generate_body("District: {} has an error margin of {}".format(key.name, district_dict[key])))
        print(self.generate_frame("DISTRICTS ENDS"))
        print()

    def print_neighbourhoods(self, neighbourhood_dict: dict):
        print()
        print(self.generate_frame("NEIGHBOURHOODS"))
        for key in neighbourhood_dict.keys():
            print(self.generate_body("{} has an error margin of {}".format(key.neighbourhood_name, neighbourhood_dict[key])))
        print(self.generate_frame("NEIGHBOURHOODS ENDS"))
        print()

    def generate_frame(self, frame_string) -> str:
        frame_half_length = int((self.frame_length - len(frame_string)) / 2)
        frame = ("-" * frame_half_length) + frame_string + ("-" * frame_half_length)

        return frame

    def generate_body(self, body_string) -> str:
        right_space_length = self.frame_length - 2 - self.left_space_length - len(body_string)

        body = "|" + (" " * self.left_space_length) + body_string + (" " * right_space_length) + "|"

        return body
