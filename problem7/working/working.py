import re


def main():
    time = input("Hours: ")
    print(convert(time))


def convert(time):
    pattern = r"^(?:(0?[1-9])?|(1[0-2])?)(?:\:([0-5][0-9]))? (AM|PM) to (?:(0?[1-9])?|(1[0-2])?)(?:\:([0-5][0-9]))? (AM|PM)"
    if matches := re.search(pattern, time.strip()):
        first = {
            "minutes": matches.group(3),
            "daytime": matches.group(4)
        }
        last = {
            "minutes": matches.group(7),
            "daytime": matches.group(8)
        }
        if last["minutes"] == None:
            last["minutes"] = "00"
        if first["minutes"] == None:
            first["minutes"] = "00"
        count = 1

        while count <= len(matches.groups()):
            if count <= 2 and matches.group(count) != None:
                first["hours"] = f"{int(matches.group(count)):02}"
                if first["daytime"] == "PM" and int(first["hours"]) != 12:
                    first["hours"] = f"{int(first["hours"])+12:02}"
                elif first["daytime"] == "AM" and int(first["hours"]) == 12:
                    first["hours"] = "00"

            if count in [5, 6] and matches.group(count) != None:
                last["hours"] = f"{int(matches.group(count)):02}"
                if last["daytime"] == "PM" and int(last["hours"]) != 12:
                    last["hours"] = f"{int(last["hours"])+12:02}"
                elif last["daytime"] == "AM" and int(last["hours"]) == 12:
                    last["hours"] = "00"

            count += 1
        return f"{first["hours"]}:{first["minutes"]} to {last["hours"]}:{last["minutes"]}"

    else:
        raise ValueError()


if __name__ == "__main__":
    main()
