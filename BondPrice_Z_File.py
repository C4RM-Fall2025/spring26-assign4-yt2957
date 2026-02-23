def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0

    for t, y in zip(times, yc):
        cashflow = coupon
        if t == times[-1]:
            cashflow = coupon + face
        discount = 1 / ((1 + y) ** t)
        bondPrice = bondPrice + cashflow * discount

    return bondPrice