def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0
    m = len(yc)

    for i, y in enumerate(yc):
        t = i + 1
        cashflow = coupon
        if t == m:
            cashflow = coupon + face

        discount = 1 / ((1 + y) ** t)
        bondPrice += cashflow * discount

    return bondPrice