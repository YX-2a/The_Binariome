from tkinter import Canvas

class Interface:
    def __init__ (self, bg_clr, ib_clr, fg_clr):
        self.color_bg = bg_clr
        self.color_lin = ib_clr 
        self.color_lvr = fg_clr
        
    def create_canvas (self,parent, height, width, book, shelf):
        self.can_ = Canvas (parent, height = height, width = width,bg = self.color_bg )
        self.lien_ = self.can_.create_line (width//2,height//20,width//2,height - height//20,width = 5, fill = self.color_lin)
        self.can_.grid (column = book,row = shelf)

class Lever  :
    def __init__ (self, inter):
        self.inter_father = inter
        self.actif_ = ""
        self.switc_ = None
        self.num_ = 0
        self.canvas = ""
        
    def create_levers (self,canvas,height,width,pow_):
        self.canvas = canvas
        self.pow_ = pow_
        self.cords2 = [width//2 - width//10,height*(10/13),width//2 + width//10,height*(10/13) + height//8]
        self.cords = [width//2 - width//10,height//10,width//2 + width//10,height//10 + height//8]
        self.color = self.inter_father.color_lvr
        self.color2 = self.color
        self.actif_ = self.canvas.create_rectangle (self.cords2, fill = self.color, outline = self.color)
        self.switc_ = True

    def change_ (self, heh):
        if self.switc_:
            if heh.x  in range (round(self.cords2[0]), round(self.cords2[2])) and heh.y in range (round(self.cords2[1]),round(self.cords2[3])):
                self.canvas.delete (self.actif_)
                self.actif_ = self.canvas.create_rectangle (self.cords, fill = self.color, outline = self.color)

                self.num_ = 2**self.pow_
                self.switc_ = False

                return self.num_
            
            else:
                return None
                
        else:
            if heh.x  in range (round(self.cords[0]), round(self.cords[2])) and heh.y in range (round(self.cords[1]),round(self.cords[3])):
                self.canvas.delete (self.actif_)
                self.actif_ = self.canvas.create_rectangle (self.cords2, fill = self.color2, outline = self.color2)

                self.num_ = 2**self.pow_
                self.switc_ = True

                return -1*(self.num_)

            else:
                return None
