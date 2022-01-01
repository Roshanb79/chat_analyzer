import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
#methods
def top_10_most_used_word():
    global most_used_word
    dic=sorted(most_used_word.items(),key=lambda x:x[1],reverse=True)[:13]
    dic=dict(dic)
    del dic[""]
    del dic["<media"]
    del dic["omitted>"]
    return dic
    
def msgtiming():
    mng=plt.get_current_fig_manager()
    mng.window.state("zoomed")
    plt.bar(msg_time.keys(),msg_time.values())
    plt.show()
    
def nOM():
    global no_of_msg_specific
    mng=plt.get_current_fig_manager()
    mng.window.state("zoomed")
    no_of_msg_specific=dict(sorted(no_of_msg_specific.items(),key=lambda x:x[1],reverse=True)[:15])
    plt.barh(list(no_of_msg_specific.keys()),list(no_of_msg_specific.values()))
    plt.gca().invert_yaxis()
    plt.show()
    
def mUW():
    temp=top_10_most_used_word()
    mng=plt.get_current_fig_manager()
    mng.window.state("zoomed")
    plt.bar(temp.keys(),temp.values())
    plt.show()

#code
chat=[]
arrIndex=0
with open('chat.txt', 'r', encoding='utf8') as f:
    while True:
        try:
            line=f.readline()
            if not line:
                break
            Msg=True
            data=line.split(",", 1)
            date=data.pop(0)
            if date[2] != "/" and date[5] != "/" and date[10] != ",":
                raise IndexError
            data=data[0]
            data=data.split("-", 1)
            time=data.pop(0)
            data=data[0]
            if ":" not in data:
                continue
            data=data.split(":", 1)
            user=data[0]
            text=data[1]
            chat.append([date, time, user, text.replace("\n", "")])
            arrIndex+=1
        except IndexError:
                chat[-1][-1]=chat[-1][-1]+line.replace("\n", "")


arr=np.array(chat)
chat=[]
print("please wait...")

#working with data
list_of_users = []
msg_time={' 1pm': 0, ' 2pm': 0, ' 3pm': 0, ' 4pm': 0, ' 5pm': 0, ' 6pm': 0, ' 7pm': 0, ' 8pm': 0, ' 9pm': 0, ' 10pm': 0, ' 11pm': 0, ' 12pm': 0, ' 1am': 0, ' 2am': 0, ' 3am': 0, ' 4am': 0, ' 5am': 0, ' 6am': 0, ' 7am': 0, ' 8am': 0, ' 9am': 0, ' 10am': 0, ' 11am': 0, ' 12am': 0}
no_of_msg_specific={}
most_used_word={}

for a in arr:
    #list of users
    list_of_users.append(a[2])

    #active time
    listTime=a[1].split(":", 1)
    try:
        if 'pm' in listTime[1]:
            hour = listTime[0]+"pm"
        else:
            hour = listTime[0]+"am"
    except IndexError:
        print(a)
    try:
        msg_time[hour]+=1
    except KeyError:
        msg_time[hour]=1
        
    #msg by specific user
    try:
        no_of_msg_specific[a[2]]+=1
    except KeyError:
        no_of_msg_specific[a[2]]=1
        
    #most used word
    for word in a[3].split(" "):
        try:
            most_used_word[word.lower()]+=1
        except KeyError:
            most_used_word[word.lower()]=1

list_of_users=set(list_of_users)
list_of_users=list(list_of_users)
color_bg="#2F4858"
color_bg_2="#006572"
print("done")
root=tk.Tk()
root.geometry("1800x900")
root.title("Whatsapp Chat Analyzer")
root.configure(bg=color_bg)

#Labels
lOU=tk.Label(root,text="List of members",font=("Bitter",20),bg="#3E994C",fg="white")
i_lOM=tk.Label(root,bg=color_bg_2,text="Number Of Media: "+str(most_used_word["<media"]),font=("Arial",20,"bold"),fg="white")
i_lOT=tk.Label(root,bg=color_bg_2,text="Number Of Texts: "+str(len(arr)-most_used_word["<media"]),font=("Arial",20,"bold"),fg="white")
tM=tk.Label(root,text="Total Messages:"+str(len(arr)),font=("Bitter",20),bg="#3E994C",fg="white")

#Lists
names=tk.Listbox(root,font=("Bitter",15),background=color_bg_2,foreground="white")
for i in range(1,len(list_of_users)+1):
    names.insert(i,list_of_users[i-1])

#Buttons
b_mUW=tk.Button(root,text="Most Used Words",command=mUW,font=("Bitter",20),bg=color_bg_2,fg="white")
b_nOM=tk.Button(root,text="Top User",command=nOM,font=("Bitter",20),bg=color_bg_2,fg="white")
b_aT=tk.Button(root,text="Msg By Time",command=msgtiming,font=("Bitter",20),bg=color_bg_2,fg="white")

#ScroolBar
scrollbar=tk.Scrollbar(names,orient="vertical")

#placement
lOU.place(x=5, y=5, width=296-50, height=56)
names.place(x=52-50, y=160-100, width=507-50, height=700)
i_lOM.place(x=587-50, y=140-100, width=589-50, height=337-50)
i_lOT.place(x=587-50, y=603-200, width=589-50, height=337-50)
b_aT.place(x=1324-200, y=140-100, width=444-50, height=102)
b_mUW.place(x=1324-200, y=345-100, width=444-50, height=102)
b_nOM.place(x=1324-200, y=550-100, width=444-50, height=102)
tM.place(x=1324-200, y=840-200, width=422-50, height=62)
scrollbar.pack(side="right",fill="y")

root.mainloop()
arr=None
    

