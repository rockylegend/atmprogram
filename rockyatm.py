import random
import mysql.connector
from prettytable import from_db_cursor
from datetime import datetime
import time
import maskpass
import re

class ATM:
    myconn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="atm7")
    conn=myconn.cursor()

    # conn.execute('''create database atm7''')
    date_time = datetime.fromtimestamp(time.time())

    def __init__ (self,name="adarsh",mobile_number=1234567891,Transaction_date_time="2023-03-24 12:12:12",email_id="singhaadarsh937@gmail.com",admin_balance1=0,balance=0):
        self.name = name
        self.mobile_number = mobile_number
        self.balance = balance
        self.amount=0
        self.amount1=0
        self.Transaction_date_time=Transaction_date_time
        self.email_id=email_id
        self.admin_balance1=admin_balance1
        # self.mydb =mysql.connector.connect(host='localhost',user='root',password='123456789',database='atm7')
        # self.conn = self.mydb.cursor()
            
    
    # def dele(self):
    #     var2=int(input("Enter the ID Number: "))
    #     query=f'delete from deposit121 where id={var2}'
    #     self.conn.execute(query)
    #     self.myconn.commit()
    #     # self.conn.execute("select * from deposit121")
    #     # table=from_db_cursor(self.conn)
    #     # print(table)

    def account_detail(self):
        query = '''create table if not exists detail222(id int not null auto_increment,Name varchar(250),Email_iD varchar(250),mobile_number varchar(250),balance int(250),Transaction_Date_Time datetime,primary key(id))'''
        self.conn.execute(query)

        value=[(name,email_id,mobile_number,self.balance,self.date_time)]
        self.conn.executemany("insert into detail222(Name,Email_id,mobile_number,balance,Transaction_Date_Time) values(%s,%s,%s,%s,%s)",value)
        self.myconn.commit()

        # self.conn.executemany("select * from detail1 where Name= %s",[(name,)])
        self.conn.execute(f"select * from detail222 where Name='{name}'")
        table=from_db_cursor(self.conn)
        print(table)
        
    def admin(self):
        query = '''create table if not exists admin1(admin_deposit int(250),admin_balance int(250),Transaction_Date_Time datetime)'''
        self.conn.execute(query)

        self.admin_deposit=0
        try:
            self.admin_deposit=int(input("Enter Admin Deposit Rs: "))
        except:
            print("WRONG INPUT")

        self.admin_balance1=self.admin_deposit+100000
        self.user_deposit_admin=self.admin_balance1+self.amount
        self.user_withdraw_admin=self.admin_balance1-self.amount1
        print("Admin Total Balance:",self.user_deposit_admin)
        value=[(self.admin_deposit,self.admin_balance1,self.date_time)]
        self.conn.executemany("insert into admin1 value(%s,%s,%s)",value)
        self.myconn.commit()
        self.conn.execute("select * from admin1")
        table=from_db_cursor(self.conn)
        # print(table)
        print(table[-1])
    
    def admin_balance(self):
        self.user_deposit_admin=self.admin_balance1+self.amount
        self.user_withdraw_admin=self.admin_balance1-self.amount1
        print("Admin Balance After User Deposit: ",self.user_deposit_admin,"Rs")
        print("Admin Balance After User Withdraw: ",self.user_withdraw_admin,"Rs")
        query = '''create table if not exists admin_balance2(Admin_Balance_User_Deposit int(250),Admin_Balance_User_withdraw int(250),Transaction_Date_Time datetime)'''
        self.conn.execute(query)
        value=[(self.user_deposit_admin,self.user_withdraw_admin,self.date_time)]
        self.conn.executemany("insert into admin_balance2 value(%s,%s,%s)",value)
        self.myconn.commit()
        self.conn.execute("select * from admin_balance2")
        table=from_db_cursor(self.conn)
        # print(table)
        print(table[-1])

    
    def user_details(self):
        while True:
        # var=input("do you want to see the All transaction detail(y/n) : ")
            print("1: User Deposit\n2: User Withdraw\n3: Exit")
            j=int(input("Enter Option: "))

            if j==1:
                self.conn.execute("select * from deposit121")
                table=from_db_cursor(self.conn)
                print(table)

                var1=input("do you want to delete any queries(y/n): ")
                if var1=="y":
                    var2=int(input("Enter the ID Number: "))
                    query=f'delete from deposit121 where id={var2}'
                    self.conn.execute(query)
                    self.myconn.commit()
                    self.conn.execute("select * from deposit121")
                    table=from_db_cursor(self.conn)
                    print(table)
                    # atm.dele()
                else:
                    break
            elif j==2:
                self.conn.execute("select * from withdraw12")
                table=from_db_cursor(self.conn)
                print(table)

                var1=input("do you want to delete any queries(y/n): ")
                if var1=="y":
                    var3=int(input("Enter the ID Number: "))
                    query=f'delete from withdraw12 where id={var3}'
                    self.conn.execute(query)
                    self.myconn.commit()
                    self.conn.execute("select * from withdraw12")
                    table=from_db_cursor(self.conn)
                    print(table)
                else:
                    break
            elif j==3:
                break
            else:
                print("Wrong Input")


    def deposit(self, amount):
        query = '''create table if not exists deposit121(id int not null auto_increment,Name varchar(250),deposit_amount int(250),deposit_balance int(250),Transaction_Date_Time datetime,primary key(id))'''
        self.conn.execute(query)

        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance:",self.balance," Rs.")
        value=[(name,self.amount,self.balance, self.date_time)]
        self.conn.executemany("insert into deposit121(Name,deposit_amount,deposit_balance,Transaction_Date_Time) values(%s,%s,%s,%s)",value)
        self.myconn.commit()
        self.conn.execute(f"select * from deposit121 where Name='{name}'")
        table=from_db_cursor(self.conn)
        print(table)

    def withdraw(self, amount1):
        self.amount1 = amount1
        if self.amount1 > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} Rs. only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            query = '''create table if not exists withdraw12(id int not null auto_increment,Name varchar(250),withdraw_amount int(250),Available_balance int(250),Transaction_Date_Time datetime,primary key(id))'''
            self.conn.execute(query)

            self.balance = self.balance - self.amount1
            print(f"{amount1} Rs. withdrawal successful!")
            print("Current account balance: ",self.balance,"Rs.")
            print()

            value=[(name,self.amount1,self.balance, self.date_time)]
            self.conn.executemany("insert into withdraw12(Name,withdraw_amount,Available_balance,Transaction_Date_Time) values(%s,%s,%s,%s)",value)
            self.myconn.commit()
            self.conn.execute(f"select * from withdraw12 where Name='{name}'")
            table=from_db_cursor(self.conn)
            print(table)
    def check_balance(self):
        print("Available balance: ", self.balance," Rs.")
        print()

        query = '''create table if not exists last_balance56(id int not null auto_increment,Name varchar(250),Available_balance int(250),Transaction_Date_Time datetime,primary key(id))'''
        self.conn.execute(query)
        
        value=[(name,self.balance, self.date_time)]
        self.conn.executemany("insert into last_balance56(Name,Available_balance,Transaction_Date_Time) values(%s,%s,%s)",value)
        self.myconn.commit()
        self.conn.execute(f"select * from last_balance56 where Name='{name}'")
        table=from_db_cursor(self.conn)
        print(table)

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)

        while True:
            try:
                option = int(input("Enter:\n1. Account Detail\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Exit\nEnter Option:"))
            except:
                print("Please Enter 1, 2, 3, 4, or 5 only!\n")
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    # amount=0
                    amount = int(input("How much you want to deposit: "))
                    atm.deposit(amount)
                elif option == 4:
                    amount1 = int(input("How much you want to withdraw: "))
                    atm.withdraw(amount1)
                elif option == 5:
                    print(f"""
             ----------------------------------
            |  printing receipt..............  |
             ----------------------------------

                ------BANK OF BARODA------
          ******************************************
              Transaction is now complete :).                         
              Transaction number: {random.randint(10000, 1000000)}
              Account holder: {name.upper()}                  
              Phone number: {mobile_number}
              Email ID : {email_id}               
              Available balance: {self.balance} Rs.
              Date/Time : {self.date_time} 
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                
           ----------------------------------------
          |   Thanks for choosing us as your bank  |  
           ----------------------------------------
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^              
          ******************************************
          """)
                    break

def admin():
        try:
            pin=int(maskpass.askpass("ENTER ADMIN PASSWORD: ",mask="*"))
            if pin==1234:
                while True:
                    print("1: Deposit \n2: Admin_Balance \n3: User Transaction Details \n4: Exit")
                    choose=input("PLEASE CHOOSE YOUR CHOICE: ")
                    if choose=="1":
                        atm.admin()
                        # break
                    elif choose=="2":
                        atm.admin_balance()
                    elif choose=="3":
                        atm.user_details()
                    elif choose=="4":
                        break
            else:
                print("INVALID PIN :(\n")
        except:
            print("Wrong Input :(")

def yn():
    while True:
        trans = input("Do you want to do any transaction?(y/n):")
        if trans == "y":
            atm.transaction()
            break
        elif trans == "n":
            print("___________________________________________________________\n")
            print("----------ATM RECEIPT CREATION----------")
            print("""
        -------------------------------------
        | Thanks for choosing us as your bank |
        | Visit us again!                     |
        -------------------------------------
            """)
            break
        else:
            print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
def user():
        print(" __________________________")
        print("|                          |")
        print("|  PLEASE INSERT YOUR CARD |")
        print("|__________________________|")
        print()
        print("WAIT >>>>>>>>>>>>>>>>>>>>>>>>>>")
        while True:
            email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
            var={"aadarsh":[8850432528,5678,"aadarsh123@gmail.com"],"suyog":[9967613212,3333,"suyog123@gmail.com"],"rohit":[1234567891,1234,"rohit123@gmail.com"],"sandeep":[8108517423,1111,"sandeep123@gmail.com"],"pooja":[1111222233,2001,"pooja123@gmail.com"],"shruti":[9876543210,2020,"shruti123@gmail.com"]}
            try:
                global name
                name = input("Enter Your Name: ")
            except:
                print("Enter Your Right Name")
            if name in var:
                print("------------ Your Name Sucessfully Match ------------")
                print()
                try:
                    global mobile_number
                    mobile_number = int(input("Enter Your Mobile Number: "))
                except:
                    print("???????????? WRONG MOBILE NUMBER ????????????")
                if var[name][0]==mobile_number:
                    print("============ Your Number Successfully Match ============")
                    print()
                    if len(str(mobile_number))==10:
                        # print("============ Your Number Sucessfully Match ============")
                        print()
                        global email_id
                        email_id=input("Enter Your Email: ")
                        if var[name][2]==email_id:
                            print("============ Your Email Sucessfully Match ============")
                            print()
                            if re.search(email_condition,email_id):
                                print("============ Right Email Validation ============")
                                print()
                                pin=int(maskpass.askpass("ENTER YOUR 4 DIGIT PIN NUMBER: ",mask="*"))
                                if pin==var[name][1]:
                                    print("+++++++++++++ Successfully Enter........ :) +++++++++++++")
                                    print("============= Welcome Bank Of Baroda =============")
                                    print("Name:",name)
                                # while True:
                                # trans = input("Do you want to do any transaction?(y/n):")
                                # if trans == "y":
                                #     atm.transaction()
                                #     break
                                # elif trans == "n":
                                #     print("___________________________________________________________\n")
                                #     print("----------ATM RECEIPT CREATION----------")
                                #     print("""
                                # -------------------------------------
                                # | Thanks for choosing us as your bank |
                                # | Visit us again!                     |
                                # -------------------------------------
                                #     """)
                                #     break
                                # else:
                                #     print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
                                    yn()
                                    break
                                else:
                                    print("------------ Wrong Password !!!!! ------------")
                                    print("------------ Please Try Again!!!! ------------") 
                                    print()  
                            else:
                                print("!!!!!! Wrong Email :( !!!!!!")
                                print("------------ Please Try Again!!!! ------------") 
                                print()
                        else:
                            print("============ Your Email NOT Match ============")
                            print("------------ Please Try Again!!!! ------------") 
                            print()
                    else:
                        print("Alert ! Enter Minimum 10 Number")
                        print("------------ Please Try Again!!!! ------------") 
                        print()
                else:
                    print("------------ Your Number doesn't match ------------")
                    print() 
                    print("------------ Please Try Again!!!! ------------") 
                    print()
            else:
                print("------------ Your name Doesn't match ------------")
                print("------------ Please Try Again!!!! ------------") 
                print()
        # else:
        #     print("Wrong Input")
                 
atm = ATM()
print("*******WELCOME TO BANK OF BARODA*******")
while True:
    print("1. Admin Panel")
    print("2. User Panel")
    print("3. Exit")
    choice=input("Enter Your Choice: ")
    if choice=="1":
        admin()
    elif choice=="2":
        user()
    elif choice=="3":
        exit()
    else:
        print("Wrong Input")