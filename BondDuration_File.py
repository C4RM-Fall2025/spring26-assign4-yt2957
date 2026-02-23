def getBondDuration(y, face, couponRate, m, ppy = 1):
    period_rate = y / ppy                  
    coupon = face * couponRate / ppy       
    n_periods = m * ppy                    

    sum_pv_cashflows = 0                   
    sum_pv_times = 0                      

    for t in range(1, n_periods + 1):
        cash_flow = coupon
        if t == n_periods:                
            cash_flow = cash_flow + face

        discount_factor = 1 / ((1 + period_rate) ** t)
        pv_cash_flow = cash_flow * discount_factor

        time_in_years = t / ppy            

        sum_pv_cashflows = sum_pv_cashflows + pv_cash_flow
        sum_pv_times = sum_pv_times + pv_cash_flow * time_in_years

    bondPrice = sum_pv_cashflows
    bondDuration = sum_pv_times / bondPrice

    return bondDuration