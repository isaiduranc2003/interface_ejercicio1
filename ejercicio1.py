
from tkinter import *
from tkinter import ttk



class Ejercicio1:
    def __init__(self,raiz):
        raiz.title("interface ejercicio 1")
        raiz.geometry('600x450')
        raiz.config(bg="gray")

        

        mainFrame = ttk.Frame(raiz,padding="0 0 0 0",width=600,relief="raised")
        mainFrame.grid()
        #mainFrame.geometry('600x450')
        mainFrame.pack(expand=True,fill="both")

        mainFrametabs = ttk.Frame(mainFrame,relief="raised")
        mainFrametabs.grid()
        #mainFrametabs.pack(expand=True,fill="both")

        mainFramespacio = ttk.Frame(mainFrame,relief="groove")
        mainFramespacio.grid(pady=10)

        mainFrame1 = ttk.Frame(mainFrame,relief="groove",padding="10 0 48 0")
        mainFrame1.grid(pady=5,sticky=W)

        mainFrame2 = ttk.Frame(mainFrame,relief="groove",padding="10 0 225 0")
        mainFrame2.grid(pady=5,sticky=W)

        mainFrame3 = ttk.Frame(mainFrame,relief="groove",padding="10 0 178 0")
        mainFrame3.grid(pady=20,sticky=W)

        mainFramebuton = ttk.Frame(mainFrame,relief="groove",padding="220 0 330 42")
        mainFramebuton.grid()

        #mainframetabs
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook.Tab",background="#00aae4",padding=[42.5,10])
        style.map("TNotebook.Tab",background=[("selected","#00aae4")])

        tabs = ttk.Notebook(mainFrametabs)
        tabs.pack()

        añadir = Frame(tabs)
        tabs.add(añadir,text="Add")

        borrar = ttk.Frame(tabs)
        tabs.add(borrar,text="Delete")

        buscar = ttk.Frame(tabs)
        tabs.add(buscar,text="Search")

        servicios = ttk.Frame(tabs)
        tabs.add(servicios,text="Services")

        ayuda = ttk.Frame(tabs)
        tabs.add(ayuda,text="Help")

        #mainframe 1
        
        ttk.Label(mainFrame1, text="First Name:",padding="30 0 0 0").grid(column=0,row=0,pady=20)
        nameEntry = ttk.Entry(mainFrame1,width=30)
        nameEntry.grid(column=1,row=0)
        ttk.Label(mainFrame1, text="Last Name:",padding="20 0 0 0").grid(column=2,row=0)
        lnameEntry = ttk.Entry(mainFrame1,width=30)
        lnameEntry.grid(column=3,row=0)
        ttk.Label(mainFrame1,text="Birth Date:",padding="30 0 0 0").grid(column=0,row=1)
        diaEntry = ttk.Entry(mainFrame1,width=5)
        diaEntry.grid(column=1,row=1,sticky=(W))
        mesEntry = ttk.Entry(mainFrame1,width=5)
        mesEntry.grid(column=1,row=1)
        añoEntry = ttk.Entry(mainFrame1,width=5)
        añoEntry.grid(column=1,row=1,sticky=(E))
        ttk.Label(mainFrame1,text="Country:").grid(column=2,row=1)
        countryEntry = ttk.Entry(mainFrame1)
        countryEntry.grid(column=3,row=1,sticky=W)


        #mainFrame2
        ttk.Label(mainFrame2,text="Credit card(if any):",padding="30 0 0 0").grid(column=0,row=0,sticky=(W),pady=20)
        creditcEntry = ttk.Entry(mainFrame2)
        creditcEntry.grid(column=1,row=0)
        ttk.Label(mainFrame2,text="Credit card Type(if any):",padding="30 0 0 0").grid(column=0,row=1)

        credittype = StringVar()
        visa = ttk.Radiobutton(mainFrame2,text="Visa",variable=credittype,value='visa')
        visa.grid(column=1,row=1)
        mastercard = ttk.Radiobutton(mainFrame2,text="MasterCard",variable=credittype,value='mastercard')
        mastercard.grid(column=2,row=1)

        #mainFrame3
        ttk.Label(mainFrame3,text="RoomType:",padding="30 0 0 0").grid(column=0,row=0,)
        roomtype = StringVar()
        normal = ttk.Radiobutton(mainFrame3,text="Normal",variable=roomtype,value='normal')
        normal.grid(column=1,row=0)
        familiar = ttk.Radiobutton(mainFrame3,text="Familiar",variable=roomtype,value='familiar')
        familiar.grid(column=1,row=1,pady=5)
        special = ttk.Radiobutton(mainFrame3,text="Special",variable=roomtype,value='apecial')
        special.grid(column=1,row=2)
        ttk.Label(mainFrame3,text="Total Staying Time(days):",padding="50 0 0 0").grid(column=2,row=0,padx=10)
        tstEntry = ttk.Entry(mainFrame3,width=8)
        tstEntry.grid(column=3,row=0)

        #mainframebutton
        ttk.Button(mainFramebuton,text="Submit").grid(pady=20)







raiz = Tk()
Ejercicio1(raiz)
raiz.mainloop()