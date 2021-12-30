def oblicz_predkosc(droga,droga_unit,czas,czas_unit):
    unit_dic={'h':1,'min':1/60,'s':1/3600,'km':1,'m':1/1000}
    s=float(droga)*unit_dic[droga_unit]
    t=float(czas)*unit_dic[czas_unit]
    return round(s/t,3)

class Roztwor_alkoholu():
    def __init__(self,obj_1,alk_1,obj_2,alk_2):
        self.obj_1 = float(obj_1)
        self.alk_1 = float(alk_1)
        self.obj_2 = float(obj_2)
        self.alk_2 = float(alk_2)

    def roztwor(self):
        wynik = (self.obj_1*self.alk_1/100 + self.obj_2*self.alk_2/100)/(self.obj_1+self.obj_2)
        return round(wynik*100,1)


class Wino_cukier():
    def __init__(self,obj,alk):
        self.obj = float(obj)
        self.alk = float(alk)

    def cukier(self):
        return 17*self.obj*self.alk

if __name__=='__main__':
    w = Wino_cukier(30,17)
    print(w.cukier())