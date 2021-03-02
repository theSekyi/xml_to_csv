import os, sys
import glob
from xml.etree import ElementTree
import pathlib

root_path = pathlib.Path().absolute()/'xml_files'
#path = os.path.dirname('xml_files')#"/home/socs/projects/xml/xml_files"

headers = ['award_title','effective_date','expiry_date','total_amount',
    'award_instrument','program_officer','abstract','award_id',
    'investigator_firstname','investigator_lastname','investigator_email_address',
    'investigator_startdate', 'university_name','university_city','university_phonenumber',
    'university_streetaddress','university_country','university_statename','university_state_Code'
    ]

def get_filepaths(root_path):
    return glob.glob(str(root_path)+"/*.xml")


def convert_to_json(file_path):
    pass

print(len(headers))