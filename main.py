def filepath_get(filepath: str = "", baseline: bool = False):
    path = __file__
    path = path.split("\\")
    temp = ""
    if baseline:
        for i in range(0, len(path) - 1):
            temp += path[i] + "\\"
        temp += filepath
        return temp
    for i in range(0, 3):
        temp += path[i] + "\\"
    path = temp + filepath
    return path


def parsefile(filepath: str = ""):
    f = open(filepath, "r")
    contents = f.read().split("- manifestVersion")
    temp = []
    temp2 = []
    for i in range(1, len(contents)):
        contents2 = contents[i].split("\n")
        if contents2[len(contents2) - 1] == "":
            temp2.append(contents2[4].strip())
            temp2.append(contents2[len(contents2) - 3].strip())
        else:
            temp2.append(contents2[4].strip())
            temp2.append(contents2[len(contents2) - 2].strip())

        if temp2[1] == "enabled: true":
            temp.append(temp2[0].split("displayName: ")[1])
        temp2 = []
    return temp


def compare_arrays(array1: list, array2: list):
    matching = []
    for i in range(0, len(array1)):
        if array2.__contains__(array1[i]):
            matching.append(array1[i])

    if len(matching) > 0:
        for i in range(0, len(matching)):
            array1.remove(matching[i])
            array2.remove(matching[i])

    if len(array2) == len(array1):
        if len(array1) == 0:
            print("Mod lists match")

    if len(array1) > 0:
        print("These mods are disabled or missing from mod list: ")
        for i in range(0, len(array1)):
            print(array1[i])

    if len(array2) > 0:
        print("These mods are enabled that are missing from baseline: ")
        for i in range(0, len(array2)):
            print(array2[i])


if __name__ == '__main__':
    profileName = input("Please enter Profile name to compare with baseline: ")
    try:
        compare_arrays(parsefile(filepath_get("baseline.yml", True)), parsefile(
            filepath_get(f"AppData\\Roaming\\r2modmanPlus-local\\RiskOfRain2\\profiles\\{profileName}\\mods.yml")))
    except FileNotFoundError:
        print("Either this Profile doesnt exist, or it doesnt contain a mods file that is in the format of a YML file")
