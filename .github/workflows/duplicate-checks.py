import os
import sys

def duplicate_check():
    files = os.listdir(".")
    files.remove(".git")
    files.remove(".github")
    list = []
    for i in files:
        list.append(i)
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
                duplicate_array.append(list[j])
    return set(duplicate_array)

if __name__ == "__main__":

    duplicates = sorted((list(duplicate_check())))
    # duplicates = str(duplicates)
    print(f"found duplicates - {duplicates}")
    sys.exit(1)
