class DataAnalyzer:
    def __init__(self, districts: dict, ballot_boxes: dict, neighbourhoods: dict):
        self.districts = districts  # a dictionary with keys being district_name and values being district object
        self.ballot_boxes = ballot_boxes  # a dictionary with keys being tuple (district, ballot_box_no) and values being ballot_box object
        self.neighbourhoods = neighbourhoods # a dictionary with keys being neighbourhood name and values being neighbourhood object
        self.total_vote = None  # the number of votes that are valid in the whole city -> int
        self.total_parties_by_vote_count = None  # the number of votes that each party received in the whole city -> dict(party_name: str, party_vote_: int)
        self.total_parties_by_percentage = None  # the percentage of total votes that each party received in the whole city -> dict(party_name: str, party_percentage: float)

    def get_percentages_total(self) -> dict:
        # @Return: a dictionary in which keys are party names and values are the percentage of total votes that each party received in the city
        # @PrivateMemberAffect: permanently changes self.total_vote, self.total_parties_by_vote_count, and self.total_parties_by_percentage

        if self.total_parties_by_percentage is not None:
            return self.total_parties_by_percentage

        self.total_vote = int()
        self.total_parties_by_vote_count = dict()
        self.total_parties_by_percentage = dict()

        for district_name in self.districts.keys():
            district = self.districts[district_name]
            self.total_vote += district.total_vote

            for party_name in district.parties_by_vote_count.keys():
                party_vote = district.parties_by_vote_count[party_name]

                if party_name not in self.total_parties_by_vote_count.keys():
                    self.total_parties_by_vote_count[party_name] = 0

                self.total_parties_by_vote_count[party_name] += party_vote

        for party_name in self.total_parties_by_vote_count.keys():
            party_vote = self.total_parties_by_vote_count[party_name]
            self.total_parties_by_percentage[party_name] = (party_vote / self.total_vote) * 100

        return self.total_parties_by_percentage

    def get_districts_by_margin_of_error(self, margin_of_error: float) -> dict:
        # @Parameter: margin_of_error: maximum error margin that the district can have compared to the local election results
        # @Return: dict(district: District, error_margin: int) containing the district objects whose error margin is within the parameter specified

        ret = dict()

        for district_name in self.districts.keys():
            district = self.districts[district_name]
            biggest_error_margin = 0

            district_percentages = district.parties_by_percentage
            total_percentages = self.get_percentages_total()

            is_within = True
            for party_name in total_percentages.keys():
                total_party_percentage = total_percentages[party_name]
                district_party_percentage = district_percentages[party_name]

                current_error_margin = abs(total_party_percentage - district_party_percentage)

                if current_error_margin > biggest_error_margin:
                    biggest_error_margin = current_error_margin

                if current_error_margin > margin_of_error:
                    is_within = False
                    break

            if is_within:
                ret[district] = biggest_error_margin

        return ret

    def get_ballot_boxes_by_margin_of_error(self, margin_of_error: float) -> dict:
        # @Parameter: margin_of_error: maximum error margin that the ballot_box can have compared to the district election result in which this ballot box is located
        # @Return: dict(ballot_box: BallotBox, error_margin: int) containing the ballot box objects whose error margin is within the parameter specified

        ret = dict()

        for primary_key in self.ballot_boxes.keys():
            ballot_box = self.ballot_boxes[primary_key]
            biggest_error_margin = 0
            district = self.districts[primary_key[0]]

            ballot_box_percentages = ballot_box.parties_by_percentage
            district_percentages = district.parties_by_percentage

            is_within = True
            for party_name in district_percentages.keys():
                district_party_percentage = district_percentages[party_name]
                try:
                    ballot_box_party_percentage = ballot_box_percentages[party_name]
                except:  # The case in which the party has not entered to the election for that ballot box
                    ballot_box_party_percentage = 0

                current_error_margin = abs(district_party_percentage - ballot_box_party_percentage)

                if current_error_margin > biggest_error_margin:
                    biggest_error_margin = current_error_margin

                if current_error_margin > margin_of_error:
                    is_within = False
                    break

            if is_within:
                ret[ballot_box] = biggest_error_margin

        return ret

    def get_neighbourhoods_by_margin_of_error(self, margin_of_error: float) -> dict:
        # @Parameter: margin_of_error: maximum error margin that the neighbour can have compared to the district election result in which this neighbourhood is located
        # @Return: dict(neighbourhood: Neighbourhood, error_margin: int) containing the neighbourhood objects whose error margin is within the parameter specified

        ret = dict()

        for neighbourhood_name in self.neighbourhoods.keys():
            neighbourhood = self.neighbourhoods[neighbourhood_name]
            neighbourhood.calculate_percentages()
            biggest_error_margin = 0
            district = self.districts[neighbourhood.district]

            neighbourhood_percentages = neighbourhood.parties_by_percentage
            district_percentages = district.parties_by_percentage

            is_within = True
            for party_name in district_percentages.keys():
                district_party_percentage = district_percentages[party_name]
                try:
                    neighbourhood_party_percentage = neighbourhood_percentages[party_name]
                except:  # # The case in which the party has not entered to the election for all the ballot boxes located in that neighbourhood
                    neighbourhood_party_percentage = 0

                current_error_margin = abs(district_party_percentage - neighbourhood_party_percentage)

                if current_error_margin > biggest_error_margin:
                    biggest_error_margin = current_error_margin

                if current_error_margin > margin_of_error:
                    is_within = False
                    break

            if is_within:
                ret[neighbourhood] = biggest_error_margin

        return ret
