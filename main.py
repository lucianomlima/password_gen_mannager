from tkinter import *
import mysql.connector as my_sq, string, random, csv
from tkinter import messagebox


window = Tk()
window.title('My Password Generator')
window.geometry("1015x605")
window.configure(background="#999999")
window.resizable(0, 0)

#  All MySQL

try:
    my_db = my_sq.connect(host='localhost', user='root', passwd='', )
    my_cur = my_db.cursor()

    try:
        my_cur.execute('use mypassword')

        try:
            df = 'Select * from password'
            my_cur.execute(df)
            my_cur.fetchall()
        except Exception:
            my_cur.execute(
                'create table password(name varchar(255) not null, app_name varchar(50) not null, length int('
                '30) not null, word varchar(255), info varchar(255), paas varchar(50) not null)')
    except Exception:
        my_cur.execute('create database mypassword')
        my_cur.execute('use mypassword')
        my_cur.execute('create table password(name varchar(255) not null, app_name varchar(50) not null, length int('
                       '30) not null, word varchar(255), info varchar(255), paas varchar(50) not null)')
        my_cur.execute('show tables')
        for i in my_cur:
            print(i)
except Exception:
    messagebox.showerror('Error', 'MySQL Connection Failed')


#  ALL DEF

def generate():
    try:
        if E3.get() == '':
            messagebox.showwarning('Error', "Length Field Cannot be Empty")
        elif int(E3.get()) == 0:
            messagebox.showwarning('Error', "Length Cannot be Zero")
        else:
            E6.configure(state='normal')
            B4["state"] = NORMAL
            E6.delete('1.0', 'end')
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = ['@', '#', '$', '%', '&', '*', '!']
            s5 = list(E4.get().split("-"))
            s6 = []
            s6.extend(list(s1))
            s6.extend(list(s2))
            s6.extend(list(s3))
            s6.extend(list(s4))
            # prints
            random.shuffle(s6)
            s7 = (s6[0:int(E3.get())])
            s7.extend(list(s5))
            random.shuffle(s7)
            x = "".join(s7[0:int(E3.get()) + 1])
            E6.insert(END, x)
    except ValueError:
        messagebox.showwarning('Error', 'Input Length in Natural Numbers')


def save_pass():
    try:
        if E1.get == '' or E2.get() == '' or E3.get() == '':
            messagebox.showerror('error', 'First three Fields are compulsory to fill.')
        else:
            sql = "insert into password values(%s,%s,%s,%s,%s,%s)"
            name = E1.get()
            app_name = E2.get()
            length = E3.get()
            word = E4.get()
            info = E5.get()
            paas = E6.get('1.0', 'end')
            val = (name, app_name, length, word, info, paas)
            my_cur.execute(sql, val)
            my_db.commit()
            B4["state"] = DISABLED
            messagebox.showinfo('Success', 'Information saved in database successfully')
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
            E6.delete('1.0', 'end')
            E6.configure(state='disabled')
    except Exception:
        messagebox.showinfo('Error', 'Information Not Saved. It seems that you are not connected to MySQL Server')


def save_excel():
    try:
        my_cur.execute('SELECT * FROM password')
        results = my_cur.fetchall()
        with open('password_file.csv', 'w', newline='')as f:
            w = csv.writer(f, dialect='excel')
            for record in results:
                w.writerow(record)
        messagebox.showinfo('Success', 'All passwords exported to excel. Search for ''password_file.csv'' where the '
                                       'program is saved.')
    except Exception:
        messagebox.showinfo('Error', 'Unable to fetch data from database. Make sure you are connected to the MySQL '
                                     'server.')


def secure():
    B5["state"] = DISABLED

    root = Tk()
    root.title('Secure your Password')
    root.geometry('600x300')
    root.configure(background='#999999')
    root.iconbitmap('ico.ico')
    root.resizable(0, 0)

    def dele():
        try:
            root.destroy()
            window.destroy()
        except Exception:
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", dele)

    def enable():
        B5["state"] = NORMAL
        root.destroy()

    def spas():
        if e1.get() == '':
            messagebox.showerror("Error", "you can't leave the field empty")
        else:
            T1.configure(stat='normal')
            T1.delete('1.0', 'end')
            SECURE = (('w', 'm'),
                      ('s', '$'), ('S', '$'), ('a', '@'), ('i', '!'), (' ', '_'), ('h', '#'), ('o', '0'), ('and', '&'),
                      ('B', '8'),
                      ('l', '|'), ('v', '^'), ('X', '*'), ('m', 'w'), ('q', '%'))
            password = e1.get()
            for a, b in SECURE:
                password = password.replace(a, b)
            T1.insert(END, password)
            b2["state"] = NORMAL

    def savesp():
        try:
            if E1.get() == '' or E2.get() == '':
                messagebox.showerror("Error", "Please fill your name and app name in previous window, then try again")
            else:
                E3.delete(0, END)
                E4.delete(0, END)
                sql = "insert into password values(%s,%s,%s,%s,%s,%s)"
                name = E1.get()
                app_name = E2.get()
                length = ''
                word = ''
                info = E5.get() + 'Password Generated from Secure Password'
                paas = T1.get('1.0', 'end')
                val = (name, app_name, length, word, info, paas)
                my_cur.execute(sql, val)
                my_db.commit()
                messagebox.showinfo('Success', 'Information saved in database successfully')
                E1.delete(0, END)
                E2.delete(0, END)
                E5.delete(0, END)
                E6.delete('1.0', 'end')
                e1.delete(0, END)
                T1.delete('1.0', 'end')
                b2["state"] = DISABLED

        except Exception:
            messagebox.showinfo('Error', 'Information Not Saved. It seems that you are not connected to MySQL Server')

    def remem():
        messagebox.showinfo('how to remember', "Some letters are replaced by another (w - m),(s - $), (S - $),(a - @), "
                                               "('i - !'), (' '- _), ('h - #'), ('o - 0'), ('and - &'),('B - 8'),"
                                               "('l - |'), ('v - ^'), ('X - *'), ('m - w'), ('q - %')")

    l1 = Label(root, text='Enter Any Password :', font='Candara 13', background='#999999')
    l1.grid(row=0, column=0, padx=20, pady=20, sticky=W)
    e1 = Entry(root, width=30, font='Candara 13')
    e1.grid(row=0, column=1, padx=20, pady=20)
    l2 = Label(root, text='Your Secure Password Is :', font='Candara 13', background='#999999')
    l2.grid(row=1, column=0, padx=20, pady=20, sticky=W)
    T1 = Text(root, width=30, height=1, font='Candara 13')
    T1.grid(row=1, column=1, padx=20, pady=20)
    T1.configure(state='disabled')
    b1 = Button(root, text='Generate secure Password', width=25, font='Candara 13', command=spas)
    b1.grid(row=2, column=0, padx=20, pady=20)
    b2 = Button(root, text='Save Password', width=25, font='Candara 13', state=DISABLED, command=savesp)
    b2.grid(row=2, column=1, padx=20, pady=20)
    b3 = Button(root, text='How to Remember This Pass.', width=25, font='Candara 13', command=remem)
    b3.grid(row=3, column=0, padx=20, pady=20)
    root.protocol("WM_DELETE_WINDOW", enable)

    mainloop()


def showpass():
    try:
        B1["state"] = DISABLED

        win = Tk()
        win.title('See All Saved Passwords')
        win.geometry('995x427')
        win.configure(background='#999999')
        win.iconbitmap('ico.ico')
        win.resizable(0, 0)

        frame = Frame(win)
        scroll = Scrollbar(frame, orient=VERTICAL)
        lb = Listbox(frame, selectmode=EXTENDED, width=105, height=15, font='Candara 13', yscrollcommand=scroll.set,
                     background='#C0C0C0')
        lb.pack(padx=20, pady=20)
        scroll.config(command=lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        frame.pack()
        sql = "select * from password "
        my_cur.execute(sql)
        record = my_cur.fetchall()
        n = 1
        for row in record:
            lb.insert(END, str(n) + '     ' +
                      str(row[0]) + '   ||     ' + str(row[1]) + '   ||    ' + str(row[2]) + '   ||     ' + str(
                row[3]) + '    ||    ' + str(row[4]) + '   ||        ' + str(row[5]))
            n = n + 1

        def deleteAll():
            msg = messagebox.askyesno('Alert', 'Do you want to delete all saved passwords from database')
            if msg:
                lb.delete(0, END)
                my_cur.execute('TRUNCATE TABLE password')
                my_db.commit()

            else:
                pass

        def deleteselected():

            xs = messagebox.askyesno('Alert', 'Do you want to permanently delete the password from database')
            if xs:
                sql = "select * from password"
                my_cur.execute(sql)
                records = my_cur.fetchall()
                n = 1
                # print(lb.get(ANCHOR))
                for row in records:
                    while (lb.get(ANCHOR)) == (
                            str(n) + '     ' + str(row[0]) + '   ||     ' + str(row[1]) + '   ||    ' + str(
                            row[2]) + '   ||     ' + str(row[3]) + '    ||    ' + str(row[4]) + '   ||        ' + str(
                        row[5])):
                        cf = "delete from password  where paas ='%s'" % (row[5])
                        my_cur.execute(cf)
                        my_db.commit()
                        # print('passs')
                        # print(row[5])
                        n += 1
                        pass
                    n += 1
                lb.delete(ANCHOR)
            else:
                return

        def delt():
            try:
                win.destroy()
                window.destroy()
            except Exception:
                window.destroy()

        def sd():
            B1["state"] = NORMAL
            win.destroy()

        window.protocol("WM_DELETE_WINDOW", delt)

        button2 = Button(frame, text="Delete All Passwords", font='Candara 13', command=deleteAll, width=50, height=2,
                         background='#999999', relief=GROOVE)
        button2.pack(side=LEFT, padx=40, pady=5)

        button3 = Button(frame, text="Delete selected Password", font='Candara, 13', command=deleteselected, width=50,
                         height=2, background='#999999', relief=GROOVE)
        button3.pack(side=RIGHT, padx=40, pady=5)
        win.protocol("WM_DELETE_WINDOW", sd)


    except Exception:
        messagebox.showerror('Error', 'Makesure You are connected to MySQL server.')


# ALL LABELS

L1 = Label(window, text='My Password Generator', fg='#1a0000', background='#999999', font='Candara 30 ', borderwidth=5,
           relief=RIDGE, padx=50)
L1.pack(anchor=CENTER, pady=8)
L2 = LabelFrame(window, text='', font='Candara 10', height=400, width=996, background='#C0C0C0', padx=4)  # input
L2.pack(anchor=CENTER, pady=5)
L3 = LabelFrame(window, text='', background='#C0C0C0', height=128, width=996)  # middle
L3.pack(anchor=CENTER, pady=5)
L4 = LabelFrame(window, text='', font='Candara 10', height=140, width=996, background='#C0C0C0')  # options
L4.pack(anchor=S, pady=5)
L5 = Label(L2, text='Enter Your Name Or Username  :', font='Candara 16', background='#C0C0C0')
L5.grid(row=0, column=0, padx=12, pady=10, sticky=W)
L6 = Label(L2, text='Enter The Name of App :', font='Candara 16', background='#C0C0C0')
L6.grid(row=1, column=0, padx=12, pady=10, sticky=W)
L7 = Label(L2, text='Enter The Length of Password :', font='Candara 16', background='#C0C0C0')
L7.grid(row=2, column=0, padx=12, pady=10, sticky=W)
L8 = Label(L2, text='Any Specific Word That Password Must Include :', font='Candara 16', background='#C0C0C0')
L8.grid(row=3, column=0, padx=12, pady=10, sticky=W)
L9 = Label(L2, text='Any Additional Information(*Optional) :', font='Candara 16', background='#C0C0C0')
L9.grid(row=4, column=0, padx=12, pady=10, sticky=W)
# ENTRY BOXES

E1 = Entry(L2, width=40, font='Candara, 16')  # your name
E1.grid(row=0, column=1, padx=20, pady=10)
E2 = Entry(L2, width=40, font='Candara, 16')  # name of app
E2.grid(row=1, column=1, padx=20, pady=10)
E3 = Entry(L2, width=40, font='none, 16')  # length
E3.grid(row=2, column=1, padx=20, pady=10)
E4 = Entry(L2, width=40, font='Candara, 16')  # word
E4.grid(row=3, column=1, padx=20, pady=10)
E5 = Entry(L2, width=40, font='Candara, 16')
E5.grid(row=4, column=1, padx=20, pady=10)
E6 = Text(L3, width=60, height=1, font='Candara 16')
E6.grid(row=1, columnspan=3, padx=40, pady=10)
E6.configure(state='disabled')

# ALL BUTTONS

B1 = Button(L4, text='See All Saved Passwords', height=3, width=30, relief=GROOVE, background='#999999',
            font='Candara 13 bold',
            command=showpass, borderwidth=3)
B1.grid(row=0, column=0, padx=26, pady=10)
B2 = Button(L4, text='Export Passwords To Excel', height=3, width=30, relief=GROOVE, background='#999999',
            font='Candara 13 bold', command=save_excel, borderwidth=3)
B2.grid(row=0, column=1, padx=24, pady=10)
B5 = Button(L4, text='Secure Your Password', height=3, width=30, relief=GROOVE, background='#999999',
            font='Candara 13 bold',
            command=secure, borderwidth=3)
B5.grid(row=0, column=2, padx=24, pady=10)
B3 = Button(L3, text='Generate Password', height=1, width=45, relief=GROOVE, background='#999999',
            font='Candara 13 bold',
            command=generate, borderwidth=3)
B3.grid(row=0, column=0, padx=40, pady=10)
B4 = Button(L3, text='Save Password', height=1, width=45, relief=GROOVE, background='#999999', font='Candara 13 bold',
            state=DISABLED, command=save_pass, borderwidth=3)
B4.grid(row=0, column=1, padx=40, pady=10)

window.iconbitmap('ico.ico')
mainloop()
