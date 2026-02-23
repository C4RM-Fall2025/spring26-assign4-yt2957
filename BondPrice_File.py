def getBondPrice(y, face, couponRate, m, ppy = 1):
    period_rate = y / ppy                  
    coupon = face * couponRate / ppy       
    n_periods = m * ppy                    

    bondPrice = 0

    for t in range(1, n_periods + 1):
        cash_flow = coupon
        if t == n_periods:                
            cash_flow = cash_flow + face

        discount_factor = 1 / ((1 + period_rate) ** t)
        pv = cash_flow * discount_factor
        bondPrice = bondPrice + pv

    return bondPrice