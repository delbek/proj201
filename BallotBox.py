class BallotBox:
    def __init__(self, district: str, neighbourhood: str, ballot_box_no: int, total_vote: int):
        # Primary Key is the tuple -> (self.district, self.ballot_box_no) -> This is due to the fact that the ballot box no is unique in each district but not in the whole city
        self.district = district  # District name in which this ballot box is located
        self.ballot_box_no = ballot_box_no  # Ballot box no
        self.neighbourhood = neighbourhood  # Neighbourhood name in which this ballot box is located
        self.total_vote = total_vote  # Total vote of this ballot box
        self.parties_by_vote = dict()  # Key -> party name | Value -> Vote count party has received
        self.parties_by_percentage = dict()  # Key -> party name | Value -> Vote percentage party has received

    def add_party(self, party_name: str, vote_received: int):
        self.parties_by_vote[party_name] = vote_received
        self.parties_by_percentage[party_name] = (vote_received / self.total_vote) * 100
