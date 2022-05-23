import os
import sys

def duplicate_check():
    list = [
        os.path.join(dir_path, file)
        for dir_path, _, file_list in os.walk("rules")
        for file in file_list
        if file.endswith("json")
    ]

    duplicate_array = []
    for i in range(len(list)):
        data1=[]
        with open(list[i], "r") as file1:
                datafile1 = file1.read()
                for k in datafile1:
                    if k.strip() != "":
                        data1.append(k)
                
        for j in range(i+1, len(list)):
            data2 = []
            with open(list[j], "r") as file2:
                datafile2 = file2.read()
                for k in datafile2:
                    if k.strip() != "":
                        data2.append(k)
            if data1 == data2:
                duplicate_array.append(list[i])
                duplicate_array.append(list[j])
    return set(duplicate_array)

if __name__ == "__main__":

    duplicates = sorted((list(duplicate_check())))
    if duplicates:
        print(f"found duplicates - {duplicates}")
        sys.exit(1)
    else:
        print("No duplicates found")
        sys.exit(0)
