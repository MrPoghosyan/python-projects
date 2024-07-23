import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" # writ"?"...
key = "your_key_write"

while True:
    orig = input("Starting location: ")
    if orig.lower() == "quit" or orig.lower() == "q":
        break

    dest = input("Destination: ")
    if orig.lower() == "quit" or orig.lower() == "q":
        break
    
    url = main_api + urllib.parse.urlencode(
            {"key":key, "from":orig, "to":dest, "unit":"k", "locale":"ru_RU"})
    print(url)

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful rout call.\n")
        print("Direction from: " + orig + " to " + dest)
        print("Trip Duration:  " + json_data["route"]["formattedTime"])
        print("Kilometers:     " + str(json_data["route"]["distance"]))
        print("Fuel Used:      " + str("{:.2f}".format(json_data["route"]["distance"]*8/100)))  # It consumes 8 liters of gasoline pre 100km

        print("\n=====================================================\n")

        for each in json_data["route"]["legs"]["0"]["maneuvers"]:
            print(each["narrative"])

        print("\n=====================================================\n")

    else:
        print("API Statuse: " + str(json_statuse) + ". " + json_data["info"]["messages"][0])
        print("Refe to: https://developer.mapquest.com/documentation/api/search-ahead/status-codes.html#general-status-codes")
        
        print("\n=====================================================\n")
