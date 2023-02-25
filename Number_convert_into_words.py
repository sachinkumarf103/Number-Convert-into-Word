from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Converter - Number Into Words")
root.geometry("1000x500+250+100")
root.resizable(0,0)
#*********************************************************
word_lst = {0:"Zero" , 1:"One" , 2:"Two" , 3:"Three" , 4:"Four" , 5:"Five" , 6:"Six" , 7:"Seven" , 8:"Eight" , 9:"Nine" , 10:"Ten" , 11:"Eleven" , 12:"Twelve" , 13:"Thirteen", 14:"Fourteen" , 15:"Fifteen" , 16:"Sixteen" , 17:"Seventeen" , 18:"Eighteen" , 19:"Nineteen" , 20:"Twenty" , 30:"Thirty" , 40:"Fourty" , 50:"Fifty" , 60:"Sixty" , 70:"Seventy" , 80:"Eighty" , 90:"Ninty" , 100:"Hundred" , 1000:"Thousand" , 100000:"Lacs" , 10000000:"Crores"}



def res():
    wrd = ""            #for store words
    num = int(usr_ent.get())
    tmp_num = num
    if num<=999999999:
        while tmp_num != 0:

            # For Unit
            if tmp_num>=1 and tmp_num<=9:
                wrd += word_lst[tmp_num]
                tmp_num = int(tmp_num/10)

            # Fpr Ten
            elif tmp_num>=10 and tmp_num<=99:
                a = int(tmp_num/10)
                b = a*10
                wrd += word_lst[b] + " "
                tmp_num = tmp_num % 10
                if tmp_num !=0:
                    wrd += word_lst[tmp_num] + " "
                tmp_num = int(tmp_num/10)

            # For Hundred
            elif tmp_num>=100 and tmp_num<=999:
                a = int(tmp_num/100)
                wrd += word_lst[a] +" "+word_lst[100] + " "
                tmp_num = tmp_num%100

            # For Thousand and Ten Thousand
            elif tmp_num>=1000 and tmp_num<=99999:
                a = int(tmp_num/1000)
                if a>=21 and a%10 !=0:
                    b = int(a/10)    
                    c = b*10                #if a is greater than or equl to 21 and a reminder not equl to zero and for convert into ten
                    wrd += word_lst[c] + " "
                    d = a%10
                    wrd += word_lst[d] + " " + word_lst[1000] + " "
                else:
                    wrd += word_lst[a] + " " + word_lst[1000] + " "
                tmp_num = tmp_num%1000

            # For Lac and Ten Lac
            elif tmp_num>=100000 and tmp_num<=9999999:
                a = int(tmp_num/100000)
                if a>=21 and a%10 !=0:
                    b = int(a/10)    
                    c = b*10                #if a is greater than or equl to 21 and a reminder not equl to zero and for convert into ten
                    wrd += word_lst[c] + " "
                    d = a%10
                    wrd += word_lst[d] + " " + word_lst[100000] + " "
                else:
                    wrd += word_lst[a] + " " + word_lst[100000] + " "
                tmp_num = tmp_num%100000

            # For Crores and Ten Crores
            elif tmp_num>=10000000 and tmp_num<=999999999:
                a = int(tmp_num/10000000)
                if a>=21 and a%10 !=0:
                    b = int(a/10)    
                    c = b*10                #if a is greater than or equl to 21 and a reminder not equl to zero and for convert into ten
                    wrd += word_lst[c] + " "
                    d = a%10
                    wrd += word_lst[d] + " " + word_lst[10000000] + " "
                else:
                    wrd += word_lst[a] + " " + word_lst[10000000] + " "
                tmp_num = tmp_num%10000000
                
        #print(wrd)
        show_lbl.config(text=wrd)
    else:
        messagebox.showerror("Converter" , "You Corss the Limit....! You enter Only 9 Digit")
        #print("You cross the limit..... Sorry!")

        


#**********************************************************
hed_frm = Frame(root, bg="red")
hed_frm.pack(ipadx=2,ipady=1)
hed_lbl = Label(hed_frm, text="Converter", font=("Provicali", 40), underline=4)
hed_lbl.pack()

mid_frm = Frame(root,)
mid_frm.pack(pady=30)

ur_lbe = Label(mid_frm, text="Enter the Number", font=("Times New Roman", 35))
ur_lbe.pack()

usr_ent = Entry(mid_frm, width=12, font=("Times New Roman", 25), justify=CENTER)
usr_ent.pack(ipady=5)

btn = Button(mid_frm, text="Convert", font=("Times New Roman", 20), relief="groove", command=res)
btn.pack(pady=10)

# res_frm = Frame(root, width=100, height=100, bg="red")
# res_frm.pack(ipadx=40)

show_lbl = Label(root, text="Resutl", fg="Green", font=("Times New Roman", 20), )
show_lbl.pack()

#Notification
end_lbl = Label(root, text="@SAM", bg="lightblue")
end_lbl.pack(side=BOTTOM, fill=X, ipady=5)
not_lbl = Label(root, text="Note : You can enter 9 Digits Only So, Be your limit Okay")
not_lbl.pack(side=BOTTOM)

root.mainloop()