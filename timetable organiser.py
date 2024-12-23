#__initials__

import random
import pickle
assigned=[]
d={'admin':'$ch00lT!m3t@6l3'}
reg=open("accounts.dat",'ab+')
try:
    while True:
        h=pickle.load(reg)
        if 'admin' in d.keys(): 
            print("WELCOME")
        
except EOFError:
    pickle.dump(d,reg)
    reg.close()

#__function_definitions__

def create_timetable(classes, periods):
    subjects=['English', 'Hindi', 'Maths', 'Science', 'Social_science', 'Computer']
    class_file=open("Student_timetable.txt", 'a+')
    for i in range(classes):
        x=[]
        a=input("Enter the name of the class")
        a=a+':'
        x.append(a)
        random.shuffle(subjects)
        jk=subjects+subjects
        h=jk[0:periods]
        for i in h:
            x.append(i)
        z=''
        for i in x:
            z+=i+' | '
        z=z+'\n'
        print(z)
        class_file.write(z)
        class_file.flush()
    class_file.close()
           
def display_classTT():
    class_file=open("Student_timetable.txt", 'r+')
    a=class_file.readlines()
    for i in a:
        print(i)
    class_file.close()
    
def create_teacherTT():
    import pickle
    test=[]
    teacher_file=open("Teacher's_timetable.dat", 'wb+')
    for m in range(6):
        assigned=[]
        sub=input("Enter subject")
        assigned.append(sub)
        sub=sub.capitalize()
        print("Teacher required per subject must be 4")
        no=4
        
        for j in range(no):
            schedule={}
            copy_schedule={}
            w=input("Enter teacher's name")
            schedule['name']=w
            schedule['subject']=sub
            class_file=open("Student_timetable.txt", 'r+')
            a=class_file.readlines()
            p={}
            
            for i in a:
                i=i.split()
                for op in range(len(i)//2):
                    if '|' in i:
                        i.remove('|')
                x=i.index(sub)
                p[i[0]]=x
            c=[];key=[]
            
            for (k,v) in p.items():
                if v not in c and k not in assigned:
                    c.append(v)
                    key.append(k)
                    assigned.append(k)
            for kh in range(len(c)):
                schedule[c[kh]]=key[kh]
                copy_schedule[c[kh]]=key[kh]
                
            if len(schedule)>3:
                t=list(schedule.values())
                size=len(schedule)-5
                for seq in range(size):
                    s=t.pop()
                    assigned.remove(s)
                    for k,v in copy_schedule.items():
                        if v==s:
                            del schedule[k]
            print(schedule)
            test.append(schedule)
            pickle.dump(schedule,teacher_file)
            teacher_file.flush()
        teacher_file.flush()
    teacher_file.close()
    class_file.close()

def display_teacherTT():
    import pickle
    teacher_file=open("Teacher's_timetable.dat",'rb')
    try:
        while True:
            a=pickle.load(teacher_file)
            print(a)
    except EOFError:
        print("\n All the data has been fetched out of the file")
    
def create_subsfile():
    print("5 teachers must  be made available only for substitution")
    fh=open('substitution_teachers.txt','w+')
    for i in range(5):
        a=input("Enter teacher name")
        a=a+'\n'
        fh.write(a)
        fh.flush()
    fh.close()
    print("data inserted")   

def set_substitution(name):
    global assigned
    import pickle
    teacher_file=open("Teacher's_timetable.dat",'rb')
    subs_file=open('substitution_teachers.txt','r+')
    subs_teacher=subs_file.readlines()
    try:
        while True:
            a=pickle.load(teacher_file)
            if type(a) is dict:
                if a['name']==name:
                    x=list(a.items())
                    x=x[2:]
    except EOFError:
        print("file termination")
    teacher_file.close()
    print(x)
    k=''
    random.shuffle(subs_teacher)
    for i in subs_teacher:
        if i not in assigned:
            k=i
    assigned.append(k)
    print(assigned)
    for i in x:
        print(i, 'assigned to', k)
        
def clear_substitution():
    global assigned
    assigned.clear()
    print(assigned)
    print("Data cleared for the day")

def register_user(username,password):
    global d
    import pickle
    reg=open("accounts.dat",'ab+')
    d[username]=password
    pickle.dump(d,reg)

    
#__main__

reg=open("accounts.dat",'rb+')
d=pickle.load(reg)
l=list(d.keys())
username=input("enter username")
password=input("enter password")


if username not in l:
    print("INVALID USERNAME")
else:
    
    if d[username]==password:
        print("You are logged in")
        s='y'
        print("___MENU___\n\
1. register user\n\
2. create classwise timetable\n\
3. display classwise tietable\n\
4. generate teacher's timetable\n\
5. display teacher's timetable\n\
6. create file of substitution\n\
7. set substitution\n\
8. clear substitutions\n")

        while s=='y':
            a=int(input("enter choice in no without period '.' "))
            if  a==1:
                if username=='admin':
                    h=int(input("How many users are to be registered?"))
                    for i in range(h):
                        user=input("enter username")
                        passw=input("enter password")
                        register_user(user,passw)
                else:
                    print("Sorry, only admin can register any new users")
                    
            elif a==2:
                classes=int(input("Enter no of classes whose timetable is to be recorded"))
                periods=int(input("Enter no of periods that will be held in a day"))
                create_timetable(classes, periods)
                
            elif a==3:
                display_classTT()
                
            elif a==4:
                create_teacherTT()
                
            elif a==5:
                display_teacherTT()
                
            elif a==6:
                create_subsfile()
                
            elif a==7:
                x=int(input("How many teachers sre absent?"))
                for i in range(x):
                    name=input("Enter name")
                    set_substitution(name)
                    
            elif a==8:
                clear_substitution()
                
            else:
                print("Invalid choice")
            s=input("anything else to be done? y/n?")

            
    else:
            print("Incorrect password")
                
                
                
                
                
                

                
