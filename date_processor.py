def increment_date(date):
    y = date // 10000
    m = (date // 100) % 100
    d = date % 100

    d = d + 1
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if d == 32:
            m += 1
            d = 1

    if m in [4, 6, 9, 11]:
        if d == 31:
            m += 1
            d = 1

    if m == 2:
        if y % 4 == 0 and y != 2000:
            if d == 30:
                m += 1
                d = 1
        else:
            if d == 29:
                m = m + 1
                d = 1

    if m == 13:
        m = 1
        y += 1

    return d + 100 * m + 10000 * y