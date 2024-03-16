from tkinter import *
from tkinter import ttk
from winsound import *
from pygame import mixer
from gtts import gTTS
from PIL import Image, ImageTk
from tkinter import messagebox
from fpdf import FPDF
#import tkinter as tk
import numpy as np
import pandas as pd
import os
import mysql.connector
import datetime
import random
import string
import smtplib
import fpdf
import webbrowser


global dd, l1, p_mail, p_mailen, OPTIONS, Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, root, c, mycursor, dda, entry_1, entry_2, entry_3, entry_4, counter, counter1, new, dr_username, nameentry, ageentry, phentry
counter = 0
counter1 = 0
dd = datetime.datetime.now().strftime("%d-%m-%Y")
dda = datetime.datetime.now().strftime("%Y%m%d")



root = Tk()




#database connection-------------------------------------------------------------------------------------------- 
mydb = mysql.connector.connect(

    host = 'remotemysql.com',
    port = 3306,
    user = 'ITTX8hHZms',
    passwd = 'vXmZXfTU5Z',
    db = 'ITTX8hHZms'
)


mycursor = mydb.cursor()

data = mycursor.fetchone()
print ("Database version : %s " % data)

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)




# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr ---------------------------------------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)


# decision tree --------------------------------------------------------------------------------------------------------------------

def DecisionTree():

    global d1, t1
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    

    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])

        tts = gTTS(text="The patient may be suffering from" + disease[a], lang='en-au')
        tts.save("pcvoice.mp3")
        # to start the file from python
        mixer.init()
        mixer.music.load('pcvoice.mp3')
        mixer.music.play()
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
        tts = gTTS(text="Please recheck the symptoms", lang='en-au')
        tts.save("pcvoice.mp3")
        # to start the file from python
        mixer.init()
        mixer.music.load('pcvoice.mp3')
        mixer.music.play()

    d1 = disease[a]
    print(d1)



# random forest --------------------------------------------------------------------------------------
def randomforest():
    global d2, t2

    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
        tts = gTTS(text="The patient may be suffering from" + disease[a], lang='en-au')
        tts.save("pcvoice1.mp3")
        # to start the file from python
        mixer.init()
        mixer.music.load('pcvoice1.mp3')
        mixer.music.play()
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")
        tts = gTTS(text="please recheck the symptoms", lang='en-au')
        tts.save("pcvoice1.mp3")
        # to start the file from python
        mixer.init()
        mixer.music.load('pcvoice1.mp3')
        mixer.music.play()

    d2 = disease[a]




#navie bayes ------------------------------------------------------------------------------------
def NaiveBayes():
    global d3, t3
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
        tts = gTTS(text="The patient may be suffering from" + disease[a], lang='en-au')
        tts.save("pcvoice3.mp3")
        # to start the file from python
        mixer.init()
        mixer.music.load('pcvoice3.mp3')
        mixer.music.play()
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")
        tts = gTTS(text="please recheck the symptoms", lang='en-au')
        tts.save("pcvoice3.mp3")
        # to start the file from python
        mixer.init()
        mixer.music.load('pcvoice3.mp3')
        mixer.music.play()

    d3 = disease[a]

#GUI_FUNCTIONS--------------------------------------------------

#to check the registration of the patient---------------------------------------------------



   

#submit button ----------
#splashscreeen start----------------------------------------------------------
class DemoSplashScreen:
    global root
    def __init__(self, parent):
        self.parent = parent
        self.Splash()
        self.Window()

    def Splash(self):
        self.openimage = Image.open('logo_complete.jpg')
        self.imgSplash = ImageTk.PhotoImage(self.openimage)


    def Window(self):
        # ambil ukuran dari file image
        length, width = self.openimage.size
 
        winLen = (self.parent.winfo_screenwidth()-length)//2
        winwidth = (self.parent.winfo_screenheight()-width)//2
 
        # atur posisi window di tengah-tengah layar
        self.parent.geometry("%ix%i+%i+%i" %(length, width,
                                             winLen,winwidth))
 
        # atur Image via Komponen Label
        Label(self.parent, image=self.imgSplash).pack()

def submitold():

    global aadharentry, x_symptoms, x_disease, patient_disease, patient_symptoms

    patient_symptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    patient_disease = [d2,d1,d3]
    x_symptoms = ",".join(patient_symptoms)
    x_disease = ",".join(patient_disease)
    print(patient_symptoms)
    print(patient_disease)

    mycursor.execute('INSERT INTO entry (aadhar_card, symptoms, disease, visited_date) VALUES (%s ,%s ,%s ,%s)',(aadharentry, x_symptoms, x_disease, dda))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    messagebox.askokcancel("SUBMIT", "PATIENT'S SYMPTOMS AND DETECTED DISEASE SUCCESSFULLY SAVED")

def newpatient():
    new.destroy()
    main()
    

def close():
    mydb.close()
    new.destroy()


def header():
    global pr_drn
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',14)
    pdf.cell(10,10,'WELCOME TO DOCTOR %s CLINIC'%pr_drn)

def print_pdf():

    global pr_drn 

    pr_drn = dr_name
    di1 = d1
    di2 = d2
    di3 = d3
    si1 = Symptom1.get()
    si2 = Symptom2.get()
    si3 = Symptom3.get()
    si4 = Symptom4.get()
    si5 = Symptom5.get()

    p_name = nameentry
    p_age = ageentry
    p_ph = phentry

    mycursor.execute("SELECT M_NAME FROM `Medicine` WHERE D_ID IN (SELECT D_ID FROM disease WHERE D_NAME = '%s')" %di1)
    med1 = mycursor.fetchall()

    mycursor.execute("SELECT M_NAME FROM `Medicine` WHERE D_ID IN (SELECT D_ID FROM disease WHERE D_NAME = '%s')" %di2)
    med2 = mycursor.fetchall()

    mycursor.execute("SELECT M_NAME FROM `Medicine` WHERE D_ID IN (SELECT D_ID FROM disease WHERE D_NAME = '%s')" %di3)
    med3 = mycursor.fetchall()

    print(med1)
    print(med2)
    print(med3)

    mycursor.execute("SELECT T_NAME FROM `pathology` WHERE D_ID IN (SELECT D_ID FROM disease WHERE D_NAME = '%s')" %di1)
    patho1 = mycursor.fetchall()

    mycursor.execute("SELECT T_NAME FROM `pathology` WHERE D_ID IN (SELECT D_ID FROM disease WHERE D_NAME = '%s')" %di2)
    patho2 = mycursor.fetchall()

    mycursor.execute("SELECT T_NAME FROM `pathology` WHERE D_ID IN (SELECT D_ID FROM disease WHERE D_NAME = '%s')" %di3)
    patho3 = mycursor.fetchall()

    pdf=FPDF('P','mm',(210,350))
    pdf.add_page(orientation = 'P')
    header()
    #pdf.set_auto_page_break(auto=bool, margin = 0.0)
    pdf.set_font("Arial", '',size=12)
    pdf.cell(10,30,"DOCTOR NAME: %s"%pr_drn)
    pdf.ln(0)
    pdf.cell(10,50,"PATIENT NAME: %s"%p_name)
    pdf.ln(0)
    pdf.cell(10,70,"PATIENT AGE: %s"%p_age)
    pdf.ln(0)
    pdf.cell(10,90,"PATIENT NUMBER: %s"%p_ph)
    pdf.ln(0)
    pdf.cell(10,110,"SYMPTOMS DETECTED")
    pdf.ln(0)
    pdf.cell(10,130,'1. %s'%si1)
    pdf.ln(0)
    pdf.cell(10,140,'2. %s'%si2)
    pdf.ln(0)
    pdf.cell(10,150,'3. %s'%si3)
    pdf.ln(0)
    pdf.cell(10,160,'4. %s'%si4)
    pdf.ln(0)
    pdf.cell(10,170,'5. %s'%si5)
    pdf.ln(0)
    pdf.cell(10,190, 'DISEASE DETECTED')
    pdf.ln(0)
    pdf.cell(10,210,'1. %s'%di1)
    pdf.ln(0)
    pdf.cell(10,220,'2. %s'%di2)
    pdf.ln(0)
    pdf.cell(10,230,'3. %s'%di3)
    pdf.ln(0)
    pdf.add_page(orientation = 'P')
    pdf.cell(10,30,'MEDICINE SUGGESTION FOR DISEASE 1')
    pdf.ln(0)
    j=50
    for i in med1:
        pdf.cell(10,j,str(i))
        j = j + 10
        pdf.ln(0)
    
    j = j + 20
    pdf.cell(10,j,'MEDICINE SUGGESTION FOR DISEASE 2')
    pdf.ln(0)
    j = j + 20
    for i in med2:
        pdf.cell(10,j,str(i))
        j = j + 10
        pdf.ln(0)
    
    j = j + 20
    pdf.cell(10,j,'MEDICINE SUGGESTION FOR DISEASE 3')
    pdf.ln(0)
    j = j + 20
    for i in med3:
        pdf.cell(10,j,str(i))
        j = j + 10
        pdf.ln(0)

    pdf.add_page(orientation = 'P')
    j = 30
    pdf.cell(10,j,'PATHOLOGY TEST SUGGESTION FOR DISEASE 1')
    pdf.ln(0)
    j = j + 20
    for i in patho1:
        pdf.cell(10,j,str(i))
        j = j + 10
        pdf.ln(0)

    j = j + 20
    pdf.cell(10,j,'PATHOLOGY TEST SUGGESTION FOR DISEASE 2')
    pdf.ln(0)
    j = j +20
    for i in patho2:
        pdf.cell(10,j,str(i))
        j = j + 10
        pdf.ln(0)

    j = j + 20
    pdf.cell(10,j,'PATHOLOGY TEST SUGGESTION FOR DISEASE 3')
    pdf.ln(0)
    j = j + 20
    for i in patho3:
        pdf.cell(10,j,str(i))
        j = j + 10
        pdf.ln(0)

    pdf.output('%s.pdf'%p_name,'F')
    webbrowser.open('%s.pdf'%p_name)

    

def newsymptoms():
    global t1, t2, t3, new, aadharen, NameEn, Ageen, ph_noen, Symptom1, Symptom2, Symptom3, Symptom4, Symptom5, counter1, S1En, S2En, S3En, S4En, S5En


    #popup.destroy()
    root.destroy()
    counter1=1
    new = Toplevel()
    new.wm_state('zoomed')

    Symptom1 = StringVar()
    Symptom1.set('Select Symptom 1')
    Symptom2 = StringVar()
    Symptom2.set('Select Symptom 2')
    Symptom3 = StringVar()
    Symptom3.set('Select Symptom 3')
    Symptom4 = StringVar()
    Symptom4.set('Select Symptom 4')
    Symptom5 = StringVar()
    Symptom5.set('Select Symptom 5')
    new.iconbitmap('logo.ico')
    new.title("Smart Assistant For Doctors")
    new.iconbitmap('logo.ico')
    new.configure(background='light blue')

    # entry variables


   

    # Heading
    w2 = Label(new, justify=LEFT, text="Smart Assistant For Doctors", fg="black", bg="light blue")
    w2.config(font=("Elephant", 30))
    w2.grid(row=1, column=0, columnspan=2, padx=100)
    w2 = Label(new, justify=LEFT, text="Rajiv Gandhi Institute Of Technology ", fg="black", bg="light blue")
    w2.config(font=("Aharoni", 30))
    w2.grid(row=2, column=0, columnspan=2, padx=100)

    #w3 = Label(root, justify=LEFT, text="DR %s"%(entry_1.get()), fg="black", bg="light blue")
    #w3.config(font=("Aharoni", 20))
    #w3.grid(row=4, column=0, columnspan=2, padx=100)


    #w4 = Label(root, justify=LEFT, text="Degree %s"%(droplist.get()), fg="black", bg="light blue")
    #w4.config(font=("Aharoni", 20))
    #w4.grid(row=4, column=1, columnspan=2, padx=100)

    #w4 = Label(root, justify=LEFT, text="Date %s"%(dd), fg="black", bg="light blue")
    #w4.config(font=("Aharoni", 20))
    #w4.grid(row=4, column=3, columnspan=2, padx=100)

    # labels
    NameLb = Label(new, text="Name of the Patient", fg="yellow", bg="black")
    NameLb.grid(row=6, column=0, pady=15, sticky=W)

    AgeLb = Label(new, text="AGE", fg="yellow", bg="black")
    AgeLb.grid(row=7, column=0, pady=15, sticky=W)

    ph_no = Label(new, text="Phone Number", fg="yellow", bg="black")
    ph_no.grid(row=8, column=0, pady=15, sticky=W)

    aadhar = Label(new, text="AADHAR Card No.", fg="yellow", bg="black")
    aadhar.grid(row=9, column=0, pady=15, sticky=W)

    S1Lb = Label(new, text="Symptom 1", fg="yellow", bg="black")
    S1Lb.grid(row=10, column=0, pady=10, sticky=W)

    S2Lb = Label(new, text="Symptom 2", fg="yellow", bg="black")
    S2Lb.grid(row=11, column=0, pady=10, sticky=W)

    S3Lb = Label(new, text="Symptom 3", fg="yellow", bg="black")
    S3Lb.grid(row=12, column=0, pady=10, sticky=W)

    S4Lb = Label(new, text="Symptom 4", fg="yellow", bg="black")
    S4Lb.grid(row=13, column=0, pady=10, sticky=W)

    S5Lb = Label(new, text="Symptom 5", fg="yellow", bg="black")
    S5Lb.grid(row=14, column=0, pady=10, sticky=W)


    lrLb = Label(new, text="Disease 1", fg="white", bg="red")
    lrLb.grid(row=18, column=0, pady=10,sticky=W)

    destreeLb = Label(new, text="Disease 2", fg="white", bg="red")
    destreeLb.grid(row=19, column=0, pady=10, sticky=W)

    ranfLb = Label(new, text="Disease 3", fg="white", bg="red")
    ranfLb.grid(row=20, column=0, pady=10, sticky=W)

    # entries
    
    Name = Label(new, text=nameentry, fg="black")
    Name.grid(row=6, column=1, pady=10, sticky=W)


    Age = Label(new, text=ageentry, fg="black")
    Age.grid(row=7, column=1, pady=10, sticky=W)

    ph_nol = Label(new, text=phentry, fg="black")
    ph_nol.grid(row=8, column=1, pady=10, sticky=W)

    aadhar = Label(new, text=aadharentry, fg="black")
    aadhar.grid(row=9, column=1, pady=10, sticky=W)



    OPTIONS = sorted(l1)

    #print(OPTIONS)


    S1En = OptionMenu(new, Symptom1, *OPTIONS)
    S1En.grid(row=10, column=1)

    S2En = OptionMenu(new, Symptom2, *OPTIONS)
    S2En.grid(row=11, column=1)

    S3En = OptionMenu(new, Symptom3, *OPTIONS)
    S3En.grid(row=12, column=1)

    S4En = OptionMenu(new, Symptom4, *OPTIONS)
    S4En.grid(row=13, column=1)

    S5En = OptionMenu(new, Symptom5, *OPTIONS)
    S5En.grid(row=14, column=1)



    dst = Button(new, text="Disease 1", command=DecisionTree,bg="green",fg="yellow")
    dst.grid(row=8, column=3,padx=10)
    
    rnf = Button(new, text="Disease 2", command=randomforest,bg="green",fg="yellow")
    rnf.grid(row=9, column=3,padx=10)

    lr = Button(new, text="Disease 3", command=NaiveBayes,bg="green",fg="yellow")
    lr.grid(row=10, column=3,padx=10)

    submit = Button(new, text="SUBMIT", command=submitold,bg="green",fg="yellow")
    submit.grid(row=19, column=3,padx=10)

    printit = Button(new, text="PRINT", command=print_pdf,bg="green",fg="yellow")
    printit.grid(row=20, column=3,padx=10)

    exit = Button(new, text="EXIT", command=close ,bg='brown',fg='white')
    exit.grid(row=21, column=3,padx=10)

    new_patient = Button(new, text="NEW PATIENT", command=newpatient ,bg='brown',fg='white')
    new_patient.grid(row=23, column=3,padx=10)
    #textfileds
    t1 = Text(new, height=1, width=40,bg="white",fg="black")
    t1.grid(row=18, column=1, padx=10)

    t2 = Text(new, height=1, width=40,bg="white",fg="black")
    t2.grid(row=19, column=1 , padx=10)

    t3 = Text(new, height=1, width=40,bg="white",fg="black")
    t3.grid(row=20, column=1 , padx=10)

    tts = gTTS(text="Please enter the symptoms of the patient", lang='en-au')
    tts.save("intro2.mp3")
    mixer.init()
    mixer.music.load('intro2.mp3')
    mixer.music.play()
    new.mainloop()

def already_patient():
    ans = messagebox.askokcancel("ALREADY EXIST", "PATIENT ALREADY EXIST")
    if (ans == True):
        newsymptoms()
    

def new_patient():
    a = messagebox.askokcancel("SUCCESSFULL", "PATIENT SUCCESSFULLY REGISTERED")
    if (a == True):
        newsymptoms()
    else:
        aa = messagebox.askyesno("ALERT", "DO YOU WANT TO EXIT")
        if (aa == True):
            root.destroy()




#-------------------------------------------------------
def patient_check():
    global nameentry, ageentry, phentry, aadharentry, popup, emailentry, p_mailen, dr_name, drqua, dr_username, username_login_entry, xi
    
    nameentry = NameEn.get()
    ageentry = Ageen.get()
    phentry = ph_noen.get()
    aadharentry = aadharen.get()
    emailentry = p_mailen.get()
    dr_username = xi

    mycursor.execute("SELECT doc_name FROM doctor WHERE doc_user = '%s'" %dr_username)
    dname = mycursor.fetchone()
    dr_name = dname[0]
    mycursor.execute("SELECT doc_quali FROM doctor WHERE doc_user = '%s'" %dr_username)
    drqua = mycursor.fetchone()
    dr_qua = drqua[0]
    print(drqua)
    print(emailentry)
    try:
        
        mycursor.execute('INSERT INTO patient (name, Age, phone_number, aadhar_card, patient_email, doc_name, doc_quali, visit_date) VALUES (%s ,%s ,%s ,%s ,%s, %s, %s, %s)',(nameentry, ageentry, phentry, aadharentry, emailentry, dr_name, dr_qua, dda))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        tts = gTTS(text="PATIENT SUCCESSFULLY REGISTERED", lang='en-au')
        tts.save("pop1.mp3")
        mixer.init()
        mixer.music.load('pop1.mp3')
        mixer.music.play()
       
        
        

        mail = smtplib.SMTP('smtp.gmail.com:587')
        msg = "WELCOME TO AI HEALTHCARE SYSTEM BY TIMBA INC. THANK YOU FOR VISITNG DR. %s (%s)"%(dr_name,dr_qua)
        mail.starttls()
        mail.login('kushhingol123@gmail.com','kushhingol@1')
        receiver = emailentry
        sender = "kushhingol123@gmail.com"
        mail.sendmail(sender, receiver, msg)
        mail.close()
        new_patient()
        #popup.mainloop()


    except:
        
        tts = gTTS(text="patient already exist", lang='en-au')
        tts.save("popup.mp3")
        mixer.init()
        mixer.music.load('popup.mp3')
        mixer.music.play()
        already_patient()
        
        

def main():
    
    global root, NameEn, Ageen, ph_noen, aadharen, progressbar, app, p_mailen, entry_1, c, display_name, degree_name, l1, p_mail
    Name = StringVar()
    number = IntVar()
    email = StringVar()
    ph = IntVar()
    aa = IntVar()
    root = Tk()

    root.wm_state('zoomed')


    if(counter1==0):
        login_screen.destroy()
    
    dr_user = xi
    mycursor.execute("SELECT doc_name FROM doctor WHERE doc_user = '%s'" %dr_user)
    drname = mycursor.fetchone()
    nameofdr = drname[0]
 


    root.title("Smart Assistant For Doctors")
    root.iconbitmap('logo.ico')
    root.configure(background='light blue')

    # Heading
    w2 = Label(root, justify=LEFT, text="Smart Assistant For Doctors", fg="black", bg="light blue")
    w2.config(font=("Elephant", 30))
    w2.grid(row=1, column=0, columnspan=2, padx=100)
    w2 = Label(root, justify=LEFT, text="Rajiv Gandhi Institute Of Technology ", fg="black", bg="light blue")
    w2.config(font=("Aharoni", 30))
    w2.grid(row=2, column=0, columnspan=2, padx=100)

    w3 = Label(root, justify=LEFT, text="DR %s"%(nameofdr), fg="black", bg="light blue")
    w3.config(font=("Aharoni", 20))
    w3.grid(row=4, column=0, columnspan=2, padx=100)


    #w4 = Label(root, justify=LEFT, text="Degree %s"%(degree_name), fg="black", bg="light blue")
    #w4.config(font=("Aharoni", 20))
    #w4.grid(row=4, column=1, columnspan=2, padx=100)

    w5 = Label(root, justify=LEFT, text="Date %s"%(dd), fg="black", bg="light blue")
    w5.config(font=("Aharoni", 20))
    w5.grid(row=4, column=3, columnspan=2, padx=100)

    # labels
    NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
    NameLb.grid(row=6, column=0, pady=15, sticky=W)

    AgeLb = Label(root, text="AGE", fg="yellow", bg="black")
    AgeLb.grid(row=7, column=0, pady=15, sticky=W)

    ph_no = Label(root, text="Phone Number", fg="yellow", bg="black")
    ph_no.grid(row=8, column=0, pady=15, sticky=W)

    aadhar = Label(root, text="AADHAR Card No.", fg="yellow", bg="black")
    aadhar.grid(row=9, column=0, pady=15, sticky=W)

    p_mail = Label(root, text="Email ID", fg="yellow", bg="black")
    p_mail.grid(row=10, column=0, pady=15, sticky=W)


# entries
    #OPTIONS = sorted(l1)

    NameEn = Entry(root, textvariable=Name)
    NameEn.grid(row=6, column=1)

    Ageen = Entry(root, textvariable=number)
    Ageen.grid(row=7, column=1)

    ph_noen = Entry(root, textvariable=ph)
    ph_noen.grid(row=8, column=1)

    aadharen = Entry(root, textvariable=aa)
    aadharen.grid(row=9, column=1)

    p_mailen = Entry(root, textvariable=email)
    p_mailen.grid(row=10, column=1)

    check = Button(root, text="CHECK", command=patient_check,bg='brown',fg='white',width="20")
    check.grid(row=8, column=2,padx=10)

    quit = Button(root, text="EXIT", command=root.destroy ,bg='brown',fg='white',width="20")
    quit.grid(row=9, column=2,padx=10)

    tts = gTTS(text="welcome to Smart assistant for Doctors. Please enter the patient details", lang='en-au')
    tts.save("intro.mp3")
    mixer.init()
    mixer.music.load('intro.mp3')
    mixer.music.play()

    root.mainloop()

#login and registration window--------------------------------------------------------------------------
def login_registration():
    
    global main_screen
    main_screen = Tk()   # create a GUI window 
    main_screen.iconbitmap('logo.ico')
     # set the configuration of GUI window 
     # set the title of GUI window

    width = 400
    height = 280
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    main_screen.title("Account Login")
# create a Form label 
    Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13))
 
# create Login Button 
    login = Button(main_screen,text="Login", height="2", width="30",bg='brown',fg='white', command = login_func).grid(row=40, column=50, padx=100, pady=30)
    #login.grid(row=10, column=10,padx=30)

# create a register button
    register = Button(main_screen,text="Register", height="2", width="30",bg='brown',fg='white', command = doctor_registration).grid(row=60, column=50, padx=100, pady=30) 
    #register.grid(row=50, column=10,padx=30)
    main_screen.mainloop() # start the GUI

def doctor_login():
    global login_screen, username_login_entry, password_login_entry, pop_reg

    #pop_reg.destroy()
    #registration_screen.destroy()
    if(counter==1):
        main_screen.destroy()

    login_screen = Tk()
    login_screen.iconbitmap('logo.ico')
    
    login_screen.geometry('500x500')
    login_screen.title("Login")
    
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
   
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()

    b = Button(login_screen, text="Login", width=20,bg='brown',fg='white', command=login_verification)
    b.pack()
    c = Button(login_screen, text="Back", width=20,bg='brown',fg='white', command=back_login).place(x=180,y=280)
    login_screen.mainloop()

def login_func():

    main_screen.destroy()
    doctor_login()

def login_verification():

    global username_login_entry, password_login_entry, login_screen, xi
    xi = username_login_entry.get()
    yi = password_login_entry.get()
    if username_login_entry.get() == "" or password_login_entry.get() == "":
        Label(login_screen,text="Please complete the required field!", fg="red").place(x=240,y=280)
    else:
        mycursor.execute("SELECT * FROM `doctor` WHERE `doc_user` = %s AND `doc_pass` = %s", (xi, yi))
        if mycursor.fetchone() is not None:
            main()
            username_login_entry.set()
            password_login_entry.set()
            lbl_text.config(text="")
        else:
            Label(login_screen,text="Invalid username or password", fg="red").place(x=240,y=280)
            username_login_entry.set(" ")
            password_login_entry.set(" ") 


def randomString(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
   


def back_reg():
    registration_screen.destroy()
    login_registration()

def back_login():
    login_screen.destroy()
    login_registration()

def success_reg():
    answer = messagebox.askokcancel("SUCCESSFULL", "SUCCESSFULLY REGISTERED!!! PLEASE CHECK YOUR EMAIL FOR USERNAME AND PASSWORD")
    if (answer == True):
        registration_screen.destroy()
        doctor_login()

def already_doc():
    answ = messagebox.askokcancel("NOTICE", "DOCTOR ALREADY REGISTERED")
    if (answ == True):
        registration_screen.destroy()
        doctor_login()


def registration_verification():
    global fullname_en, email_en, quali_en, address_en, paswd, entry_2, entry_1, entry_3, entry_4, pop_reg, B5, B4, mycursor
    #pop_reg = Tk()
    fullname_en = entry_1.get()
    email_en = entry_2.get()
    print(email_en)
    quali_en = c.get()
    print(quali_en)
    address_en = entry_3.get()
    phone_en = entry_4.get()
    try:
        user = randomString()
        paswd = randomString()
        mycursor.execute('INSERT INTO doctor (doc_name, doc_email, doc_quali, doc_address, doc_phone, doc_user, doc_pass) VALUES (%s ,%s ,%s ,%s ,%s, %s, %s)',(fullname_en, email_en, quali_en, address_en, phone_en, user, paswd))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mail = smtplib.SMTP('smtp.gmail.com:587')
        x = user
        y = paswd
        msg = "WELCOME TO AI HEALTHCARE SYSTEM BY TIMBA INC. DR. %s your username %s & password %s . PLEASE MAIL US YOUR DOCUMENTS."%(fullname_en,x,y)
        mail.ehlo()
        mail.starttls()
        mail.login('kushhingol123@gmail.com','kushhingol@1')
        receiver = email_en
        sender = "kushhingol123@gmail.com"
        mail.sendmail(sender, receiver, msg)
        mail.close()
        success_reg()
        

    except:
        
        already_doc()
        tts = gTTS(text="Doctor already exist", lang='en-au')
        tts.save("pop_reg1.mp3")
        mixer.init()
        mixer.music.load('pop_reg1.mp3')
        mixer.music.play()
        

   



def doctor_registration():
    global registration_screen, entry_1, entry_2, entry_3, entry_4, c
    main_screen.destroy()

    counter = 1
    
    registration_screen = Tk()
    registration_screen.iconbitmap('logo.ico')
    registration_screen.geometry('600x600')
    registration_screen.title("Registration Form")

    label_0 = Label(registration_screen, text="Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)


    label_1 = Label(registration_screen, text="FullName   DR.",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(registration_screen, textvariable=StringVar())
    entry_1.place(x=240,y=130)

    label_2 = Label(registration_screen, text="Email",width=20,font=("bold", 10))
    label_2.place(x=80,y=180)

    entry_2 = Entry(registration_screen, textvariable=StringVar())
    entry_2.place(x=240,y=180)

    label_3 = Label(registration_screen, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=80,y=230)
    var = IntVar()
    Radiobutton(registration_screen, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
    Radiobutton(registration_screen, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

    label_4 = Label(registration_screen, text="Qualification",width=20,font=("bold", 10))
    label_4.place(x=80,y=280)

    list1 = ['MD','MS','MBBS','BAMS','BHMS','GFAM'];
    c=StringVar()
    droplist=OptionMenu(registration_screen,c, *list1)
    droplist.config(width=25)
    c.set('Select Your Medical Degree') 
    droplist.place(x=240,y=280)

    label_5 = Label(registration_screen, text="Clinic Address",width=20,font=("bold", 10))
    label_5.place(x=80,y=330)
    entry_3 = Entry(registration_screen, textvariable=StringVar(), width=40)
    entry_3.place(x=240,y=330)

    label_6 = Label(registration_screen, text="Phone Number",width=20,font=("bold", 10))
    label_6.place(x=80,y=380)
    entry_4 = Entry(registration_screen, textvariable=IntVar(), width=40)
    entry_4.place(x=240,y=380)

    Button(registration_screen, text='Submit',width=20,bg='brown',fg='white',command=registration_verification).place(x=180,y=430)
    Button(registration_screen, text='Back',width=20,bg='brown',fg='white',command=back_reg).place(x=180,y=480)


    registration_screen.mainloop()




root.overrideredirect(True)
progressbar = ttk.Progressbar(orient=HORIZONTAL, length=10000, mode='determinate')
progressbar.pack(side='bottom')
app = DemoSplashScreen(root)
progressbar.start()
    
root.after(5000, root.destroy)


login_registration()
global patient_symptoms, patient_disease






#splashscreeen start----------------------------------------------------------
class DemoSplashScreen:
    def __init__(self, parent):
        self.parent = parent
        self.Splash()
        self.Window()

    def Splash(self):
        self.openimage = Image.open('logo_complete.jpg')
        self.imgSplash = ImageTk.PhotoImage(self.openimage)


    def Window(self):
        # ambil ukuran dari file image
        length, width = self.openimage.size
 
        winLen = (self.parent.winfo_screenwidth()-length)//2
        winwidth = (self.parent.winfo_screenheight()-width)//2
 
        # atur posisi window di tengah-tengah layar
        self.parent.geometry("%ix%i+%i+%i" %(length, width,
                                             winLen,winwidth))
 
        # atur Image via Komponen Label
        Label(self.parent, image=self.imgSplash).pack()
#---------------------------------------------------------------------------------















