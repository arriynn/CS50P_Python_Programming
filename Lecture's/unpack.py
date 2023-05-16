def total(galleons, sickels, knuts):
    return f"{(galleons * 17 + sickels) * 29 + knuts:,}"

coins= {"galleons": 100, "sickels": 50, "knuts": 25}

print(total(**coins), "Knuts") 