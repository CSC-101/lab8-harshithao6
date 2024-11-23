import sys
#input: common-line argument
#output: added floats
#pupose: to read in a file and add the two float values together
def main():
   #if there is no file
    if len(sys.argv) <2:
        print("there is an error")
        exit()

    filename = sys.argv[1]
    try:
        with open(filename,"r") as file_data:
            for line in file_data:
                data = line.split()
                value1 = float(data[0])
                value2 = float(data[1])
                print(value1 + value2)

    except ValueError:
        print(f"Error: this cannot be converted to a float.")
        exit()
    except FileNotFoundError:
        print(f"Error: File not found.")
        exit()

if __name__ == "__main__":
    main()



