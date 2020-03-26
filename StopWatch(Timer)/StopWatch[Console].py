#!/usr/bin/python3

def StopWatch():
    
    h, m, s, ms = 00, 00, 00, 00

    while ms < 60 and ms >= 0:
        hours = str(h) + ':' + str(m) + ':' + str(s) + ':' + str(ms)
        print(hours)
        ms += 1
        if ms == 60:
            ms = 0
            if s < 60 and s >= 0:
                s += 1
                if s == 60:
                    s = 0
                    if m < 60 and m >= 0:
                        m += 1
                        if m == 60:
                            m = 0
                            if h < 24 and h >= 0:
                                h += 1
                                if h == 24:
                                    h = 0

StopWatch()
