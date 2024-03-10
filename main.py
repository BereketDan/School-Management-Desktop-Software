################################################## Import Library ####################################################



import os
import csv
import cv2
import time
import qrcode
import sqlite3
import winsound
from tkinter import*
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
from tkinter import messagebox
from pyzbar.pyzbar import decode




############################################### Setup Desktop Layout #################################################

def dest():
    of.destroy()
of =Tk()
of.overrideredirect(2)

w=650
h=430

sw = of.winfo_screenwidth()
sh = of.winfo_screenheight()
x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
of.geometry("%dx%d+%d+%d" % (w,h,x,y))
img = PhotoImage(file='splash.png')
Label(of,image=img).pack()
of.resizable(0,0)
of.after(1,dest)

#of.attributes('-alpha',0.95)
of.mainloop()



root = Tk()
root.title(""" \t School of Marvel """)
root['background']='#222'
root.iconbitmap("cloud.ico")







################################################## Absetnt Students ####################################################

global noow
global date_now
noow = datetime.now()
date_now = noow.strftime("20%y-%m-%d")



def ABdata():
    ab=Tk()
    
    ab.title('Today Record')
    framey = Frame(ab, width=925, height=76,bg='#333').place(x=8,y=468)
        
    framex = Frame(ab, width=941, height=88,bg='white').place(x=0,y=0)
    lb = Label(ab,text='Absent Students',fg='#006aff',bg='white',font=('Arail',15,'bold')).place(x=155,y=27)
    lb = Label(ab,text='Late Students',fg='#006aff',bg='white',font=('Arail',15,'bold')).place(x=610,y=27)
    lb = Label(ab,text=f'{date_now}',fg='#888',bg='#333',font=('Arail',14,'normal')).place(x=630,y=490)
    
    def land():
        
  
        style = ttk.Style()
        style.map('Treeview',background=[('selected','#6957D9')])
        mt = ttk.Treeview(ab,height=17)
        mt['columns']=('Student_Name','Grade','Section','Date','Parent_Phone')
        
            
        mt.column('#0',width=0)
        
        mt.column('Student_Name',width=146,anchor=W)
        mt.column('Grade',width=45,anchor=W)
        mt.column('Section',width=48,anchor=W)
        mt.column('Date',width=75,anchor=W)
        mt.column('Parent_Phone',width=113,anchor=W)

        

        


        mt.heading('#0',text='',anchor=W)
        
        mt.heading('Student_Name',text='Student Name',anchor=W)
        mt.heading('Grade',text='Grade',anchor=W)
        mt.heading('Section',text='Section',anchor=W)
        mt.heading('Date',text='Date',anchor=W)
        mt.heading('Parent_Phone',text='Parent Phone',anchor=W)

        conn = sqlite3.connect('AbsentDb.db')
        i = conn.cursor()
        gdd = gxs.get()
        scc = str(sxs.get())
        i.execute(f"SELECT * FROM AbsentDB WHERE DateA = DATE('now') AND Grade = '"+ gdd +"' AND Section = '"+ scc +"' ")
        inames = i.fetchall()
        cot = 0
        
        
        for name in inames:
          
            mt.insert(parent='',index='end',iid=cot,values=(name[0],name[1],name[2],name[3],name[4],name[5]))
            cot = cot + 1
        mt.place(x=8,y=95)


        for name in inames:
            print

        

        stylee = ttk.Style()
        stylee.map('Treeview',background=[('selected','#6957D9')])
        mit = ttk.Treeview(ab,height=17)
        mit['columns']=('Student_Name','Grade','Section','Date','Time','Parent_Phone')
        
            
        mit.column('#0',width=0)
        
        mit.column('Student_Name',width=140,anchor=W)
        mit.column('Grade',width=45,anchor=W)
        mit.column('Section',width=48,anchor=W)
        mit.column('Date',width=72,anchor=W)
        mit.column('Time',width=67,anchor=W)
        mit.column('Parent_Phone',width=109,anchor=W)





        


        mit.heading('#0',text='',anchor=W)
        
        mit.heading('Student_Name',text='Student Name',anchor=W)
        mit.heading('Grade',text='Grade',anchor=W)
        mit.heading('Section',text='Section',anchor=W)
        mit.heading('Date',text='Date',anchor=W)
        mit.heading('Time',text='Time',anchor=W)
        mit.heading('Parent_Phone',text='Parent Phone',anchor=W)

        conn = sqlite3.connect('LateDb.db')
        i = conn.cursor()
        i.execute("SELECT * FROM LateDB WHERE DateA = DATE('now') AND Grade = '"+ gdd +"' AND Section = '"+ scc +"'")
        inames = i.fetchall()
        cot = 0
        
        
        for name in inames:
          
            mit.insert(parent='',index='end',iid=cot,values=(name[0],name[1],name[2],name[3],name[4],name[5],name[6]))
            cot = cot + 1
        mit.place(x=448,y=95)





    gxs = ttk.Combobox(ab, width = 28)
    gxs['values'] = (9,10,11,12)
      
    gxs.place(x=14,y=476)
    gxs.current(0)

    sxs = ttk.Combobox(ab, width = 28)
      
    # Adding combobox drop down list
    sxs['values'] = ('A','B','C','D')
      
    sxs.place(x=247,y=476)
    sxs.current(0)

    sbtn = Button(ab,text='Show Data',width=59,bg="#006aff",fg='white',relief = FLAT,command = land).place(x=14 ,y=512)

    
    
            
            
    ab.geometry("940x550")
    ab.resizable(0,0)
    ab.mainloop()





################################################## Camera and QR-Code  ####################################################



            

def Atd():
   
    Dtime=(time.strftime ("%I:%M:%S"))
    cap = cv2.VideoCapture(0)
    
    students = []
    conn = sqlite3.connect("StudentDb.db")
    c = conn.cursor()

    c.execute("SELECT * FROM StudentDB")
    reader = c.fetchall()


    for row in reader:
        students.append((row[1]))
        


    while True:
        re,frame = cap.read()
        d=decode(frame)
        
        
        try:
            for obj in d:
               
               
                naame = d[0].data.decode()
                
               
                
               
                if naame in students:
                    
                    
                    winsound.Beep(1000,100)
                    students.remove(naame)
                    print("deleted...",naame,Dtime)



                    
                    c.execute("SELECT * FROM StudentDB WHERE Student_Name = '"+ naame +"'")
                    grade = c.fetchall()
                    print(grade)
                    
                    for grad in grade:
                       print(grade)






                    #if 2<=x and 4>=x or 6<=x and 8>=x:
                    #    print("correct",x)
                    #else:
                    #    print('ops')

                    # here will customize time



                    
                    if "2:20:00">= Dtime:
                        
                       c.execute("SELECT * FROM StudentDB WHERE Student_Name = '"+ naame +"'")
                       grade = c.fetchall()
                       print(grade)
                       for grad in grade:
##                       
                           print(grad[0],grad[1],grad[2],grad[3],grad[4],grad[5],grad[6],grad[7],grad[8],grad[9],grad[10])
##                    
                       for grad in grade:
                            conn = sqlite3.connect('LateDb.db')
                            m = conn.cursor()
                           
                            MainDB = [grad[1],grad[2],grad[3],date_now,Dtime,grad[10],1]
                            
                            m.execute("INSERT INTO LateDB VALUES (?,?,?,?,?,?,?);",MainDB)
                            

                            conn.commit()
                            conn.close()
                           
                        
                     
        except:
            
            print("Erorr")
            
        cv2.imshow('Attendance QR-Code',frame)
        key = cv2.waitKey(1)
        
        
        if key == ord("b"):
            
            try:
                for stu in students:
                    c.execute("SELECT * FROM StudentDB WHERE Student_Name = '"+ stu +"'")
                    All = c.fetchall()
                    for al in All:
                        data = [al[0],al[1],al[2],al[3],al[4],al[5],al[6],al[7],al[8],al[9],al[10]]

                        conn = sqlite3.connect('AbsentDb.db')
                        m = conn.cursor()
                       
                        MainDB = [al[1],al[2],al[3],date_now,al[10],1]
                        
                        m.execute("INSERT INTO AbsentDB VALUES (?,?,?,?,?,?);",MainDB)
                        

                        conn.commit()
                        conn.close()
                        
##                        f = open('AbsentStudent.txt', 'a',newline='')
##                        f.write(f'{All} \n \n ')
                        print(al[0],al[1],al[2],al[3],al[4],al[5],al[6],al[7],al[8],al[9],al[10])
            
            except:
                print("it's okay")
        
            break

    
    
        
    cap.release()
    cv2.destroyAllWindows()





################################################## Analyize Data     ####################################################







def ana():
    vd=Tk()
    vd.title('Analyze Data')


    def later():
        print(uname.get(),gd.get(),dname.get(),sc.get())
        style = ttk.Style()
        style.map('Treeview',background=[('selected','#6957D9')])
        mt = ttk.Treeview(vd,height=16)
        mt['columns']=('Date','Time')
        
            
        mt.column('#0',width=0)
        mt.column('Date',width=150,anchor=W)
        mt.column('Time',width=165,anchor=W)
      



        


        mt.heading('#0',text='',anchor=W)
        mt.heading('Date',text='Date',anchor=W)
        mt.heading('Time',text='Time',anchor=W)
   

        conn = sqlite3.connect('LateDb.db')
        i = conn.cursor()
        
        i.execute("SELECT * FROM LateDB WHERE Student_Name LIKE ? AND Grade = ? AND Section = ? AND DateA LIKE ?" ,('%' + str(uname.get()) + '%' , gd.get() , str(sc.get()) ,'%' + str(dname.get())  + '%'))
        names = i.fetchall()
        cot = 0
    
        for name in names:
            lb = Label(vd, text=f'{name[0]}',fg='#006aff',font=('arial',14,'bold')).place(x=545,y=10)

            ans = Frame(vd, width=318, height=32,bg="#333")
            ans.place(x=400,y=448)
            mt.insert(parent='',index='0',iid=cot,values=(name[3],name[4]))
            cot = cot + 1
        mt.place(x=400,y=90)



        



        style = ttk.Style()
        style.map('Treeview',background=[('selected','#6957D9')])
        mt = ttk.Treeview(vd,height=16)
        mt['columns']=('Date')
        
            
        mt.column('#0',width=0)
        mt.column('Date',width=160,anchor=W)
       
      



        


        mt.heading('#0',text='',anchor=W)
        mt.heading('Date',text='Date',anchor=W)
        
   

        con = sqlite3.connect('AbsentDb.db')
        il = con.cursor()
        
        il.execute("SELECT * FROM AbsentDB WHERE Student_Name LIKE ? AND Grade = ? AND Section = ? AND DateA LIKE ?" ,('%' + str(uname.get()) + '%' , gd.get() , str(sc.get()) ,'%' + str(dname.get())  + '%'))
        names = il.fetchall()
        cot = 0
        global j
        j = 0
        for name in names:
            
            j = j + name[5]
            
            
            lb = Label(vd, text=f'{name[0]}',fg='#006aff',font=('arial',14,'bold')).place(x=545,y=10)

            ans = Frame(vd, width=162, height=32,bg="#333")
            ans.place(x=740,y=448)

            
            

            
       
            mt.insert(parent='',index='0',iid=cot,values=(name[3]))
            cot = cot + 1

        lb = Label(vd, text=f'{j} times',fg='#fff',bg='#333',font=('arial',11,'normal')).place(x=765,y=451)
        mt.place(x=740,y=90)



        



        
    side_bar = Frame(vd, width=360, height=550,bg="#006aff")
    side_bar.place(x=0,y=0)   

    lb = Label(vd, text='User Info',bg='#006aff',fg='white',font=('arial',15,'normal')).place(x=130,y=90)
    lb = Label(vd, text=f'{date_now}',fg='#888',font=('arial',13,'normal')).place(x=840,y=10)

    
    lb = Label(vd, text='Username',bg='#006aff',fg='white').place(x=79,y=150)
    lb = Label(vd, text='Date',bg='#006aff',fg='white').place(x=80,y=210)
    lb = Label(vd, text='Grade',bg='#006aff',fg='white').place(x=80,y=264)
    lb = Label(vd, text='Section',bg='#006aff',fg='white').place(x=80,y=313)
    
    uname = Entry(vd,width=34,highlightthickness=1,fg='#555')
    uname.place(x=80,y=175)

    dname = Entry(vd,width=34,highlightthickness=1,fg='#555')
    dname.place(x=80,y=230)



    gd = ttk.Combobox(vd, width = 31)
      


    gd['values'] = (9,10,11,12)
      
    gd.place(x=80,y=284)
    gd.current(0)




    sc = ttk.Combobox(vd, width = 31)
      


    sc['values'] = ('A','B','C','D')
      
    sc.place(x=80,y=335)
    sc.current(0)







    
    
    








    Btn=Button(vd,text='Submit',fg='#fff',bg='#006aff',font=('arial',13,'normal'),width=15,relief=FLAT,command=later).place(x=186,y=377)
      
    
    vd.geometry("940x550")
    vd.resizable(0,0)
    vd.mainloop()
    





################################################## Show full Database ####################################################






def Dashboard():
    dash = Tk()
    dash['background']='#222'
    dash.title('Dashboard ')
    dash.iconbitmap("MEmu.ico")
    def how():
        src = Tk()
        src['background']='#222'
        src.title('Search Result ')
        src.iconbitmap("app.ico")
        L1 = Label(src,text="Search Result....",font=('arial',11,'normal'),bg='#333',fg='orange').pack(pady=10,ipady=10,ipadx=100)
    
        frame_top = Frame(src, width=200, height=550)
        frame_top.pack(side="top", expand=2, fill= "both" )


        sf = ScrolledFrame(frame_top, width=380, height=205)
        sf.pack(side="top", expand=2, fill="both")


        sf.bind_arrow_keys(frame_top)
        sf.bind_scroll_wheel(frame_top)

        frame = sf.display_widget(Frame)
        dog = Ent.get()
        conn = sqlite3.connect("StudentData.db")
        c = conn.cursor()
        c.execute("SELECT * FROM studenets WHERE Students_Name LIKE ? ",('%' + str(Ent.get()) + '%',))
    
        items = c.fetchall()
        for item in items:
            L1 = Label(frame,text=item,font=('arial',12,'normal'),fg='#333').pack(pady=12,ipady=10,padx=9)



        def clear_text():
           Ent.delete(0, END)
        clear_text()  
        src.geometry("410x610")
        src.resizable(0,0)
        src.mainloop() 
        
        
    L1 = Label(dash,text="Dashboard Student Data",font=('arial',11,'normal'),bg='#333',fg='orange').pack(pady=10,ipady=10,ipadx=120)
    Ent = Entry(dash ,width=45,fg='#555',font=('arial',12))
    Ent.pack(ipady=4)  
    B1 = Button(dash, text='Search',command=how,font=('arial',10,'normal'),relief=FLAT,bg='#222',fg='#fff')
    B1.pack(pady=4,ipadx=140)
    
    
              

    frame_top = Frame(dash, width=400, height=550)
    frame_top.pack(side="top", expand=2, fill= "both" )


    sf = ScrolledFrame(frame_top, width=380, height=205)
    sf.pack(side="top", expand=2, fill="both")


    sf.bind_arrow_keys(frame_top)
    sf.bind_scroll_wheel(frame_top)

    frame = sf.display_widget(Frame)
   
    

   
    conn = sqlite3.connect("StudentData.db")
    c = conn.cursor()

    c.execute("SELECT * FROM studenets")
    r = c.fetchall()
    num = 2
    for i in r:
        
        Log = Label(frame ,text = i[0] ,font=('arial',11,'normal')).grid( row = num ,column =0, padx=10,pady=10)
        Log = Label(frame ,text = i[1],font=('arial',11,'normal')).grid(row = num ,column =1, padx=10,pady=10)
        Log = Label(frame ,text = i[2],font=('arial',11,'normal')).grid(row = num ,column =2, padx=10,pady=10)
        Log = Label(frame ,text = i[3],font=('arial',11,'normal')).grid(row = num ,column =3, padx=10,pady=10)
        num = num + 1


    
    
    
    dash.geometry("940x550")
    dash.resizable(0,0)
    dash.mainloop()





################################################## Registraion Code ####################################################


global var
var = StringVar()

def Addstudent():
    ads = Tk()
    
    #ads['background']='#222'
    ads.title('Registeration Section')
    #ads.iconbitmap("wpsbox.ico")
    
    style = ttk.Style()
    style.map('Treeview',background=[('selected','#6957D9')])
    mt = ttk.Treeview(ads,height=13)
    mt['columns']=('ID_NO','Student_Name','Grade','Section','Sex','Age','Region','Town','Kebele','Parent_Name','Parent_Phone')
    
        
    mt.column('#0',width=0)
    mt.column('ID_NO',width=30,anchor=W)
    mt.column('Student_Name',width=130,anchor=W)
    mt.column('Grade',width=70,anchor=W)
    mt.column('Section',width=60,anchor=W)
    mt.column('Sex',width=60,anchor=W)
    mt.column('Age',width=60,anchor=W)
    mt.column('Region',width=100,anchor=W)
    mt.column('Town',width=100,anchor=W)
    mt.column('Kebele',width=60,anchor=W)
    mt.column('Parent_Name',width=130,anchor=W)
    mt.column('Parent_Phone',width=120,anchor=W)





    


    mt.heading('#0',text='',anchor=W)
    mt.heading('ID_NO',text='ID',anchor=W)
    mt.heading('Student_Name',text='Student Name',anchor=W)
    mt.heading('Grade',text='Grade',anchor=W)
    mt.heading('Section',text='Section',anchor=W)
    mt.heading('Sex',text='Sex',anchor=W)
    mt.heading('Age',text='Age',anchor=W)
    mt.heading('Region',text='Region',anchor=W)
    mt.heading('Town',text='Town',anchor=W)
    mt.heading('Kebele',text='Kebele',anchor=W)
    mt.heading('Parent_Name',text='Parent Name',anchor=W)
    mt.heading('Parent_Phone',text='Parent Phone',anchor=W)

    conn = sqlite3.connect('StudentDb.db')
    i = conn.cursor()
    i.execute("SELECT * FROM StudentDB ")
    inames = i.fetchall()
    cot = 0
    
    for name in inames:
      
        mt.insert(parent='',index='end',iid=cot,values=(name[0],name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9],name[10]))
        cot = cot + 1
    mt.place(x=8,y=35)
    
    Label(ads,text="School Of Marvel" ,fg="white",bg="#006aff",width=75).place(x=8,y=6)

    conn.commit()
        
    def searchView():
        sdf = Tk()
    
        #ads['background']='#222'
        sdf.title('Search Result')
        #ads.iconbitmap("wpsbox.ico")
        Label(sdf,text="Search Result" ,fg="white",bg="#006aff",width=131).place(x=8,y=6)
        style = ttk.Style()
        style.map('Treeview',background=[('selected','#6957D9')])
        mt = ttk.Treeview(sdf,height=23)
        mt['columns']=('ID_NO','Student_Name','Grade','Section','Sex','Age','Region','Town','Kebele','Parent_Name','Parent_Phone')
        
            
        mt.column('#0',width=0)
        mt.column('ID_NO',width=30,anchor=W)
        mt.column('Student_Name',width=130,anchor=W)
        mt.column('Grade',width=70,anchor=W)
        mt.column('Section',width=60,anchor=W)
        mt.column('Sex',width=60,anchor=W)
        mt.column('Age',width=60,anchor=W)
        mt.column('Region',width=100,anchor=W)
        mt.column('Town',width=100,anchor=W)
        mt.column('Kebele',width=60,anchor=W)
        mt.column('Parent_Name',width=130,anchor=W)
        mt.column('Parent_Phone',width=120,anchor=W)





        


        mt.heading('#0',text='',anchor=W)
        mt.heading('ID_NO',text='ID',anchor=W)
        mt.heading('Student_Name',text='Student Name',anchor=W)
        mt.heading('Grade',text='Grade',anchor=W)
        mt.heading('Section',text='Section',anchor=W)
        mt.heading('Sex',text='Sex',anchor=W)
        mt.heading('Age',text='Age',anchor=W)
        mt.heading('Region',text='Region',anchor=W)
        mt.heading('Town',text='Town',anchor=W)
        mt.heading('Kebele',text='Kebele',anchor=W)
        mt.heading('Parent_Name',text='Parent Name',anchor=W)
        mt.heading('Parent_Phone',text='Parent Phone',anchor=W)

        conn = sqlite3.connect('StudentDb.db')
        i = conn.cursor()
        
        i.execute("SELECT * FROM StudentDB WHERE Student_Name LIKE ? OR Grade LIKE ? OR Section LIKE ?",('%' + str(srcF.get()) + '%','%' + srcF.get()  + '%','%' + str(srcF.get())  + '%'))
        names = i.fetchall()
        cot = 0
    
        for name in names:
       
            mt.insert(parent='',index='0',iid=cot,values=(name[0],name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9],name[10]))
            cot = cot + 1
        mt.place(x=8,y=35)
        sdf.geometry("940x550")
        sdf.resizable(0,0)
        sdf.mainloop()
    def clear_text():
        fname.delete(0, END)
        pnum.delete(0, END)
        pname.delete(0, END)
        
    def submit():
      
        grad = monthchoosen.get()
        sect = gx.get()
        nname = fname.get()
        gend = gen.get()
        ag = ege.get()
        kb = keb.get()
        pnumm = pnum.get()
        pnamee = pname.get()
        
        img = qrcode.make(nname)
        img.save(f"QRcd/{nname}.jpg")
        print(nname,grad,sect,gend,ag,"Oromiya","Asella",kb,pnamee,pnumm)
        
        conn = sqlite3.connect('StudentDb.db')
        m = conn.cursor()
       
        MainDB = [None,nname,grad,sect,gend,ag,"Oromiya","Asella",kb,pnamee,pnumm]
        
        m.execute("INSERT INTO StudentDB VALUES (?,?,?,?,?,?,?,?,?,?,?);",MainDB)
        

        conn.commit()
        conn.close()

        clear_text()

    def orgs():
        org = Tk()
    
        #ads['background']='#222'
        org.title('Search Result')
        #ads.iconbitmap("wpsbox.ico")
        
        style = ttk.Style()
        style.map('Treeview',background=[('selected','#6957D9')])
        mt = ttk.Treeview(org,height=24)
        mt['columns']=('ID_NO','Student_Name','Grade','Section','Sex','Age','Region','Town','Kebele','Parent_Name','Parent_Phone')
        
            
        mt.column('#0',width=0)
        mt.column('ID_NO',width=30,anchor=W)
        mt.column('Student_Name',width=130,anchor=W)
        mt.column('Grade',width=70,anchor=W)
        mt.column('Section',width=60,anchor=W)
        mt.column('Sex',width=60,anchor=W)
        mt.column('Age',width=60,anchor=W)
        mt.column('Region',width=100,anchor=W)
        mt.column('Town',width=100,anchor=W)
        mt.column('Kebele',width=60,anchor=W)
        mt.column('Parent_Name',width=130,anchor=W)
        mt.column('Parent_Phone',width=120,anchor=W)





        Label(org,text=f'Grade  {str(gxs.get())}  |  Section  {sxs.get()}',fg="white",bg="#006aff",width=131).place(x=8,y=5)
    


        mt.heading('#0',text='',anchor=W)
        mt.heading('ID_NO',text='ID',anchor=W)
        mt.heading('Student_Name',text='Student Name',anchor=W)
        mt.heading('Grade',text='Grade',anchor=W)
        mt.heading('Section',text='Section',anchor=W)
        mt.heading('Sex',text='Sex',anchor=W)
        mt.heading('Age',text='Age',anchor=W)
        mt.heading('Region',text='Region',anchor=W)
        mt.heading('Town',text='Town',anchor=W)
        mt.heading('Kebele',text='Kebele',anchor=W)
        mt.heading('Parent_Name',text='Parent Name',anchor=W)
        mt.heading('Parent_Phone',text='Parent Phone',anchor=W)

        conn = sqlite3.connect('StudentDb.db')
        i = conn.cursor()
        
        i.execute("SELECT * FROM StudentDB WHERE Grade = ? AND Section = ?",( str(gxs.get()),sxs.get()) )
        names = i.fetchall()
        cot = 0
    
        for name in names:
       
            mt.insert(parent='',index='0',iid=cot,values=(name[0],name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9],name[10]))
            cot = cot + 1
        mt.place(x=8,y=35)
        org.geometry("940x550")
        org.resizable(0,0)
        



    header = Frame(ads,bg='#222',width=471,height=222).place(x=460,y=325)

    Label(ads,text="Organize Search",bg='#222',fg='#888' ).place(x=468,y=330)
    gxs = ttk.Combobox(ads, width = 28)
      

    # Adding combobox drop down list
    gxs['values'] = (9,10,11,12)
      
    gxs.place(x=468,y=356)
    gxs.current(0)

    sxs = ttk.Combobox(ads, width = 28)
      
    # Adding combobox drop down list
    sxs['values'] = ('A','B','C','D')
      
    sxs.place(x=468,y=396)
    sxs.current(0)

    sbtn = Button(ads,text='Show Data',width=26,bg="#333",fg='white',relief = FLAT,command = orgs).place(x=468 ,y=432)

    







    srcF = Entry(ads,width=45,bd=2,highlightthickness=2)
    srcF.place(x=546,y=5)

    sbtn = Button(ads,text='Search',width=13,bg="#333",fg='white',relief = FLAT,command = searchView).place(x=830 ,y=6)






    gx = ttk.Combobox(ads, width = 28)
      
    # Adding combobox drop down list
    gx['values'] = ('A','B','C','D')
      
    gx.place(x=8,y=480)
    gx.current(0)
    

    Label(ads,text="Full Name" ).place(x=8,y=330)
    
    fname = Entry(ads,width=32,highlightthickness=1,bd=2)
    fname.place(x=8,y=355)
    Label(ads,text="Grade" ).place(x=8,y=390)
    
    

    gm = StringVar()
    
    monthchoosen = ttk.Combobox(ads, width = 29)
      
    # Adding combobox drop down list
    monthchoosen['values'] = (9,10,11,12)
    monthchoosen.current(0)
    monthchoosen.place(x=8,y=416)
    

    Label(ads,text="Section" ).place(x=8,y=445)
    Label(ads,text="Sex" ).place(x=8,y=515)


    gen = ttk.Combobox(ads, width = 21)
      
    # Adding combobox drop down list
    gen['values'] = ('M','F')
      
    gen.place(x=48,y=515)
    gen.current(0)


    
    
    Label(ads,text="Parent Name" ).place(x=250,y=330)
    pname = Entry(ads,width=30,bd=2,highlightthickness=2)
    pname.place(x=250,y=355)
    Label(ads,text="Parent Phone" ).place(x=250,y=388)
    pnum = Entry(ads,width=30,bd=2,highlightthickness=2)
    pnum.place(x=250,y=415)
    
    Label(ads,text="Age" ).place(x=250,y=450)
    
    
    ege = ttk.Combobox(ads, width = 21)
      
    # Adding combobox drop down list
    ege['values'] = (15,16,17,18,19,20)
      
    ege.place(x=290,y=450)
    ege.current(1)

    Label(ads,text="Kebele" ).place(x=250,y=480)
    
    kb = IntVar()
    keb = ttk.Combobox(ads, width = 21)
      
    # Adding combobox drop down list
    keb['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
      
    keb.place(x=290,y=480)
    keb.current(1)

    Abtn = Button(ads,text='Submit Data',width=26,bg="#006aff",fg='white',relief = FLAT,command = submit).place(x=250 ,y=520)


    
    ads.geometry("940x550")
    ads.resizable(0,0)
    ads.mainloop()




################################################## QR-Code Generator ####################################################







def QrGen():
    
    QR=Tk()
   
    QR.title('---QR-Code Generator---')
    QR.iconbitmap("Plugin.ico")
    
    
    L1=Label(QR,text="Create QR-Code",font=('Pump Demi Bold LET',34,'normal'),bg='#fff',fg='#006aff').pack(ipady=40,ipadx=315)
    Br=Label(QR,text='').pack(ipady=5)
    Br=Label(QR,text='').pack(ipady=5)
    com=Label(QR,text='Please enter the student full name_________________',fg='#006aff',font=('arial',12,'normal')).pack(ipady=1)


  
    def sad():
        ore = e.get()
        print(ore)
        img = qrcode.make(ore)
        img.save(f"QRcd/{ore}.jpg")
        def clearr():
           e.delete(0, END)
        clearr()
   
    e = Entry(QR,width=42,fg='#333',font=('arial',13),bd=2)
    e.pack(ipady=10,pady=7)

   
  
        
    Btn=Button(QR,text='Create',fg='white',bg='#006aff',width=53,relief=FLAT,command=sad).pack(ipady=12,pady=7)
    QR.geometry('940x550')
    QR.resizable(0,0)
    QR.mainloop()






################################################## About us ####################################################






    

def Abtus():
    Mb = messagebox.showinfo("About us","""| Onyx Technology |\n \n \n \n \n Developers:  Bereket Daniel 
                       Benjamin Endale \n \n \n \n \n Contact: +251966442525 | Bereket Daniel 
                 +2519277279927 | Benjamin Endale \n \n \n \n \n Our Service: Static Web Devlopmnet
                      Office Automation
                      Mangement Software Development
                      Analytic Software Development
                      Logo Desgin \n \n \n \n \n \n 
                     
                                        


""")
    







################################################## Delete Data ####################################################

def delt():
    dt=Tk()
    
    dt.title('---Customize Data---')
    dt.iconbitmap("Plugin.ico")
    def dltLt():
        os.remove("LateStudent.txt")
        print('scussesfuly deleted')
    def dltAb():
        os.remove("AbsentStudent.txt")
        print('scussesfuly deleted')
    
    
    L1=Label(dt,text="Customize Data",font=('Pump Demi Bold LET',34,'normal'),bg='#fff',fg='#006aff').pack(ipady=40,ipadx=315)
    Br=Label(dt,text='').pack(ipady=5)
    Br=Label(dt,text='').pack(ipady=5)
    com=Label(dt,text='______________Here you can delete unwanted data',fg='#006aff',font=('arial',12,'normal')).pack(ipady=1)


  
    

   
  
    Btn=Button(dt,text='Delete All DataBase',fg='white',bg='#006aff',width=53,relief=FLAT,command=None).pack(ipady=12,pady=7)
    Btn=Button(dt,text='Delete Late Student List',fg='white',bg='#006aff',width=53,relief=FLAT,command=dltLt).pack(ipady=12,pady=7)
      
    Btn=Button(dt,text='Delete Absent Student List',fg='white',bg='#006aff',width=53,relief=FLAT,command=dltAb).pack(ipady=12,pady=7)
    dt.geometry('940x550')
    dt.resizable(0,0)
    dt.mainloop()
    





################################################## Instruction ####################################################

def inst():
        In = messagebox.showinfo("Instructions",""" | Instructions About System |\n \n \n \n \n [] First register student when you add register student data at the same time thestudent name change into QR-codeand store in QR-code image folder.
                                 \n 
[] Then start camera or click Attendance Run button  and when you finish if you want to stop camera click 'b' on keyboardand when you hit 'b' button it will report Late student and Absent student data.
                             \n \n \n \n \n \n \n
                     
                                        """)





    

def IDG():

    w = Tk()
    w.iconbitmap("fav.ico")
    w.title("Digital Id Generator")
    global namee

    

    def clr():
       
        fileName.delete(0,END)

    



    def exe():
        photoo = fileName.get()
        print(photoo)
        with open(f"{photoo}.csv",'r') as file:
            reader = csv.reader(file)
            for row in reader:
                Ft = ImageFont.truetype('Cfont.ttf', 26)
                img = Image.open('Idc.png')
               
                imgcopy = img.copy()
                img2 = Image.open('Nani.jpg')
                img2copy = img2.copy()
               
                img.paste(img2copy,(830,465))
                imgcopy.save("New_ID/ohmighty.png")
                I1 = ImageDraw.Draw(img)
                I1.text((374, 700), row[9], fill=(25, 25, 185),font=Ft)
               
                I1.text((130, 180), row[0], fill=(32, 32, 180),font=Ft)
                I1.text((110, 310), row[1], fill=(32, 32, 180),font=Ft)
                I1.text((270, 310), row[2], fill=(32, 32, 180),font=Ft)
                I1.text((459, 310), row[3], fill=(32, 32, 180),font=Ft)
                I1.text((590, 310), row[4], fill=(32, 32, 180),font=Ft)
                I1.text((374, 438), row[5], fill=(32, 32, 180),font=Ft)
                I1.text((620, 438), row[6], fill=(32, 32, 180),font=Ft)
                I1.text((374, 540), row[7], fill=(32, 32, 180),font=Ft)
                I1.text((374, 637), row[8], fill=(32, 32, 180),font=Ft)

                
                img.save(f"New_ID/{row[0]}.png")
                Fimg = Image.open(f'New_ID/{row[0]}.png')

                
                nimg = Fimg.resize((500,300))
                nimg.save('New_ID/nodeJs.png')
              
            
        lb = Label(w,text='Succesfuly create id card in <New_ID> Folder',fg='#006aff').place(x=288,y=400)
     
        
     
   
    header = Frame(w,bg='#fff',width=940,height=140).place(x=0,y=0)

    



    HeadTitle = Label(w,text='Digital ID Card Generator',fg='#006aff',bg='#fff',font=('Pump Demi Bold LET',34,'normal')).place(x=230,y=40)
    

   

    btn = Button(w,text='Generate ID', width=44,bg='#006aff',fg='white' ,height=1,relief = FLAT,command=exe).place(x=288,y=290)
    btn = Button(w,text='Exist', width=20,bg='#006aff',fg='white' ,height=1,relief = FLAT,command=w.destroy).place(x=288,y=350)
    btn = Button(w,text='Clear', width=20,bg='#006aff',fg='white' ,height=1,relief = FLAT,command=clr).place(x=454,y=350)

    fileName = Entry(w,width=52,fg='#fff',relief=FLAT,bg='#333')
    fileName.place(x=288,y=240)

    lb = Label(w,text='Enter the Excel file name properly',fg='#006aff',font=(6)).place(x=286,y=200)






   
      


    w.geometry('940x550')
    w.resizable(0,0)
    w.mainloop()







################################################## MenuBar code ####################################################








menubar = Menu(root)

    # Adding File Menu and commands
file = Menu(menubar, tearoff = 1,bg='#333' ,fg='#fff')
menubar.add_cascade(label ='Main', menu = file )

file.add_command(label ='Main DashBoard      ', command = Addstudent)
file.add_command(label ='Attendance Run     ', command = Atd)
file.add_command(label ='Register Students    ', command = Dashboard)

file.add_command(label ='Analyze data     ', command = ana)

file.add_command(label ='Today Records     ', command = ABdata)
file.add_separator()

file.add_command(label ='Close', command = root.destroy)


    # Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0,bg='#333' ,fg='#fff')
menubar.add_cascade(label ='Edit', menu = edit)


edit.add_command(label =' Delete Data      ', command = delt)


   

    # Adding Help Menu
set_ = Menu(menubar, tearoff = 0,bg='#333' ,fg='#fff')
menubar.add_cascade(label ='Create', menu = set_)
set_.add_command(label ='  Generete QR-Code    ', command = QrGen)
set_.add_command(label ='  ID Card Generator    ', command = IDG)
    
help_ = Menu(menubar, tearoff = 0,bg='#333' ,fg='#fff')
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='  Instructions   ', command = inst)

    
about_ = Menu(menubar, tearoff = 0,bg='#333' ,fg='#fff')
menubar.add_cascade(label ='About', menu = about_)
about_.add_command(label ='About us          ', command = Abtus)

    
root.config(menu = menubar)
    
img = PhotoImage(file='core.png')
Label(root,image=img).pack()



w=940
h=550

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.attributes('-alpha',0.96)

root.resizable(0,0)
root.mainloop()





################################################## Tnx God ####################################################




