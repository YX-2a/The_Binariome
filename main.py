from tkinter import Tk, Canvas
from interface import Interface, Lever


if __name__ == "__main__" :
    w = Tk()
    w.title ("Interact Two")
    w.resizable (0,0)

    he = 250
    wi = 300

    terface1 = Interface()
    terface1.create_canvas (w,he,wi)

    terface2 = Interface()
    terface2.create_canvas (w,he,wi)

    Lever().create_levers (terface1.can_,[he//2,wi*(1/6),he//2 + he//5,wi*(1/6) + wi//15],"#000000",[he//2,wi*(4/6),he//2 + he//5,wi*(4/6) + wi//15],"#000000")
    Lever().create_levers (terface2.can_,[he//2,wi*(4/6),he//2 + he//5,wi*(4/6) + wi//15],"#000000",[he//2,wi*(1/6),he//2 + he//5,wi*(1/6) + wi//15],"#000000")
    
    w.mainloop()

