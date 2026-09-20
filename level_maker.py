from tkinter import Tk, Canvas, Menu, Label, Button, PhotoImage, Toplevel
from interface import Interface, Lever
from level_reader import read_level
from os import listdir as LD

class Level:
    def __init__ (self, lvl_dir, hlp_img, def_lvl, skp_gd,icon_img,bg_clr, ib_clr, fg_clr):
        self.w = Tk()
        self.w.resizable (0,0)
        self.icon_img = PhotoImage (file = icon_img)
        self.w.iconphoto (0, self.icon_img)
        self.can_list = []
        self.ext = lvl_dir
        drek = LD (self.ext)
        self.dre = []
        for i in drek:
            if i == skp_gd or i[0] == ".":
                continue
            
            else:
                self.dre.append (i)
        
        self.fname, self.hlp_img, self.bcl, self.icl, self.fcl = def_lvl,hlp_img,bg_clr,ib_clr,fg_clr
        
    def about_ (self):
       self.abt = Toplevel(self.w)
       self.abt.title ("About")
       self.abt.iconphoto (0, self.icon_img)
       self.abt.resizable (0,0)
       
       self.img = PhotoImage (file=self.hlp_img).subsample(2, 2)
       abt_text = Label (self.abt, image = self.img)

       abt_text.pack()
       self.abt.mainloop()
       
    def menu_ (self):
        self.men_  = Menu (self.w)
        self.w.config (menu = self.men_)
        men_lev = Menu (self.men_, tearoff = 0)
        
        for i, btn_lev in enumerate (self.dre) :
            self.btn_i = men_lev.add_radiobutton (label=btn_lev)
            men_lev.entryconfig(i, command=lambda btn_lev=btn_lev: self.next_er(btn_lev))
            
        men_abt = Menu (self.men_, tearoff = 0)
        men_abt.add_command (label="About", command = self.about_)
        men_abt.add_separator()
        men_abt.add_command (label="Quit", command = self.w.destroy)

        self.men_.add_cascade (menu = men_lev,label="Levels")
        self.men_.add_command (label="Refresh", command = lambda nibler = self.fname : self.next_er (self.fname) )
        self.men_.add_cascade (menu = men_abt,label="About")
            
    def next_er (self, fname):
        self.reload ()
        options = read_level (self.ext + fname)
        self.fname = fname
        self.make_level (options[0],options[1],options[2],options[3],options[4])
        
    def make_level (self, title, height, width, gl, canl):
        self.w.title (title + " | Goal : " + str(gl))
        self.opera_ = 0
        for ca in canl:
            if ca[2] == True:
                terface_ = Interface(self.bcl, self.icl, self.fcl)
                terface_.create_canvas (self.w,height,width,ca[1],ca[0])
                lever_= Lever(terface_)
                lever_.create_levers (terface_.can_,height,width,canl.index(ca))
                self.can_list.append (terface_.can_)

                def handle (heh, lev=lever_):
                    val =  lev.change_(heh)
                    if val is not None:
                        self.opera_ += val

                        if self.opera_ == gl:
                            self.w.title (title + " | Goal : " + str(gl) + " = " + str(self.opera_))

                        else:
                            self.w.title (title + " | Goal : " + str(gl) + " ≠ " + str(self.opera_))

                terface_.can_.bind ("<Button-1>", handle)
                    
            else:
                terface_ = Interface(self.bcl, self.icl, self.fcl)
                terface_.create_canvas (self.w,height,width,ca[1],ca[0])
                self.can_list.append (terface_.can_)
        
    def reload (self):
        self.w.title ("")

        for can in self.can_list:
            can.destroy ()
            
        self.w.update()
        
    def end_ (self):
        self.w.mainloop()
