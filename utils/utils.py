jednotky = {
    '1': "jedna",
    '2': "dva",
    '3': "tri",
    '4': "ctyri",
    '5': "pet",
    '6': "sest",
    '7': "sedm",
    '8': "osm",
    '9': "devet",
    '0': "nula"
}

desitky = {
    10: "deset",
    20: "dvacet",
    30: "tricet"
}


def cisla_do_slov(cislo: int) -> str:
    assert isinstance(cislo, int)
    cifry = list(str(cislo))
    output: str = ""
    for c in cifry:
        output += jednotky[c] + " "
    return output.rstrip()
