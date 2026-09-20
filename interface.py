from tkinter import Canvas

class Lever:
    def __init__ (self):
        self.actif_ = ""
        self.switc_ = False
        
    def create_levers (self,canvas,cords,color,cords2,color2): ##dont play with switc_ or you will suffer
        self.actif_ = canvas.create_rectangle (cords, fill = color) ## because of this bitch
        self.switc_ = False
        
        def change_ (heh):
            if self.switc_:
                if heh.x  in range (round(cords2[0]), round(cords2[2])) and heh.y in range (round(cords2[1]),round(cords2[3])):
                    canvas.delete (self.actif_)
                    self.actif_ = canvas.create_rectangle (cords, fill = color)

                    self.switc_ = False
                    
                else:
                    None
                    
            else:
                if heh.x  in range (round(cords[0]), round(cords[2])) and heh.y in range (round(cords[1]),round(cords[3])):
                    canvas.delete (self.actif_)
                    self.actif_ = canvas.create_rectangle (cords2, fill = color2)

                    self.switc_ = True

                else:
                    None

        canvas.bind ("<Button-1>", change_)

class Interface:
    def __init__ (self):
        self.color = "#aaaaaa"
        self.color_line = "#909090"
        
    def create_canvas (self,parent, height, width):
        self.can_ = Canvas (parent, height = height, width = width,bg = self.color )
        self.lien_ = self.can_.create_line (height//2 + height//10,width*(1/6) - width//30,height//2 + height//10,width*(4/6) + width//10,width = 5, fill = self.color_line)
        self.can_.pack (side = "left")
