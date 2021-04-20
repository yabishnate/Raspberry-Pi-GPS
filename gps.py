import requests
import smtplib

#API key
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close()

address = input("Please enter your current address\n")

destination = input("Please enter the destination\n")

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

r = requests.get(url + "origins=" + address + "&destinations=" + destinations + "&key=" + api_key)

time = r.json()["rows"[0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"[0]["elements"][0]["duration"]["value"]
                   
print("\n The total travel time from your address to the destination is", time)
