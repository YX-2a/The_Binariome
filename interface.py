from tkinter import Canvas

class Lever:
    def __init__ (self):
        self.actif_ = ""
        self.switc_ = False
        
    def create_levers (self,canvas,height,width): ##dont play with switc_ or you will suffer
        self.cords = [height//2,width*(1/6),height//2 + height//5,width*(1/6) + width//15]
        self.cords2 = [height//2,width*(4/6),height//2 + height//5,width*(4/6) + width//15]
        self.color = "#000000"
        self.color2 = self.color
        self.actif_ = canvas.create_rectangle (self.cords, fill = self.color) ## because of this bitch
        self.switc_ = False
        
        def change_ (heh):
            if self.switc_:
                if heh.x  in range (round(self.cords2[0]), round(self.cords2[2])) and heh.y in range (round(self.cords2[1]),round(self.cords2[3])):
                    canvas.delete (self.actif_)
                    self.actif_ = canvas.create_rectangle (self.cords, fill = self.color)

                    self.switc_ = False
                    
                else:
                    None
                    
            else:
                if heh.x  in range (round(self.cords[0]), round(self.cords[2])) and heh.y in range (round(self.cords[1]),round(self.cords[3])):
                    canvas.delete (self.actif_)
                    self.actif_ = canvas.create_rectangle (self.cords2, fill = self.color2)

                    self.switc_ = True

                else:
                    None

        canvas.bind ("<Button-1>", change_)

class Interface:
    def __init__ (self):
        self.color = "#aaaaaa"
        self.color_line = "#909090"
        
    def create_canvas (self,parent, height, width, side_ # = "top" | "bottom" | "left" | "right"
                       ):
        self.can_ = Canvas (parent, height = height, width = width,bg = self.color )
        self.lien_ = self.can_.create_line (height//2 + height//10,width*(1/6) - width//30,height//2 + height//10,width*(4/6) + width//10,width = 5, fill = self.color_line)
        self.can_.pack (side = side_)
