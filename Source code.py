import Tkinter as tk   # python3
#import Tkinter as tk   # python
import pickle

TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Pageone, Pagetwo,amritsar,kanpur,jaipur,meerut,agra,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=" WELCOME TO My Cabs", font=TITLE_FONT,fg="yellow",bg="black")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="BOOK NOW",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("Pageone"))


        button2 = tk.Button(self, text="TO CANCEL",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("Pagetwo"))
        button1.pack()
        label = tk.Label(self, text="\n", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)


        button2.pack()


class Pageone(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="choose your destination", font=TITLE_FONT,fg="yellow",bg="black",)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="AMRITSAR",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("amritsar"))
        button2 = tk.Button(self, text="KANPUR",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("kanpur"))
        button3 = tk.Button(self, text="AGRA",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("agra"))
        button4 = tk.Button(self, text="MEERUT",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("meerut"))
        button5 = tk.Button(self, text="JAIPUR",fg="yellow",bg="black",
                            command=lambda: controller.show_frame("jaipur"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()



class destination:
            perkm=12

            def __init__(self,dest,distance):
                self.dest=dest
                self.distance=distance

            def display(self):


                price=destination.perkm *(self.distance)
                print price
fh=open("binary.dat","wb+")
amritsar=destination("amritsar",400)
kanpur=destination("kanpur",350)
agra=destination("agra",150)
jaipur=destination("jaipur",240)
meerut=destination("meerut",80)
pickle.dump(jaipur,fh)
pickle.dump(amritsar,fh)
pickle.dump(kanpur,fh)
pickle.dump(agra,fh)
pickle.dump(meerut,fh)


fh.close()


class amritsar(tk.Frame,destination):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="AMRITSAR", font=TITLE_FONT,)


        fh=open("binary.dat","rb")
        def __init__(self,dest,distance):

           destination.__init__(self,dest,distance)





        try:
            while True:
                           m=pickle.load(fh)
                           tdestination=m.dest


                           if tdestination == "amritsar":
                                 price =int(m.distance)*12

                                 str1= str(m.distance)
                                 destination=m.dest
                                 price=str(price)
                                 string1="Your Destination:"+destination+"\n"+"\n"+"\n"+"Trip Cost:"+price+"\n"+"\n"+"\n"+"Select payment method:"

        except EOFError:
                           pass
        fh.close()
        label = tk.Label(self, text=string1, font=TITLE_FONT)

        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="paytm",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
        button1.pack()
        button2 = tk.Button(self, text="cash",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
        button2.pack()
class kanpur(tk.Frame,destination):

 def __init__(self, parent, controller):

    tk.Frame.__init__(self, parent)
    self.controller = controller

    label = tk.Label(self, text="KANPUR", font=TITLE_FONT,)


    fh=open("binary.dat","rb")
    def __init__(self,dest,distance):

       destination.__init__(self,dest,distance)
    try:

            while True:
                           m=pickle.load(fh)
                           tdestination=m.dest


                           if tdestination == "kanpur":
                                 price =int(m.distance)*12
                                 str1= str(m.distance)
                                 destination=m.dest
                                 price=str(price)
                                 string1="Your Destination:"+destination+"\n"+"Trip Cost:"+ price+"\n"+"\n"+"\n"+"Select payment method:"
    except EOFError:
                           pass
    fh.close()
    label = tk.Label(self, text=string1, font=TITLE_FONT)

    label.pack(side="top", fill="x", pady=10)

    button1 = tk.Button(self, text="paytm",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
    button1.pack()
    button2 = tk.Button(self, text="cash",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
    button2.pack()
class agra(tk.Frame,destination):

    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="agra", font=TITLE_FONT)


        fh=open("binary.dat","rb")
        def __init__(self,dest,distance):

           destination.__init__(self,dest,distance)
           try:

            while True:
                           m=pickle.load(fh)
                           tdestination=m.dest


                           if tdestination == "agra":
                                 price =int(m.distance) *12

                                 str1= str(m.distance)
                                 destination=m.dest
                                 price=str(price)
                                 string1="Your Destination:"+destination+"\n"+"Trip Cost:"+price+"\n"+"\n"+"\n"+"Select payment method:"
           except EOFError:
                           pass
           fh.close()
           label = tk.Label(self, text=string1, font=TITLE_FONT)

           label.pack(side="top", fill="x", pady=10)

           button1 = tk.Button(self, text="paytm",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
           button1.pack()
           button2 = tk.Button(self, text="cash",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
           button2.pack()


class meerut(tk.Frame,destination):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="meerut", font=TITLE_FONT)


        fh=open("binary.dat","rb")
        def __init__(self,dest,distance):

           destination.__init__(self,dest,distance)
           try:

             while True:
                           m=pickle.load(fh)
                           tdestination=m.dest


                           if tdestination == "meerut":
                                 price =int(m.distance)*12

                                 str1= str(m.distance)
                                 destination=m.dest
                                 price=str(price)
                                 string1="Your Destination:"+destination+"\n"+"Trip Cost:"+price+"\n"+"\n"+"\n"+"Select payment method:"
           except EOFError:
                           pass
           fh.close()
           label = tk.Label(self, text=string1, font=TITLE_FONT)

           label.pack(side="top", fill="x", pady=10)

           button1 = tk.Button(self, text="paytm",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
           button1.pack()
           button2 = tk.Button(self, text="cash",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
           button2.pack()
class jaipur(tk.Frame,destination):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="jaipur", font=TITLE_FONT)


        fh=open("binary.dat","rb")
        def __init__(self,dest,distance):

           destination.__init__(self,dest,distance)
           try:

            while True:
                           m=pickle.load(fh)
                           tdestination=m.dest


                           if tdestination == "jaipur":
                                 price =int(m.distance)*12

                                 str1= str(m.distance)
                                 destination=m.dest
                                 price=str(price)
                                 string1="Your Destination:"+destination+"\n"+"Trip Cost:"+price+"\n"+"\n"+"\n"+"Select payment method:"
           except EOFError:
                           pass
           fh.close()
           label = tk.Label(self, text=string1, font=TITLE_FONT)

           label.pack(side="top", fill="x", pady=10)

           button1 = tk.Button(self, text="paytm",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
           button1.pack()
           button2 = tk.Button(self, text="cash",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("Pagetwo")
                           )
           button2.pack()

class Pagethree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="click your desired destination", font=TITLE_FONT)

        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="",
                           command=lambda: controller.show_frame("StartPage")
                           )
        button.pack()


class Pagetwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Thank You For Choosing My Cabs", font=TITLE_FONT,fg="yellow",bg="black")
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="pay your fare with the selected method after the ride is completed", font=TITLE_FONT,fg="yellow",bg="black")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Book another cab",fg="yellow",bg="black",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
