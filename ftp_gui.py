from tkinter import*  
from tkinter import filedialog as fd
import ftplib 
base = Tk()  
base.geometry('500x500')  
base.title("FTP Server")

mylist = []



def ftp_protocol():
    try:
        ftp_server = ftplib.FTP(mylist[1], mylist[2], mylist[3])
        print(ftp_server.getwelcome())
        ftp_server.dir()
        fname = mylist[0].split('/')
        with open(mylist[0], "rb") as file:
            ftp_server.storbinary(f"STOR {fname[len(fname)-1]}", file)    
        global labl_4
        labl_4 = Label(base, text="File sent successfully", width=20,font=("bold", 10))  
        labl_4.place(x=180,y=450)  
        # labl_4.pack()
        mylist.clear()
        ftp_server.dir()
        ftp_server.close()
    except: 
        labl_4 = Label(base, text=f"Wrong Credentials", width=20,font=("bold", 10))  
        labl_4.place(x=180,y=450) 
        mylist.clear
def get_data(l):
    
    l.append(server_name.get())
    l.append(username.get())
    l.append(password.get())
    ftp_protocol()
    
def open_text_file(l):
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    l.append(fd.askopenfile(filetypes=filetypes).name)
    fname = mylist[0].split('/')
    labl_4 = Label(base, text=fname[len(fname)-1], font=("bold", 10))  
    labl_4.place(relx=0.5,y=350, anchor=CENTER) 



labl_0 = Label(base, text="FTP Server",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  

server_name = StringVar()
labl_1 = Label(base, text="FTP Server: ", width=20,font=("bold", 10))  
labl_1.place(x=80,y=130)  
entry_1 = Entry(base, textvariable=server_name)  
entry_1.place(x=240,y=130)  


username = StringVar()
labl_2 = Label(base, text="Username: ", width=20,font=("bold", 10))  
labl_2.place(x=80,y=150)  
entry_2 = Entry(base, textvariable=username)  
entry_2.place(x=240,y=150)


password = StringVar()
labl_3 = Label(base, text="Password: ", width=20,font=("bold", 10))  
labl_3.place(x=80,y=170)  
entry_3 = Entry(base, show="*",textvariable=password)  
entry_3.place(x=240,y=170)


Button(base, text='File to be Uploaded' , command=lambda:open_text_file(mylist)).place(x=200,y=300)  

Button(base, text='Submit' , command=lambda: get_data(mylist), width=20, bg="black",fg='white').place(x=180,y=380)  

    
 
base.mainloop() 

print(mylist)