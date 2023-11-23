import pandas as pd
import os
from District import District
from BallotBox import BallotBox
from Neighbourhood import Neighbourhood


class DataLoader:
    @staticmethod
    def load_data(file_path: str):
        # @Parameter: file_path containing the election results of individual neighbourhoods and of total city for a particular election
        # @Return: 3D tuple containing districts, ballot boxes, and neighbourhoods dictionaries whose keys are their unique identifiers and whose values are District, Ballot Box, and Neighbourhood objects, respectively

        districts = dict()
        ballot_boxes = dict()
        neighbourhoods = dict()

        file_list = os.listdir(file_path)

        for filename in file_list:
            df = pd.read_excel("{}/{}".format(file_path, filename), skiprows=10)
            if filename.split('.')[0] == "genel":
                for index, row in df.iterrows():
                    district = District(row["İlçe Adı"], row["Toplam Geçerli Oy"])
                    for column_name, value in row.iloc[9:].items():
                        district.add_party(column_name, value)
                    districts[district.name] = district
            else:
                for index, row in df.iterrows():
                    ballot_box = BallotBox(row["İlçe Adı"], row["Mahalle/Köy"], row["Sandık No"],
                                           row["Toplam Geçerli Oy"])

                    if ballot_box.neighbourhood not in neighbourhoods:
                        neighbourhood = Neighbourhood(row["Mahalle/Köy"], row["İlçe Adı"])
                        neighbourhoods[row["Mahalle/Köy"]] = neighbourhood
                    else:
                        neighbourhood = neighbourhoods[ballot_box.neighbourhood]

                    for column_name, value in row.iloc[11:].items():
                        ballot_box.add_party(column_name, value)
                    ballot_boxes[(ballot_box.district, ballot_box.ballot_box_no)] = ballot_box
                    neighbourhood.add_ballot_box(ballot_box)

        return districts, ballot_boxes, neighbourhoods
