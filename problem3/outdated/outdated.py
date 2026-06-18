def outdated():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            t = input("Date: ").strip()
            if "/" in t:
                mes, dia, ano = t.split("/")
                if not mes.isnumeric() or not dia.isnumeric() or not ano.isnumeric() or not 1 <= int(dia) <= 31 or not 1 <= int(mes) <= 12:
                    raise ValueError()
                print(f"{ano}-{int(mes):02}-{int(dia):02}")
                break

            elif "," in t:
                v_data, v_ano = t.split(",")
                v_mes, v_dia = v_data.split()
                if v_mes in months and 1 <= int(v_dia) <= 31 and 1 <= int(months.index(v_mes.capitalize())-1) <= 12:
                    print(
                        f"{int(v_ano)}-{months.index(v_mes.capitalize())+1:02}-{int(v_dia):02}")
                    break

        except ValueError:
            pass


outdated()
