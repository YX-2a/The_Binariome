from tkinter import Tk, Canvas
from interface import Interface, Lever

class Level:
    def __init__ (self):
        self.w = Tk()
        self.w.resizable (0,0)

    def make_level (self, title, height, width, canl):
        self.w.title (title)
        for ca in canl:
                if ca[1] == True:
                    terface_ = Interface()
                    terface_.create_canvas (self.w,height,width,ca[0])
                    Lever().create_levers (terface_.can_,height,width)
                    
                else:
                    terface_ = Interface()
                    terface_.create_canvas (self.w,height,width,ca[0])

    def end_ (self):    
        self.w.mainloop()


def read_level (filename):
    with open (filename) as levl:
        levl_raw = levl.readlines ()

    i0, i1, tit, hi, wi, can_list = None,None,None,None,None,[]

    for i in levl_raw :
        if "YLFSys ==" in i:
            i0 = i
        if "== YLFSys" in i:
            i1 = i
        else:
            continue
        
    inde1 = levl_raw.index(i0) + 1
    inde2 = levl_raw.index(i1) 
    
    levl_uck = levl_raw [ inde1 : inde2 ]
    levl_uck = [i.strip() for i in levl_uck]
    levl_uck = [i for i in levl_uck if i != ""]

    for i in levl_uck:
        if "t:" in i:
            tit = i.replace ("t:","")
        if "h:" in i:
            hi = int(i.replace ("h:",""))
        if "w:" in i:
            wi = int(i.replace ("w:",""))
            levl_uck = levl_uck[levl_uck.index(i) + 1:]

    for i in levl_uck:
        can = i[3:]
        if "," in can:
            can_list.append ([can[:can.index(",l")], True ])
        else:
            can_list.append ([can, False ])
            
    return tit, hi, wi, can_list
