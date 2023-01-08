from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
from datetime import date, datetime, timedelta

import json

from my_package import LogInCredentials


class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Login Page")
        self.window.geometry('1350x750+0+0')
        self.frame = Frame(self.window, width=1350, height=750)
        self.frame.pack()
        self.frame.grid_propagate(False)
        bg = ImageTk.PhotoImage(Image.open("./Data/OnlinePharmacy.jpg"))
        img_label = Label(self.frame, image=bg)
        img_label.place(x=0, y=0)

        self.labelTitle = Label(self.frame, text="Medicine Automation Software", font=('arial', 30, 'bold'),
                                fg="#222730", bg="#b6b2ad", bd=20)
        self.labelTitle.grid(row=0, column=0, pady=(0, 40), padx=(0, 50))
        self.labelTitle.place(in_=self.frame, anchor="center", relx=.5, rely=.123)

        # ****   FRAMES     *************

        self.frame1 = Frame(self.frame, width=542, height=180, bd=2, relief='solid', padx=12, bg="#7D8CA3")
        self.frame1.place(in_=self.frame, anchor="center", relx=.5, rely=.44)
        self.frame1.grid_propagate(False)

        self.frame2 = Frame(self.frame, width=542, height=70, bd=2, relief='solid', padx=12, bg="#7D8CA3")
        self.frame2.place(in_=self.frame, anchor="center", relx=.5, rely=.61)
        self.frame2.grid_propagate(False)


        # ===========             USERNAME AND PASSWORD (FRAME 2)            ===================================================================================

        self.labelUser = Label(self.frame1, text="USERNAME / USER ID   ", font=('arial', 12, 'bold'), bg="#7D8CA3",
                               bd=20)
        self.labelUser.grid(row=0, column=0, columnspan=2, pady=10)
        self.username = StringVar()
        self.eUsername = Entry(self.frame1, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1, textvariable=self.username)
        self.eUsername.grid(row=0, column=2, columnspan=2, pady=10)

        self.labelPass = Label(self.frame1, text="PASSWORD   ", font=('arial', 12, 'bold'), bg="#7D8CA3", bd=20)
        self.labelPass.grid(row=1, column=0, columnspan=2, pady=10)
        self.password = StringVar()
        self.ePass = Entry(self.frame1, show="*", width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1, textvariable=self.password)
        self.ePass.grid(row=1, column=2, columnspan=2, pady=10)

        # ===========            LOGIN RESET EXIT (FRAME 3)            ===================================================================================

        self.btnLogin = Button(self.frame2, text="Login", command=lambda: self.userLogin(), font=('arial', 12, 'bold'),
                               width=13)
        self.btnLogin.grid(row=0, column=0, padx=11, pady=11)
        self.btnReset = Button(self.frame2, text="Reset", command=lambda: self.reset(), font=('arial', 12, 'bold'),
                               width=15)
        self.btnReset.grid(row=0, column=1, padx=11, pady=11)
        self.btnExit = Button(self.frame2, text="Exit", command=lambda: self.exitProgram(), font=('arial', 12, 'bold'),
                              width=13)
        self.btnExit.grid(row=0, column=2, padx=11, pady=11)

        self.window.mainloop()

    def userLogin(self):
        """

        This method is used to check the user credentials and if the user is valid then it will open the operation selection window

        """
        if (
                self.eUsername.get() != shopowner.name and self.eUsername.get() != shopowner.ID) or self.ePass.get() != shopowner.password:
            messagebox.showwarning("Invalid Entries!", "The Username or Password entered is incorrect")
        else:
            self.operation_selection_window()

    def reset(self):
        """

        This method is used to reset the username and password fields

        """
        self.window.destroy()
        MainWindow(Tk())

    def exitProgram(self):
        """

        This method is used to exit the program

        """
        choice = messagebox.askquestion("Exit", "Are you sure?")
        if choice == 'yes':
            exit()

    def operation_selection_window(self):
        """

        This method is used to open the operation selection window

        """
        self.username.set("")
        self.password.set("")
        self.newWindow = Toplevel(self.window)
        self.app = OperationSelectionWindow(self.newWindow)


class OperationSelectionWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Operation Selection Page")
        self.window.geometry('1350x750+0+0')
        self.frame = Frame(self.window)
        self.frame.pack()

        # ====================             FRAMES             ===================================================================================

        self.frame1 = Frame(self.frame, width=1000, height=100, bd=7, relief='ridge', bg="SkyBlue2")
        self.frame1.grid(row=0, column=0, sticky="news")

        self.frame2 = Frame(self.frame, width=900, height=630, bd=7, relief='ridge', padx=12)
        self.frame2.grid(row=0, column=1)

        # ====================             BUTTONS IN FRAME1             ===================================================================================

        self.btnNewMedicine = Button(self.frame1, text="Add New Medicine",
                                     command=lambda: self.addNewMedicineToInventory(), font=('arial', 12, 'bold'),
                                     width=20)
        self.btnNewMedicine.grid(row=0, column=0, padx=40, pady=10)

        self.btnExistMedicine = Button(self.frame1, text="Restock  /\nAdd New Batch of \nExisting Medicine",
                                       command=lambda: self.addExistMedicine(), font=('arial', 12, 'bold'), width=20)
        self.btnExistMedicine.grid(row=1, column=0, padx=40, pady=10)

        self.btnEditPublications = Button(self.frame1, text="Query about a Medicine", command=lambda: self.Query(),
                                          font=('arial', 12, 'bold'), width=20)
        self.btnEditPublications.grid(row=3, column=0, padx=40, pady=10)

        self.btnCustomerBills = Button(self.frame1, text="Print the list of \nexpired Medicines",
                                       command=lambda: self.printexpiredlist(), font=('arial', 12, 'bold'), width=20)
        self.btnCustomerBills.grid(row=4, column=0, padx=40, pady=10)

        self.btnCustomerBills = Button(self.frame1, text="Process \ncustomer order",
                                       command=lambda: self.processOrder(), font=('arial', 12, 'bold'), width=20)
        self.btnCustomerBills.grid(row=5, column=0, padx=40, pady=10)

        self.btnSummary = Button(self.frame1, text="Print and Store \nrequirement for the \nnext day",
                                 command=lambda: self.printandstorerequirement(), font=('arial', 12, 'bold'), width=20)
        self.btnSummary.grid(row=6, column=0, padx=40, pady=10)

        self.btnAddDeliverer = Button(self.frame1, text="Add Vendor",
                                      command=lambda: self.operationsonvendors(), font=('arial', 12, 'bold'), width=20)
        self.btnAddDeliverer.grid(row=7, column=0, padx=40, pady=10)

        self.btnDeliveryDetails = Button(self.frame1, text="Vendor wise cheque \nfor items supplied",
                                         command=lambda: self.producecheque(), font=('arial', 12, 'bold'), width=20)
        self.btnDeliveryDetails.grid(row=8, column=0, padx=40, pady=10)

        self.btnDeliveryDetails = Button(self.frame1, text="Generate Revenue \nand Profit",
                                         command=lambda: self.Generate(), font=('arial', 12, 'bold'), width=20)
        self.btnDeliveryDetails.grid(row=9, column=0, padx=40, pady=10)

        self.window.mainloop()

    def addNewMedicineToInventory(self):
        self.reset()
        # ====================            ADD NEW MEDICINE HEADING             ===================================================================================

        self.labelNewMedicine = Label(self.frame2, text="Add New Medicine", font=('arial', 17, 'bold'),
                                      bd=20)
        self.labelNewMedicine.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       MEDICINE DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelcnumber = Label(self.frameDetails, text="Code Number ", font=('arial', 12, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelcnumber.grid(row=0, column=0, rowspan=2)
        self.cNum = IntVar()
        self.ecNum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.cNum)
        self.ecNum.grid(row=2, column=0, padx=10)

        self.labeltradename = Label(self.frameDetails, text="Trade Name ", font=('arial', 12, 'bold'), bd=10,
                                    bg="SkyBlue2", justify=LEFT)
        self.labeltradename.grid(row=0, column=1, rowspan=2)
        self.trname = StringVar()
        self.eTrame = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.trname)
        self.eTrame.grid(row=2, column=1, padx=10)

        self.labelgenname = Label(self.frameDetails, text="Generic Name ", font=('arial', 12, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelgenname.grid(row=0, column=2, rowspan=2)
        self.gname = StringVar()
        self.eGname = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.gname)
        self.eGname.grid(row=2, column=2, padx=10)

        self.labelppu = Label(self.frameDetails, text="Price per Unit ", font=('arial', 12, 'bold'), bd=10,
                              bg="SkyBlue2", justify=LEFT)
        self.labelppu.grid(row=4, column=0, rowspan=2)
        self.pricepU = IntVar()
        self.ePPU = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.pricepU)
        self.ePPU.grid(row=6, column=0, padx=10)

        self.labelBNo = Label(self.frameDetails, text="Batch Number ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelBNo.grid(row=4, column=1, rowspan=2)
        self.bnum = StringVar()
        self.eBnum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.bnum)
        self.eBnum.grid(row=6, column=1, padx=10)

        self.labelexpD = Label(self.frameDetails, text="Expiry Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelexpD.grid(row=4, column=2, rowspan=2)
        self.expdate = StringVar()
        self.eExpdate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                              borderwidth=1,
                              textvariable=self.expdate)
        self.eExpdate.grid(row=6, column=2, padx=10)

        self.labelvid = Label(self.frameDetails, text="Vendor Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvid.grid(row=8, column=0, rowspan=2)
        self.vId = IntVar()
        self.eVId = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vId)
        self.eVId.grid(row=10, column=0, padx=10)

        self.labelcompD = Label(self.frameDetails, text="Company Description ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelcompD.grid(row=8, column=1, rowspan=2)
        self.compd = StringVar()
        self.eCompd = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.compd)
        self.eCompd.grid(row=10, column=1, padx=10)

        self.labelmedD = Label(self.frameDetails, text="Medicine Description ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelmedD.grid(row=8, column=2, rowspan=2)
        self.medd = StringVar()
        self.eMedd = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.medd)
        self.eMedd.grid(row=10, column=2, padx=10)

        self.labelavailQ = Label(self.frameDetails, text="Available Quantity ", font=('arial', 12, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelavailQ.grid(row=12, column=0, rowspan=2)
        self.availq = IntVar()
        self.eAvailq = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                             borderwidth=1,
                             textvariable=self.availq)
        self.eAvailq.grid(row=14, column=0, padx=10)

        self.labelthresval = Label(self.frameDetails, text="Threshold Value ", font=('arial', 12, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelthresval.grid(row=12, column=1, rowspan=2)
        self.thresVal = IntVar()
        self.eThresVal = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.thresVal)
        self.eThresVal.grid(row=14, column=1, padx=10)

        self.labelusell = Label(self.frameDetails, text="Unit Selling ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelusell.grid(row=12, column=2, rowspan=2)
        self.uSell = IntVar()
        self.eUSell = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.uSell)
        self.eUSell.grid(row=14, column=2, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Add", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.addnewMed())
        self.btnAddTop.grid(row=19, column=1, padx=20)

    def addnewMed(self):
        """

        This method is used to add new medicine to the database

        """
        # self.reset()
        if self.gname.get() == "" and self.trname.get() == "":
            messagebox.showerror("Empty names!", "Enter generic name or trade name of the medicine", parent=self.window)
        elif self.compd.get() == "":
            messagebox.showerror("Empty Company Description field", "Enter the company description of the medicine",
                                 parent=self.window)
        elif self.vId.get() == 0:
            messagebox.showerror("Empty Vendor ID Field!", "Enter the vendor ID from which the medicine is bought",
                                 parent=self.window)
        elif self.pricepU.get() <= 0:
            messagebox.showwarning("Price must be non-negative!", "Enter valid price of medicine (>= 0)",
                                   parent=self.window)
        elif len(self.expdate.get()) != 10 or self.expdate.get()[2] != '-' or self.expdate.get()[5] != '-':
            messagebox.showerror("Expiry Date formatting error!", "Enter the expiry date in DD-MM-YYYY format",
                                 parent=self.window)
        elif int(self.expdate.get()[3:5]) > 12:
            messagebox.showerror("Expiry Date Entry Error!", "Enter a valid expiry date with proper month number",
                                 parent=self.window)
        elif (int(self.expdate.get()[0:2]) > 31) or (
                int(self.expdate.get()[0:2]) > 30 and int(self.expdate.get()[3:5]) in [2, 4, 6, 9, 11]):
            messagebox.showerror("Expiry Date Entry Error!", "Enter a valid expiry date with proper date number",
                                 parent=self.window)
        else:
            var = {
                "code_number": self.cNum.get(),
                "trade_name": self.trname.get(),
                "generic_name": self.gname.get(),
                "price_per_unit": self.pricepU.get(),
                "Batch_no": self.bnum.get(),
                "exp_date": self.expdate.get(),
                "vendor_id": self.vId.get(),
                "company_description": self.compd.get(),
                "medicine_description": self.medd.get(),
                "available_quantity": self.availq.get(),
                "threshold_value": self.thresVal.get(),
                "unit_selling": self.uSell.get()
            }
            medicineInventory.append(var)
            with open("./Data/MedicineInventory.json", "w") as p:
                json.dump(medicineInventory, p, indent=4)
                messagebox.showinfo("Success", "Medicine added successfully", parent=self.window)
        # self.btnAddTop.mainloop()

    def addExistMedicine(self):
        self.reset()
        # ====================            ADD NEW BATCH OF EXISTING MEDICINE HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Restock  /\nAdd New Batch of \nExisting Medicine", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       MEDICINE DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelcnumber = Label(self.frameDetails, text="Code Number ", font=('arial', 12, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelcnumber.grid(row=0, column=0, rowspan=2)
        self.cNum = IntVar()
        self.ecNum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.cNum)
        self.ecNum.grid(row=2, column=0, padx=10)

        self.labelBNo = Label(self.frameDetails, text="Batch Number ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelBNo.grid(row=0, column=1, rowspan=2)
        self.bnum = StringVar()
        self.eBnum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.bnum)
        self.eBnum.grid(row=2, column=1, padx=10)

        self.labelexpD = Label(self.frameDetails, text="Expiry Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelexpD.grid(row=0, column=2, rowspan=2)
        self.expdate = StringVar()
        self.eExpdate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                              borderwidth=1,
                              textvariable=self.expdate)
        self.eExpdate.grid(row=2, column=2, padx=10)

        self.labelppu = Label(self.frameDetails, text="Price per Unit ", font=('arial', 12, 'bold'), bd=10,
                              bg="SkyBlue2", justify=LEFT)
        self.labelppu.grid(row=4, column=0, rowspan=2)
        self.pricepU = IntVar()
        self.ePPU = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.pricepU)
        self.ePPU.grid(row=6, column=0, padx=10)

        self.labelvid = Label(self.frameDetails, text="Vendor Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvid.grid(row=4, column=1, rowspan=2)
        self.vId = IntVar()
        self.eVId = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vId)
        self.eVId.grid(row=6, column=1, padx=10)

        self.labelavailQ = Label(self.frameDetails, text="Available Quantity ", font=('arial', 12, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelavailQ.grid(row=4, column=2, rowspan=2)
        self.availq = IntVar()
        self.eAvailq = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                             borderwidth=1,
                             textvariable=self.availq)
        self.eAvailq.grid(row=6, column=2, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Enter", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.addExisting())
        self.btnAddTop.grid(row=8, column=1, padx=20)

    def addExisting(self):
        """

        This function is used to add new batch of existing medicine

        """
        code_found = False
        flag = False
        instance = 0
        if self.bnum.get() != "" or self.availq.get() != 0 or self.cNum.get() != 0:
            for i in medicineInventory:
                if i["code_number"] == self.cNum.get():
                    code_found = True
                    instance = i
                    if str(i["Batch_no"]) == str(self.bnum.get()):
                        i["available_quantity"] += self.availq.get()
                        messagebox.showinfo("Success",
                                            "Available quantity of the medicines with code_no: " + str(i["code_number"]) +
                                            " and batch_no: " + i["Batch_no"] + " increased by " +
                                            str(self.availq.get()), parent=self.window)
                        with open("./Data/MedicineInventory.json", "w") as p:
                            json.dump(medicineInventory, p, indent=4)
                        flag = True
            if code_found is True and flag is False:
                if len(self.expdate.get()) != 10 or self.expdate.get()[2] != '-' or self.expdate.get()[5] != '-':
                    messagebox.showerror("Expiry Date formatting error!",
                                         "Enter the expiry date in DD-MM-YYYY format",
                                         parent=self.window)
                elif int(self.expdate.get()[3:5]) > 12:
                    messagebox.showerror("Expiry Date Entry Error!",
                                         "Enter a valid expiry date with proper month number",
                                         parent=self.window)
                elif (int(self.expdate.get()[0:2]) > 31) or (
                        int(self.expdate.get()[0:2]) > 30 and int(self.expdate.get()[3:5]) in [2, 4, 6, 9, 11]):
                    messagebox.showerror("Expiry Date Entry Error!",
                                         "Enter a valid expiry date with proper date number",
                                         parent=self.window)
                elif self.pricepU.get() <= 0:
                    messagebox.showwarning("Price must be non-negative!", "Enter valid price of medicine (> 0)",
                                           parent=self.window)
                else:
                    obj = {"code_number": self.cNum.get(),
                           "trade_name": instance["trade_name"],
                           "generic_name": instance["generic_name"],
                           "price_per_unit": self.pricepU.get(),
                           "Batch_no": self.bnum.get(),
                           "exp_date": self.expdate.get(),
                           "vendor_id": self.vId.get(),
                           "company_description": instance["company_description"],
                           "medicine_description": instance["medicine_description"],
                           "available_quantity": self.availq.get(),
                           "threshold_value": instance["threshold_value"],
                           "unit_selling": instance["unit_selling"]}
                    medicineInventory.append(obj)
                    with open("./Data/MedicineInventory.json", "w") as p:
                        json.dump(medicineInventory, p, indent=4)
                    messagebox.showinfo("Success", "New batch has been added.", parent=self.window)
                    flag = True
        elif self.cNum.get() == 0:
            messagebox.showerror("Code Number FIeld is empty!", "Enter the code number", parent=self.window)
            code_found = True
        elif self.bnum.get() == "":
            messagebox.showerror("Batch Number Field is empty!", "Enter the Batch Number", parent=self.window)
            code_found = True
        elif self.availq.get() == 0:
            messagebox.showerror("Available Quantity field is empty", "Enter the quantity of medicine to be added",
                                 parent=self.window)
            code_found = True
        # with open("./Data/MedicineInventory.json", "w") as p:
        #     json.dump(medicineInventory, p, indent=4)
        if not code_found:
            messagebox.showinfo("Failed", "No medicine with the given code number is found.", parent=self.window)

    def Query(self):
        """

        This function is used to query the medicine inventory

        """
        self.reset()
        # ====================            QUERY HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Query about a medicine", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       MEDICINE DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelqname = Label(self.frameDetails, text="Trade Name/Generic Name ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelqname.grid(row=0, column=0, rowspan=2)
        self.qName = StringVar()
        self.eQName = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.qName)
        self.eQName.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Enter", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.printmedicine())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def printmedicine(self):
        """

        This function is used to print the details of the medicine

        """
        flag = False
        if self.qName.get() == "":
            messagebox.showwarning("Invalid Entries!", "Fill all boxes", parent=self.window)
            flag = True

        for i in medicineInventory:
            if (i["trade_name"] == self.qName.get() or i["generic_name"] == self.qName.get()):
                flag = True
                self.reset()
                self.labelMed = Label(self.frame2, text="Medicine Info", font=('arial', 17, 'bold'),
                                               bd=20)
                self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
                self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                          bg="SkyBlue2")
                self.frameDetails.grid(row=1, column=0)
                self.labelName = Label(self.frameDetails, text="Medicine Generic Name ", font=('arial', 12, 'bold'), bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=0, column=0)
                self.labelName = Label(self.frameDetails, text=i["generic_name"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=0, column=1)
                self.labelName = Label(self.frameDetails, text="Code Number ", font=('arial', 12, 'bold'), bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=1, column=0)
                self.labelName = Label(self.frameDetails, text=i["code_number"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=1, column=1)
                self.labelID = Label(self.frameDetails, text="Available Qunatity", font=('arial', 12, 'bold'), bd=10,
                                     bg="SkyBlue2", justify=LEFT)
                self.labelID.grid(row=2, column=0)
                self.labelID = Label(self.frameDetails, text=i["available_quantity"], font=('arial', 12, 'bold'), bd=10,
                                     bg="SkyBlue2", justify=LEFT)
                self.labelID.grid(row=2, column=1)
                break
        if flag == False:
            messagebox.showwarning("Invalid Entries!", "Medicine Not Found", parent=self.window)

    def printexpiredlist(self):
        self.reset()
        # ====================            PRINT LIST HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="List of Expired Medicines", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Print", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.expirylist())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def expirylist(self):
        """

        This function is used to print the list of expired medicines

        """
        self.reset()
        self.labelMed = Label(self.frame2, text="List of Expired Medicines", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)
        t = self.tDate.get().split('-')
        t = [int(k) for k in t]
        d1 = date(t[2], t[1], t[0])
        self.labelName = Label(self.frameDetails, text="Medicine Generic/Trade Name", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)
        self.labelName = Label(self.frameDetails, text="Vendor Id", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)

        l=1
        for i in medicineInventory:
            temp = i["exp_date"]
            f = temp.split('-')
            f = [int(k) for k in f]
            d2 = date(f[2], f[1], f[0])
            if d1 > d2:
                s = i["generic_name"]
                if(s == ""):
                    s = i["trade_name"]
                self.labelName = Label(self.frameDetails, text=s, font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=l, column=0)
                self.labelName = Label(self.frameDetails, text=i["vendor_id"], font=('arial', 12, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2",
                                       justify=LEFT)
                self.labelName.grid(row=l, column=1)
                l=l+1

    def processOrder(self):
        self.reset()
        self.medicineQuantityPair = []
        self.CustomerOrder = []

        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Generate bill for\n customer order", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Medicine Code Number", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tmed = IntVar()
        self.eTmed = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tmed)
        self.eTmed.grid(row=2, column=0, padx=10)

        self.labeltdate = Label(self.frameDetails, text="Quantity", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                                justify=LEFT)
        self.labeltdate.grid(row=0, column=1, rowspan=2)
        self.tQ = IntVar()
        self.eTQ = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tQ)
        self.eTQ.grid(row=2, column=1, padx=10)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=2, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=2, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Add to list", font=('arial', 12, 'bold'), width=15,
                                command=lambda: self.medicineQuantityPairFunction())
        self.btnAddTop.grid(row=2, column=3, padx=20)

        self.btnAddTop = Button(self.frameDetails, text="Print Bill", font=('arial', 12, 'bold'), width=15,
                                command=lambda: self.printcustomerorder())
        self.btnAddTop.grid(row=4, column=1, padx=20)

    def medicineQuantityPairFunction(self):
        """

        This function is used to add the medicine code and quantity to the list

        """
        flag = False
        flag2 = False
        x = 0
        for i in medicineInventory:
            if(i["code_number"]==self.tmed.get()):
                flag = True
                x = i["available_quantity"]
            if(i["code_number"]==self.tmed.get() and i["available_quantity"] > self.tQ.get()):
                flag2 = True

        if not flag:
            messagebox.showinfo("Error", "Medicine with code number:" + str(self.tmed.get()) + " is unavailabe", parent=self.window)
            flag2=True
        if not flag2:
            messagebox.showinfo("Error", "Requested Quantity(" + str(self.tQ.get()) + ") exceeds available quantity(" + str(x) +")",
                                parent=self.window)
        if flag and flag2:
            self.medicineQuantityPair = [self.tmed.get(), self.tQ.get(), self.tDate.get()]
            self.CustomerOrder.append(self.medicineQuantityPair)
            c_order = {"code_number": self.tmed.get(),
                      "quantity": self.tQ.get(),
                      "order_date": self.tDate.get()}
            customerorder.append(c_order)
            with open("./Data/customerOrder.json", "w") as p:
                json.dump(customerorder, p, indent=4)

    def printcustomerorder(self):
        self.reset()
        self.labelMed = Label(self.frame2, text="Customer Bill", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelName = Label(self.frameDetails, text="Medicine Generic Name", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)

        self.labelName = Label(self.frameDetails, text="Quantity", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)

        self.labelName = Label(self.frameDetails, text="Price Per Unit", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=2)
        cost = 0
        l=1
        for i in self.CustomerOrder:
            for j in medicineInventory:
                if j["code_number"] == i[0]:
                    j["available_quantity"] = j["available_quantity"] - i[1]
                    with open("./Data/MedicineInventory.json", "w") as p:
                        json.dump(medicineInventory, p, indent=4)
                    self.labelName = Label(self.frameDetails, text=j["generic_name"], font=('arial', 12, 'bold'),
                                           bd=10,
                                           bg="SkyBlue2",
                                           justify=LEFT)
                    self.labelName.grid(row=l, column=0)

                    self.labelName = Label(self.frameDetails, text=str(i[1]), font=('arial', 12, 'bold'),
                                           bd=10,
                                           bg="SkyBlue2",
                                           justify=LEFT)
                    self.labelName.grid(row=l, column=1)

                    self.labelName = Label(self.frameDetails, text=j["price_per_unit"], font=('arial', 12, 'bold'),
                                           bd=10,
                                           bg="SkyBlue2",
                                           justify=LEFT)
                    self.labelName.grid(row=l, column=2)
                    l = l + 1
                    cost = cost + (i[1]*j["price_per_unit"])

        if cost>0 :
            self.labelName = Label(self.frameDetails, text="TOTAL COST            =", font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=1)

            self.labelName = Label(self.frameDetails, text=str(cost), font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=2)

    def printandstorerequirement(self):
        """

        This function is used to print and store the medicine requirement

        """
        self.reset()
        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Requirement for the next day", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeltdate = Label(self.frameDetails, text="Enter Date(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labeltdate.grid(row=0, column=0, rowspan=2)
        self.tDate = StringVar()
        self.eTDate = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.tDate)
        self.eTDate.grid(row=2, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Print", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.printnstore())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def thresholdValueUpdation(self):
        #                  ****  UPDATING THRESHOLD VALUES   *******
        code_numbers_threshold = {}
        last_week = []
        now = datetime.strptime(str(self.tDate.get()), '%d-%m-%Y')
        for x in range(7):
            d = now - timedelta(days=x + 1)
            y = d.strftime("%d-%m-%Y")
            last_week.append(y)

        for i in medicineInventory:
            #     # add medicine to list
            if code_numbers_threshold.get(i["code_number"]) == None:
                code_numbers_threshold[i["code_number"]] = 0

        for i in customerorder:
            # For each order in previous week, increase quantity for corresponding medicine
            if i["order_date"] in last_week:
                code_numbers_threshold[i["code_number"]] += i["quantity"]

        # Update threshold for each medicine in inventory
        for j in medicineInventory:
            j["threshold_value"] = int(code_numbers_threshold.get(j["code_number"]))

            # Upadate the threshold values data in the file
            with open("./Data/MedicineInventory.json", "w") as p:
                json.dump(medicineInventory, p, indent=4)

        # Check quantity of each medicine per code_number
        code_numbers_quantity = {}
        for i in medicineInventory:
            if code_numbers_quantity.get(i["code_number"]) == None:
                code_numbers_quantity[i["code_number"]] = 0
            code_numbers_quantity[i["code_number"]] += i["available_quantity"]

        self.requirementsPerDay = {}
        for code_number, threshold in code_numbers_threshold.items():
            if threshold > code_numbers_quantity[code_number]:
                self.requirementsPerDay[code_number] = int(threshold) - code_numbers_quantity[code_number]
                #print(self.requirementsPerDay[code_number])

    def printnstore(self):
        current_date = str(self.eTDate.get())
        # set condition for updation:
        self.thresholdValueUpdation()
        #             ***********  PRINTING THE REQUIREMNTS   ********
        self.reset()
        self.labelMed = Label(self.frame2, text="List of Required Medicines Medicines", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelName = Label(self.frameDetails, text="Code number", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)
        self.labelName = Label(self.frameDetails, text="quantity", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)
        l = 1
        for key, value in self.requirementsPerDay.items():
            self.labelName = Label(self.frameDetails, text=key, font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=0)
            self.labelName = Label(self.frameDetails, text=value, font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=1)
            l = l + 1

    def operationsonvendors(self):
        self.reset()
        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Add Vendor", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelvid = Label(self.frameDetails, text="Enter Vendor Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvid.grid(row=0, column=0, rowspan=2)
        self.vId = IntVar()
        self.eVId = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vId)
        self.eVId.grid(row=2, column=0, padx=10)

        self.labelvname = Label(self.frameDetails, text="Enter Vendor Name ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvname.grid(row=0, column=1, rowspan=2)
        self.vName = StringVar()
        self.eVName = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vName)
        self.eVName.grid(row=2, column=1, padx=10)

        self.labelvadd = Label(self.frameDetails, text="Enter Vendor Address ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvadd.grid(row=0, column=2, rowspan=2)
        self.vAdd = StringVar()
        self.eVAdd = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vAdd)
        self.eVAdd.grid(row=2, column=2, padx=10)

        self.labelvcnum = Label(self.frameDetails, text="Enter Code Numbers of Medicines ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                              justify=LEFT)
        self.labelvcnum.grid(row=3, column=0, rowspan=2)
        self.vCnum = StringVar()
        self.eVCnum = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.vCnum)
        self.eVCnum.grid(row=5, column=0, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Enter", font=('arial', 12, 'bold'), width=5,
                                command=lambda: self.addVendor())
        self.btnAddTop.grid(row=5, column=2, padx=20)

    def addVendor(self):
        """

        This function is used to add the vendor details to the database

        """
        var2 = {
            "vendor_id": self.vId.get(),
            "code_numers": self.vCnum.get(),
            "vendor_name": self.vName.get(),
            "vendor_address": self.vAdd.get()
        }

        vendorlist.append(var2)

        with open("./Data/vendorDetails.json", "w") as p:
            json.dump(vendorlist, p, indent=4)
            messagebox.showinfo("Success", "Vendor added succesfully", parent=self.window)

    def producecheque(self):
        self.reset()
        self.vendorchequelist = []
        self.VendorCheque = []

        # ====================            PROCESS CUSTOMER HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Generate cheque for vendor", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelpcmcn = Label(self.frameDetails, text="Medicine Code Number", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelpcmcn.grid(row=0, column=0, rowspan=2)
        self.Pcmcn = IntVar()
        self.ePCmcn = Entry(self.frameDetails, width=15, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.Pcmcn)
        self.ePCmcn.grid(row=2, column=0, padx=10)

        self.labelpcq = Label(self.frameDetails, text="Quantity", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                                justify=LEFT)
        self.labelpcq.grid(row=0, column=1, rowspan=2)
        self.Pcq = IntVar()
        self.ePCq = Entry(self.frameDetails, width=15, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.Pcq)
        self.ePCq.grid(row=2, column=1, padx=10)

        self.labelpcmbn = Label(self.frameDetails, text="Medicine Batch Number", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelpcmbn.grid(row=0, column=2, rowspan=2)
        self.Pcmbn = StringVar()
        self.ePCmbn = Entry(self.frameDetails, width=15, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.Pcmbn)
        self.ePCmbn.grid(row=2, column=2, padx=10)

        self.labelpced = Label(self.frameDetails, text="Expiry Date(DD-MM-YYYY)", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                                justify=LEFT)
        self.labelpced.grid(row=0, column=3, rowspan=2)
        self.Pced = StringVar()
        self.ePCed = Entry(self.frameDetails, width=15, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.Pced)
        self.ePCed.grid(row=2, column=3, padx=10)

        self.labelpcvi = Label(self.frameDetails, text="Vendor Id", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelpcvi.grid(row=0, column=4, rowspan=2)
        self.Pcvi = IntVar()
        self.ePCvi = Entry(self.frameDetails, width=15, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.Pcvi)
        self.ePCvi.grid(row=2, column=4, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Add to list", font=('arial', 12, 'bold'), width=15,
                                command=lambda: self.vendorQuantityPairFunction())
        self.btnAddTop.grid(row=4, column=2, padx=20)

        self.btnAddTop = Button(self.frameDetails, text="Print Bill", font=('arial', 12, 'bold'), width=15,
                                command=lambda: self.printvendorcheque())
        self.btnAddTop.grid(row=4, column=3, padx=20)

    def vendorQuantityPairFunction(self):
        flag = False
        for i in medicineInventory:
            if(i["code_number"]==self.Pcmcn.get()):
                flag = True
        if not flag:
            messagebox.showinfo("Medicine with given code number is unavailabe", "First add the medicine to the medicine inventory", parent=self.window)
        if flag:
            self.vendorchequelist = [self.Pcmcn.get(),self.Pcq.get(),self.Pcmbn.get(),self.Pced.get(),self.Pcvi.get()]
            self.VendorCheque.append(self.vendorchequelist)

    def printvendorcheque(self):
        """

        This function is used to print the vendor cheque

        """
        self.reset()
        self.labelMed = Label(self.frame2, text="Vendor Cheque", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelName = Label(self.frameDetails, text="Vendor Id", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)

        self.labelName = Label(self.frameDetails, text="Date", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)

        self.labelName = Label(self.frameDetails, text="Total Amount", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=2)
        amount = 0
        l=1
        for i in self.VendorCheque:
            for j in medicineInventory:
                if j["code_number"] == i[0]:
                    j["available_quantity"] = j["available_quantity"] - i[1]
                    with open("./Data/MedicineInventory.json", "w") as p:
                        json.dump(medicineInventory, p, indent=4)
                    amount = amount + (i[1]*j["price_per_unit"])

        if amount>0 :
            self.labelName = Label(self.frameDetails, text=str(self.Pcmcn.get()), font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=0)

            self.labelName = Label(self.frameDetails, text=str(time.strftime("%d-%m-%Y")), font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=1)

            self.labelName = Label(self.frameDetails, text=str(amount), font=('arial', 12, 'bold'),
                                   bd=10,
                                   bg="SkyBlue2",
                                   justify=LEFT)
            self.labelName.grid(row=l, column=2)

    def Generate(self):
        """

        This function is used to generate the revenue between any two given time periods

        """
        self.reset()
        # ====================            GENERATE REVENUE AND PROFIT HEADING             ===================================================================================

        self.labelExistMed = Label(self.frame2, text="Generate Revenue ", font=('arial', 17, 'bold'),
                                   bd=20)
        self.labelExistMed.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       DATE DETAILS FRAME            ==============================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelt1date = Label(self.frameDetails, text="Enter Date1(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelt1date.grid(row=0, column=0, rowspan=2)
        self.t1Date = StringVar()
        self.eT1Date = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.t1Date)
        self.eT1Date.grid(row=2, column=0, padx=10)

        self.labelt2date = Label(self.frameDetails, text="Enter Date2(DD-MM-YYYY) ", font=('arial', 12, 'bold'), bd=10,
                                bg="SkyBlue2", justify=LEFT)
        self.labelt2date.grid(row=0, column=1, rowspan=2)
        self.t2Date = StringVar()
        self.eT2Date = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                            borderwidth=1,
                            textvariable=self.t2Date)
        self.eT2Date.grid(row=2, column=1, padx=10)

        self.btnAddTop = Button(self.frameDetails, text="Generate", font=('arial', 12, 'bold'), width=10,
                                command=lambda: self.revenue())
        self.btnAddTop.grid(row=4, column=0, padx=20)

    def revenue(self):
        self.reset()
        self.labelMed = Label(self.frame2, text="Total Revenue", font=('arial', 17, 'bold'),
                              bd=20)
        self.labelMed.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        t = self.t1Date.get().split('-')
        t = [int(k) for k in t]
        d1 = date(t[2], t[1], t[0])
        h = self.t2Date.get().split('-')
        h = [int(k) for k in h]
        d2 = date(h[2], h[1], h[0])
        rev=0
        for i in customerorder:
            temp = i["order_date"]
            f = temp.split('-')
            f = [int(k) for k in f]
            d3 = date(f[2], f[1], f[0])
            if d1 < d3 and d3 < d2:
                for j in medicineInventory:
                    if i["code_number"] == j["code_number"]:
                        rev = rev + (i["quantity"]*j["price_per_unit"])
        self.labelName = Label(self.frameDetails, text=self.t1Date.get()+" to "+self.t2Date.get()+"    =", font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)

        self.labelName = Label(self.frameDetails, text="Rs. "+str(rev), font=('arial', 12, 'bold'),
                               bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)

    def reset(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()


def main():
    root = Tk()
    run = MainWindow(root)
    return


shopowner_ = json.load(open("./Data/LogInCredentials.json"))
shopowner = LogInCredentials(shopowner_["name"], shopowner_["ID"], shopowner_["password"])
medicineInventory = json.load(open("./Data/MedicineInventory.json"))
vendorlist = json.load(open("./Data/vendorDetails.json"))
customerorder = json.load(open("./Data/customerOrder.json"))

if __name__ == '__main__':
    main()
