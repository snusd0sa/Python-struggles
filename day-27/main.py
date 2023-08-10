import tkinter

window = tkinter.Tk()
window.title("My first tkinter prog")
window.minsize(500,500)

#Create a Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 22 ,"bold"))
my_label.pack()




class Car:
    def __init__(self, **kw):
        #self.make = kw["make"]
        self.make = kw.get("make") #if provided, else becomes 'None'
        #self.model = kw["model"]
        self.model = kw.get("model")
my_car = Car(make="nissan",model = "ful")

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)

def test(*args):
    print(args)
 
test(1,2,3,5)

my_label["text"] = "new text"
my_label.config(text="Newer text")

# can use   from tkinter import *
# to use button = Button() etc wihtout needint tkinter.Button

#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)
    print("I got clicked!!!")


# Input
input = tkinter.Entry(width=10)
input.pack()
inp = input.get()

button = tkinter.Button(text = "Click click", command = button_clicked)
button.pack()


window.mainloop()






