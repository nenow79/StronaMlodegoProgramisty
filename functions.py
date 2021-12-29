def oblicz_predkosc(droga,droga_unit,czas,czas_unit):
    unit_dic={'h':1,'min':1/60,'s':1/3600,'km':1,'m':1/1000}
    s=float(droga)*unit_dic[droga_unit]
    t=float(czas)*unit_dic[czas_unit]
    return round(s/t,3)


