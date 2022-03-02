visszaszamolas = int(input("Kérem adja meg, hány óra van hátra a rakéta kilövéséig!"))
eltelt = 0
megallt = 0
while visszaszamolas != 0:
    felfüggeszt = input("A visszaszámlálást megállíthatja egy órára. Szeretné halasztani a kilövést? (igen/nem)")
    if felfüggeszt == "igen":
        eltelt +=1
        megallt += 1
        print("A kilövés 1 órával késleltetve.")
        print("A kilövésig", visszaszamolas, "óra van hátra.", eltelt, "órája kezdődött a számlálás. Ebből", megallt, "alkalommal", megallt, "órára volt késleltetve a kilövés.")
    else:
        visszaszamolas -= 1
        eltelt += 1
        print("A kilövésig", visszaszamolas, "óra van hátra.", eltelt, "órája kezdődött a számlálás. Ebből", megallt, "alkalommal", megallt, "órára volt késleltetve a kilövés.")
print("A rakétát sikeresen kilőttük.")