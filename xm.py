import glob
import pathlib
import csv
from bs4 import BeautifulSoup

root_path = pathlib.Path().absolute() / "xml_files"

headers = [
    "award_title",
    "effective_date",
    "expiry_date",
    "total_amount",
    "award_instrument",
    "program_officer",
    "abstract",
    "award_id",
    "investigator_firstname",
    "investigator_lastname",
    "investigator_email_address",
    "investigator_startdate",
    "university_name",
    "university_city",
    "university_phonenumber",
    "university_streetaddress",
    "university_country",
    "university_statename",
    "university_state_Code",
]


def get_filepaths(root_path):
    return glob.glob(str(root_path) + "/*.xml")


def xml_to_csv(path):
    unique_name = pathlib.Path(path).stem
    source = open(path, "r").read()
    elements = BeautifulSoup(source, features="xml")

    # create csv file
    csv_file = open(f"csv_files/data_{unique_name}.csv", "w")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)

    for element in elements.find_all("Award"):
        award_title = element.find("AwardTitle").text
        effective_date = element.find("AwardEffectiveDate").text
        expiry_date = element.find("AwardExpirationDate").text
        total_amount = element.find("AwardTotalIntnAmount").text
        award_instrument = element.find("AwardInstrument").find("Value").text
        program_officer = element.find("SignBlockName").text
        abstract = element.find("AbstractNarration").text
        award_id = elements.find("AwardID").text
        investigator_firstname = elements.find("FirstName").text
        investigator_lastname = elements.find("LastName").text
        investigator_email_address = elements.find("EmailAddress").text
        investigator_startdate = elements.find("StartDate").text
        university_name = elements.find("Institution").find("Name").text
        university_city = elements.find("Institution").find("CityName").text
        university_phonenumber = elements.find("Institution").find("PhoneNumber").text
        university_streetaddress = (
            elements.find("Institution").find("StreetAddress").text
        )
        university_country = elements.find("Institution").find("CountryName").text
        university_statename = elements.find("Institution").find("StateName").text
        university_state_Code = elements.find("Institution").find("StateCode").text

        csv_writer.writerow(
            [
                award_title,
                effective_date,
                expiry_date,
                total_amount,
                award_instrument,
                program_officer,
                abstract,
                award_id,
                investigator_firstname,
                investigator_lastname,
                investigator_email_address,
                investigator_startdate,
                university_name,
                university_city,
                university_phonenumber,
                university_streetaddress,
                university_country,
                university_statename,
                university_state_Code,
            ]
        )

    csv_file.close()


# this will retrieve the path to all the csvs in the folder
paths = get_filepaths(root_path)

# This picks the first path from paths and converts it to a csv
# xml_to_csv(paths[0])

# For multiple files
for path in paths:
    xml_to_csv(path)
