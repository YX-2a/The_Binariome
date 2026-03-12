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
        self.bbox_pad = 20
        
    def create_levers (self,canvas,height,width,pow_):
        self.canvas = canvas
        self.pow_ = pow_
        self.cord2 = [width//2 - width//10,height*(10/13),width//2 + width//10,height*(10/13) + height//8]
        self.cords = [width//2 - width//10,height//10,width//2 + width//10,height//10 + height//8]
        self.color = self.inter_father.color_lvr
        self.lvid = self.canvas.create_rectangle (self.cord2, fill = self.color, outline = self.color)
        self.switc_ = True

    def change_ (self, heh):
        if self.switc_:
            if heh.x in range (round(self.cord2[0] * 0.888), round(self.cord2[2] * 1.07)) and heh.y in range (round(self.cord2[1] * 0.913),round(self.cord2[3] * 1.07)):
                self.canvas.delete (self.lvid)
                self.lvid = self.canvas.create_rectangle (self.cords, fill = self.color, outline = self.color)

                self.num_ = 2**self.pow_
                self.switc_ = False

                return self.num_
        else:
            if heh.x in range (round(self.cords[0] * 0.888), round(self.cords[2] * 1.07)) and heh.y in range (round(self.cords[1] * 0.666),round(self.cords[3] * 1.333)):
                self.canvas.delete (self.lvid)
                self.lvid = self.canvas.create_rectangle (self.cord2, fill = self.color, outline = self.color)

                self.num_ = 2**self.pow_
                self.switc_ = True

                return -1*(self.num_)