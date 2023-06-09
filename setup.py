from setuptools import find_packages, setup 

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements():

    #Ham yaha sare requirement ko read kar re or unhe string me convert karke LIST me dalre
    #Or 'requirement.txt' me "/n" he matlab next line h har jagah to ham use remove kar re nahi to installation me error aayenga samjha
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [i.replace("\n", "") for i in requirement_list]


    #hame "setup.py" ko trigger karne "-e ." chaiye rehta he par installation me isko remove karna padta nahi to error milta
    #Isliye ham ise remove kartehe
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    #Yaha ham hamare man se jo aage package banenga for example PANDAS ka new version aaya waisehi yaha hamare code 
    #ka package ban ne wala he isliye ham yaha hamare package ka name info sab dere samjha
    name='sensor',
    version='0.0.1',
    author='Jaki Polad',
    author_email='jakipolad13@gmail.com',

    #Ye packages jo he wo apne code ka PAKCAGE banata he, jis bhi folder me  "__init__" ye constructor rehta 
    #ye use PACKAGE banadenga
    packages=find_packages(),

    #apne project ko or konse konse LIBRARIES chiaye wo ye requirments se dekh ke install karlenga samjha 
    install_requires= get_requirements()


    #TO basically ham yaha kisi orke liye bhi hamara project use karwana easy banarehe
)