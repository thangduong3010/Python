import urllib2
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print("Title: {}".format(theJSON["metadata"]["title"]) )

    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    # for each event, print the place where it occurred
    # print("All events:")
    # for i in theJSON["features"]:
    #     print("Place: " + i["properties"]["place"])

    # print the events that only have a magnitude greater than 4
    # print("The events that have a magnitude greater than 4:")
    # for i in theJSON["features"]:
    #     if i["properties"]["mag"] > 4:
    #         print("Place: " + i["properties"]["place"] + " - Magnitude: %.2f" % i["properties"]["mag"])

    # print only the events where at least 1 person reported feeling something
    print("Events that were left:")
    for i in theJSON["features"]:
        feltReport = i["properties"]["felt"]
        if (feltReport != None) and (feltReport > 0):
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReport) + " times" )

def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read data
    webURL = urllib2.urlopen(urlData)
    print("Status: {}".format(webURL.getcode()) )
    if (webURL.getcode() == 200):
        data = webURL.read()
        printResults(data)
    else:
        print("Cannot retrieve the data. Status: {}".format(webURL.getcode()) )


if __name__ == "__main__":
    main()