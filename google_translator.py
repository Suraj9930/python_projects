from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob


root=Tk()
root.title("Google Translator")
root.geometry("1080x400")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)
    #this function will show which lang you had selected,both boxes

#translation
def translate_now():
    global language
    try:
        text_=text1.get(1,8,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1,8,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","plesae try again")                

#icon
#image_icon=PhotoImage(file="images.png")
#root.iconphoto(False,image_icon)

#arrow
#arrow_image=PhotoImage(file="are.png")
#image_label1=Label(root,image=arrow_image,width=150)
#image_label1.place.keys()

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")
#first box

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)
#will give big sized below box

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)
#will give a black box

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
#now we can write on that box

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)
#added scroll bar on that box

combo2=ttk.Combobox(root,values=languageV,font="Robot 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")
#second box

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)
#will give big sized below box

f1=Frame(root,bg="Black",bd=5)
f1.place(x=628,y=118,width=440,height=210)
#will give a black box

text2=Text(f1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)
#now we can write on that box

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)
#added scroll bar on that box both

#Translate Button
translate=Button(root,text="Translate",font="Robote 15 bold italic",
                 bg='red',fg="white",command=translate_now)
translate.place(x=470,y=250)

label_change()
#function called

root.configure(bg="white")
root.mainloop()


