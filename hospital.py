from inspect import FrameInfo
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import Frame
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter.font import BOLD
from webbrowser import get
import mysql.connector
import sqlite3


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Vaccination Detail Collector")
        self.root.geometry("1540x800+0+0")

        # SQLite database connection
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hospital
                    (vaccine_dose text, name text, place text, date text, batch_no text, p_name text,
                    address text, nic_no text, age text, gender text, blood_grp text, DOB text,
                    effects text, body_temp text, blood_p text, contact_no text, email text, remark text)''')
        self.conn.commit()

        self.vaccine=StringVar()
        self.name=StringVar()
        self.place=StringVar()
        self.date=StringVar()
        self.batchno=StringVar()
        self.pname=StringVar()
        self.address=StringVar()
        self.nic=StringVar()
        self.age=StringVar()
        self.gender=StringVar()
        self.bloodgrp=StringVar()
        self.bod=StringVar()
        self.effects=StringVar()
        self.bodytemp=StringVar()
        self.bloodp=StringVar()
        self.contactno=StringVar()
        self.email=StringVar()
        self.remark=StringVar()

        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="VACCINATION DETAIL COLLECTOR",
                        fg="green",bg="white",font=("times new romen",50,BOLD) )
        lbltitle.pack(side=TOP,fill=X)

        # ===============================DATA FRAME============================== 
        Dataframe = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)
        

        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("times new romen",12,BOLD), text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("times new romen",12,BOLD), text="Prescription")
        DataframeRight.place(x=998,y=5,width=460,height=350)

        # ===============================BUTTON FRAME=============================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1538,height=70)

        # ===============================DETAILS FRAME=============================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1538,height=190)

        # =============================DATA FRAME LEFT=============================

        lblNameTablet=Label(DataframeLeft, text="Covid-19 Vaccine", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.vaccine,state="readonly"
                                        ,font=("times new roman",12,"bold"),
                                                    width=38)
        comNametablet["values"]=("1 st Dose", "2 nd Dose", "3 rd Dose", "4 th Dose")
        comNametablet.grid(row=0,column=1)



        lblNameVaccine=Label(DataframeLeft, text="Name of the Vaccine", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameVaccine.grid(row=1,column=0)

        comNameVaccine=ttk.Combobox(DataframeLeft,textvariable=self.name,state="readonly",font=("times new roman",12,"bold"),
                                                                                width=38)
        comNameVaccine["values"]=("Sinophram", "Pfizer", "AstraZeneca", "Moderna", "Sputnic V")
        comNameVaccine.grid(row=1,column=1)

        lblPlace=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Place of Vaccination",padx=2,pady=6)
        lblPlace.grid(row=2,column=0,sticky=W)
        txtPlace=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.place,width=40 )
        txtPlace.grid(row=2, column=1)

        lblDate=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Date of Vaccination",padx=2,pady=6)
        lblDate.grid(row=3,column=0,sticky=W)
        txtDate=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.date,width=40 )
        txtDate.grid(row=3, column=1)

        lblBatchNum=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Batch Number",padx=2,pady=6)
        lblBatchNum.grid(row=4,column=0,sticky=W)
        txtBatchNum=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.batchno,width=40 )
        txtBatchNum.grid(row=4, column=1)

        lblpntName=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Patient Name",padx=2,pady=6)
        lblpntName.grid(row=5,column=0,sticky=W)
        txtpntName=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.pname,width=40 )
        txtpntName.grid(row=5, column=1)

        lblAddress=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Address",padx=2,pady=6)
        lblAddress.grid(row=6,column=0,sticky=W)
        txtAddress=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.address,width=40 )
        txtAddress.grid(row=6, column=1)

        lblnic=Label(DataframeLeft,font=("times new roman",12,"bold"),text="NIC Number",padx=2,pady=6)
        lblnic.grid(row=7,column=0,sticky=W)
        txtnic=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.nic,width=40 )
        txtnic.grid(row=7, column=1)

        lblAge=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Age",padx=2,pady=6)
        lblAge.grid(row=8,column=0,sticky=W)
        txtAge=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.age,width=40 )
        txtAge.grid(row=8, column=1)

        lblGender=Label(DataframeLeft, text="Gender", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblGender.grid(row=0,column=5)

        comGender=ttk.Combobox(DataframeLeft,textvariable=self.gender,state="readonly",font=("times new roman",12,"bold"),
                                                                                width=38)
        comGender["values"]=("Male", "Female")
        comGender.grid(row=0,column=6)

        lblBlood=Label(DataframeLeft, text="Blood Group", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBlood.grid(row=1,column=5)

        comBlood=ttk.Combobox(DataframeLeft,textvariable=self.bloodgrp,state="readonly",font=("times new roman",12,"bold"),
                                                                                width=38)
        comBlood["values"]=("O+", "O-","A+","A-","B+","B-","AB+","AB-")
        comBlood.grid(row=1,column=6)

        lblDOB=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Birth of Date",padx=2,pady=6)
        lblDOB.grid(row=2,column=5,sticky=W)
        txtDOB=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.bod,width=40 )
        txtDOB.grid(row=2, column=6)

        lblSideEffects=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Side Effects",padx=2,pady=6)
        lblSideEffects.grid(row=3,column=5,sticky=W)
        txtSideEffects=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.effects,width=40 )
        txtSideEffects.grid(row=3, column=6)
        
        lblBodyTemp=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Body Tempreture",padx=2,pady=6)
        lblBodyTemp.grid(row=4,column=5,sticky=W)
        txtBodyTemp=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.bodytemp,width=40 )
        txtBodyTemp.grid(row=4 , column=6)
        
        lblBloodp=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodp.grid(row=5,column=5,sticky=W)
        txtBloodp=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.bloodp,width=40 )
        txtBloodp.grid(row=5 , column=6)

        lblContactNum=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Contact Number",padx=2,pady=6)
        lblContactNum.grid(row=6,column=5,sticky=W)
        txtContactNum=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.contactno,width=40 )
        txtContactNum.grid(row=6, column=6)

        lblEmail=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Email Address",padx=2,pady=6)
        lblEmail.grid(row=7,column=5,sticky=W)
        txtEmail=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.email,width=40 )
        txtEmail.grid(row=7 , column=6)

        lblRemark=Label(DataframeLeft,font=("times new roman",12,"bold"),text="Remark",padx=2,pady=6)
        lblRemark.grid(row=8,column=5,sticky=W)
        txtRemark=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.remark,width=40 )
        txtRemark.grid(row=8, column=6)

        #================================DATA FARME RIGHT==============================
        self.txtPrescription=Text(DataframeRight,font=("times new roman",12,"bold"),width=52,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #==================================BUTTON======================================
        btnPrescription=Button(Buttonframe , command=self.iPrescription , text="Prescription" ,fg="white",bg="green",font=("times new romen",12,BOLD),width=24,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe, command=self.iPrescriptionData ,text="Prescription Data" ,fg="white",bg="green",font=("times new romen",12,BOLD),width=24,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe, command=self.update_data , text="Update" ,fg="white",bg="green",font=("times new romen",12,BOLD),width=24,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe, command=self.iDelete ,text="Delete" ,fg="white",bg="green",font=("times new romen",12,BOLD),width=24,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe, command=self.clear ,text="Clear" ,fg="white",bg="green",font=("times new romen",12,BOLD),width=24,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe, command=self.iExit ,text="Exit" ,fg="white",bg="red",font=("times new romen",12,BOLD),width=24,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #====================================TABLE==========================================

        #===================================SCROLBAR========================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient = VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("vaccine","name","place","date","batchno","pname","address","nic","age","gender","bloodgrp","bod",
                                    "effects","bodytemp","bloodp","contactno","email","remark"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("vaccine",text="Covid-19 Vaccine")
        self.hospital_table.heading("name",text="Name of Vaccine")
        self.hospital_table.heading("place",text="Place of Vaccination")
        self.hospital_table.heading("date",text="Date of Vaccination")
        self.hospital_table.heading("batchno",text="Batch Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("address",text="Address")
        self.hospital_table.heading("nic",text="NIC Number")
        self.hospital_table.heading("age",text="Age")
        self.hospital_table.heading("gender",text="Gender")
        self.hospital_table.heading("bloodgrp",text="Blood Group")
        self.hospital_table.heading("bod",text="Birth of Date")
        self.hospital_table.heading("effects",text="Side Effects")
        self.hospital_table.heading("bodytemp",text="Body Tempreture")
        self.hospital_table.heading("bloodp",text="Blood Pressure")
        self.hospital_table.heading("contactno",text="Contact Number")
        self.hospital_table.heading("email",text="Email Address")
        self.hospital_table.heading("remark",text="Remark")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("vaccine",width=100)
        self.hospital_table.column("name",width=100)
        self.hospital_table.column("place",width=100)
        self.hospital_table.column("date",width=100)
        self.hospital_table.column("batchno",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("address",width=100)
        self.hospital_table.column("nic",width=100)
        self.hospital_table.column("age",width=100)
        self.hospital_table.column("gender",width=100)
        self.hospital_table.column("bloodgrp",width=100)
        self.hospital_table.column("bod",width=100)
        self.hospital_table.column("effects",width=100)
        self.hospital_table.column("bodytemp",width=100)
        self.hospital_table.column("bloodp",width=100)
        self.hospital_table.column("contactno",width=100)
        self.hospital_table.column("email",width=100)
        self.hospital_table.column("remark",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()

#====================================functional declration===============================

    def iPrescriptionData(self):
        # Insert data into SQLite table
        self.cursor.execute("INSERT INTO hospital VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (self.vaccine.get(), self.name.get(), self.place.get(), self.date.get(),
                             self.batchno.get(), self.pname.get(), self.address.get(), self.nic.get(),
                             self.age.get(), self.gender.get(), self.bloodgrp.get(), self.bod.get(),
                             self.effects.get(), self.bodytemp.get(), self.bloodp.get(), self.contactno.get(),
                             self.email.get(), self.remark.get()))
        self.conn.commit()
        self.fatch_data()
        messagebox.showinfo("Success", "Record has been Inserted")


    def update_data(self):
        conn = sqlite3.connect('hospital.db')
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital SET vaccine_dose=?, name=?, place=?, date=?, p_name=?,"
                            "address=?, nic_no=?, age=?, gender=?, blood_grp=?, DOB=?, effects=?,"
                            "body_temp=?, blood_p=?, contact_no=?, email=?, remark=? WHERE batch_no=?",
                            (
                                self.vaccine.get(), self.name.get(), self.place.get(),
                                self.date.get(),self.pname.get(),self.address.get(),self.nic.get(),self.age.get(),
                                self.gender.get(),self.bloodgrp.get(),self.bod.get(),
                                self.effects.get(),self.bodytemp.get(),self.bloodp.get(),
                                self.contactno.get(),self.email.get(),self.remark.get(), self.batchno.get(),
                            ))
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Update",   "Record has been updated Successfully")

    def fatch_data(self):
        # Fetch data from SQLite table
        self.cursor.execute("SELECT * FROM hospital")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            self.conn.commit()



    def get_cursor(self, event = ""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.vaccine.set(row[0])
        self.name.set(row[1])
        self.place.set(row[2])
        self.date.set(row[3])
        self.batchno.set(row[4])
        self.pname.set(row[5])
        self.address.set(row[6])
        self.nic.set(row[7])
        self.age.set(row[8])
        self.gender.set(row[9])
        self.bloodgrp.set(row[10])
        self.bod.set(row[11])
        self.effects.set(row[12])
        self.bodytemp.set(row[13])
        self.bloodp.set(row[14])
        self.contactno.set(row[15])
        self.email.set(row[16])
        self.remark.set(row[17])


    def iPrescription(self):
        self.txtPrescription.insert(END,"Covid-19 Vaccine \t\t\t:"+self.vaccine.get()+"\n")
        self.txtPrescription.insert(END,"Name of the Vaccine \t\t\t:"+self.name.get()+"\n")
        self.txtPrescription.insert(END,"Place of Vaccination \t\t\t:"+self.place.get()+"\n")
        self.txtPrescription.insert(END,"Date of Vaccination \t\t\t:"+self.date.get()+"\n")
        self.txtPrescription.insert(END,"Batch Number \t\t\t:"+self.batchno.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name \t\t\t:"+self.pname.get()+"\n")
        self.txtPrescription.insert(END,"Address \t\t\t:"+self.address.get()+"\n")
        self.txtPrescription.insert(END,"NIC Number \t\t\t:"+self.nic.get()+"\n")
        self.txtPrescription.insert(END,"Age \t\t\t:"+self.age.get()+"\n")
        self.txtPrescription.insert(END,"Gender \t\t\t:"+self.gender.get()+"\n")
        self.txtPrescription.insert(END,"Blood Group \t\t\t:"+self.bloodgrp.get()+"\n")
        self.txtPrescription.insert(END,"Birth of Date \t\t\t:"+self.bod.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects \t\t\t:"+self.effects.get()+"\n")
        self.txtPrescription.insert(END,"Body Tempreture \t\t\t:"+self.bodytemp.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure\t\t\t:"+self.bloodp.get()+"\n")
        self.txtPrescription.insert(END,"Contact Number \t\t\t:"+self.contactno.get()+"\n")
        self.txtPrescription.insert(END,"Email Address \t\t\t:"+self.email.get()+"\n")
        self.txtPrescription.insert(END,"Remark \t\t\t:"+self.remark.get()+"\n")



    def iDelete(self):
        # Delete record from SQLite table
        self.cursor.execute("DELETE FROM hospital WHERE batch_no=?", (self.batchno.get(),))
        self.conn.commit()
        self.fatch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")


    def clear(self):
        # Clear all entry fields and text widget
        self.vaccine.set("")
        self.name.set("")
        self.place.set("")
        self.date.set("")
        self.batchno.set("")
        self.pname.set("")
        self.address.set("")
        self.nic.set("")
        self.age.set("")
        self.gender.set("")
        self.bloodgrp.set("")
        self.bod.set("")
        self.effects.set("")
        self.bodytemp.set("")
        self.bloodp.set("")
        self.contactno.set("")
        self.email.set("")
        self.remark.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        # Ask for confirmation before exiting
        if messagebox.askyesno("Vaccination Detail Collector", "Do you want to Exit?"):
            self.root.destroy()

    def __del__(self):
        # Close SQLite database connection
        self.conn.close()


root=Tk()
ob=Hospital(root)
root.mainloop()