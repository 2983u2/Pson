from Pson import *


result = JParse("""{
    "Name": "Thorne Baker",
    "Properties": {
        "Garage": "AlpineSt",
        "Apartment": "AlpineSt - Apt 1"
    }

}""")
print("Name: ", result['obj']['Name'])
print("Addy: ", result['obj']['Properties']['Apartment'])
print("Garage: ", result['obj']['Properties']['Garage'])
