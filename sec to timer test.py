def convert_sec_to_time(time_left):
    hh = int(time_left / 3600)
    mm = int(((time_left / 3600) - hh) * 60)
    ss = round(((((time_left / 3600) - hh) * 60) - mm) * 60)

    return hh, mm, ss
    print(hh, mm, ss)


def con_tim_to_sec(h, m, s):
    return h * 3600 + m * 60 + s


for i in range(0, 10000):
    hh, mm, ss = convert_sec_to_time(i)
    if i == con_tim_to_sec(hh, mm, ss):
        print(i, '', hh, mm, ss)
    else:
        print(i, '', '***', hh, mm, ss, '***', )
