class District:
    def __init__(self, name: str, total_vote: int):
        self.name = name  # Primary Key
        self.total_vote = total_vote  # Total vote count of this district
        self.parties_by_vote_count = dict()  # Key -> party name | Value -> Vote count party has received
        self.parties_by_percentage = dict()  # Key -> party name | Value -> Vote percentage party has received

    def add_party(self, party_name: str, vote_received: int):
        self.parties_by_vote_count[party_name] = vote_received
        self.parties_by_percentage[party_name] = (vote_received / self.total_vote) * 100
