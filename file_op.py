class File:

    FILENAME = "data.txt"

    def __init__(self):
        pass

    def write(self, data):
        try:
            with open(File.FILENAME, mode="a") as f:
                f.write(data)
                f.write("\n")
        except:
            print("An error occured. please try again")
            return False
        else:
            return True
