
def main():
    # open a file for writing and create it if it doesn't exist
    f = open(r"F:\Github\Python\Practice\Files\data\file3.txt", "w")

    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()

if __name__ == "__main__":
    main()