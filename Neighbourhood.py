from BallotBox import BallotBox


class Neighbourhood:
    def __init__(self, neighbourhood_name: str, district: str):
        self.neighbourhood_name = neighbourhood_name  # Primary Key
        self.district = district  # District name in which this neighbourhood is located
        self.ballot_boxes = list()  # All the ballot boxes that this neighbourhood consists of
        self.total_vote = 0  # Total vote of this neighbourhood
        self.parties_by_vote = dict()  # Key -> party name | Value -> Vote count party has received
        self.parties_by_percentage = dict()  # Key -> party name | Value -> Vote percentage party has received

    def add_ballot_box(self, ballot_box: BallotBox):
        self.ballot_boxes.append(ballot_box)

        for party_name in ballot_box.parties_by_vote.keys():

            if party_name not in self.parties_by_vote:
                self.parties_by_vote[party_name] = 0

            self.parties_by_vote[party_name] += ballot_box.parties_by_vote[party_name]

        self.total_vote += ballot_box.total_vote

    def calculate_percentages(self):
        if len(self.parties_by_percentage.keys()) == 0:
            for party_name in self.parties_by_vote.keys():
                self.parties_by_percentage[party_name] = (self.parties_by_vote[party_name] / self.total_vote) * 100
