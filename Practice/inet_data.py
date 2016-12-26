import urllib2

def main():
    # Open a connection to a URL
    webURL = urllib2.urlopen("http://google.com")

    # Get the result code
    print("Result code: {}".format(str(webURL.getcode())) )

    # Read data from the URL and print it
    data = webURL.read()
    print(data)

if __name__ == "__main__":
    main()