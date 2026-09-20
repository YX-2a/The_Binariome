from tkinter import Tk, Canvas

##Consts
H = 250
W = 300

##Funcs
def create_int (parent):
    global actif1, actif2, can1, can2 
    
    def change_1 (heh):
        global actif1
       
        if heh.x  in range (H//2,H//2 + 50) and heh.y in range (round(W*(1/6)), round (W*(1/6)) + 20):
            can1.delete (actif1)
            actif1 = can1.create_rectangle (H//2,W*(4/6),H//2 + 50,W*(4/6) + 20, fill = "#000000")
            can1.bind ("<Button-1>", change_4)

        else:
            None
            
    def change_2 (heh):
        global actif2

        if heh.x  in range (H//2,H//2 + 50) and heh.y in range (round(W*(4/6)),round(W*(4/6)) + 20):
            can2.delete (actif2)
            actif2 = can2.create_rectangle (H//2,W*(1/6),H//2 + 50,W*(1/6) + 20, fill = "#000000")

            can2.bind ("<Button-1>", change_3)

        else:
            None

    def change_3 (heh):
        global actif2
        if heh.x  in range (H//2,H//2 + 50) and heh.y in range (round(W*(1/6)),round(W*(1/6)) + 20):
                can2.delete (actif2)
                actif2 = can2.create_rectangle (H//2,W*(4/6),H//2 + 50,W*(4/6) + 20, fill = "#000000")

                can2.bind ("<Button-1>", change_2)

        else:
                None
        
    def change_4 (heh):
            global actif1
            if heh.x  in range (H//2,H//2 + 50) and heh.y in range (round(W*(4/6)),round(W*(4/6)) + 20):
                can1.delete (actif1)
                actif1 = can1.create_rectangle (H//2,W*(1/6),H//2 + 50,W*(1/6) + 20, fill = "#000000")

                can1.bind ("<Button-1>", change_1)

            else:
                None

    big = "#aaaaaa"
    
    can1 = Canvas (parent, height = H, width = W,bg = big )
    can2 = Canvas (parent, height = H, width = W,bg = big )

    lien1 = can1.create_line (H//2 + 25,W*(1/6) - 10,H//2 + 25,W*(4/6) + 30,width = 5, fill = "#909090")
    lien2 = can2.create_line (H//2 + 25,W*(1/6) - 10,H//2 + 25,W*(4/6) + 30,width = 5, fill = "#909090") 

    actif1 = can1.create_rectangle (H//2,W*(1/6),H//2 + 50,W*(1/6) + 20, fill = "#000000")
    actif2 = can2.create_rectangle (H//2,W*(4/6),H//2 + 50,W*(4/6) + 20, fill = "#000000")

    can1.pack (side = "left")
    can2.pack (side = "left")

    can1.bind ("<Button-1>", change_1)
    can2.bind ("<Button-1>", change_2)


##Winconf
w = Tk()
w.title ("Interact Two")
w.resizable (0,0)

create_int (w)

w.mainloop()
