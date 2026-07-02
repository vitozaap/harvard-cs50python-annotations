values = [100, 50, 20]


def calculate(galleons, sickles, knuts):
    return galleons + sickles + knuts


# You can unpack a list using *:
print(calculate(*values))


values = {"galleons": 100, "sickles": 50, "knuts": 0}

# With 2 stars you can unpack dicts and set named parameters: 
# galleons=100, sickles=50, knuts=0
calculate(**values)
