def read_numbers(file):
    try:
        with open(file, "r", encoding = "utf-8") as file:
            content = file.read()
            return [float(x) for x in content.split()]
    except FileNotFoundError:
       print("file not found")
    except ValueError:
        print("incorrect value")
    print("program is continue working")







############# just a tests
# test = read_numbers("logs/measurement.txt")
# print (test)