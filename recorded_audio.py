import speech_recognition as sr
import tkinter as tk
from translate import Translator
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
r=sr.Recognizer()
time = None

def asr_e():
    try:
        user = str(ent_1_user.get())
        with sr.AudioFile (ent_path.get()) as source:
            audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data)
                translator= Translator(from_lang="en",to_lang="hi") 
                hindi = translator.translate(text)
                translator= Translator(from_lang="en",to_lang="gu")
                gujarati = translator.translate(text)
                with open('Converted_eng_audioTO_original_'+user+'.txt', 'a') as f:
                        f.write(text+'\n')
                print('You said :{}'.format(text))
                with open('Converted_eng_audioTO_hindi'+user+'.txt', 'ab') as f:
                        f.write(f'{hindi}\n'.encode())
                            #now if we want to read this file then use rb - read binary, that means now file being written in binary format.
                print('Hindi translation :{}'.format(hindi))
                with open('Converted_eng_audioTO_gujarati'+user+'.txt', 'ab') as f:
                        f.write(f'{gujarati}\n'.encode())
                print('Gujarati translation :{}'.format(gujarati))
                
                ent_2_original_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_2_original_txt.grid(row=3,column=1, sticky="e")
                lbl_2_original_txt = tk.Label(master=frm_entry, text="Converted text:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_2_original_txt.grid(row=3, column=0, sticky="e")
                lbl_2_original_txt.grid(row=3, column=0, padx=10)
                
                ent_3_hindi_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_3_hindi_txt.grid(row=4,column=1, sticky="e")
                lbl_3_hindi_txt = tk.Label(master=frm_entry, text="Hindi Translation:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_3_hindi_txt.grid(row=4, column=0, sticky="e")
                lbl_3_hindi_txt.grid(row=4, column=0, padx=10)
                
                ent_4_guj_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_4_guj_txt.grid(row=5,column=1, sticky="e")
                lbl_4_guj_txt = tk.Label(master=frm_entry, text="Gujarati Translation:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_4_guj_txt.grid(row=5, column=0, sticky="e")
                lbl_4_guj_txt.grid(row=5, column=0, padx=10)
                
                ent_2_original_txt.delete(0,tk.END)
                ent_2_original_txt.insert(0,text)
                
                ent_3_hindi_txt.delete(0,tk.END)
                ent_3_hindi_txt.insert(0,hindi)
                
                ent_4_guj_txt.delete(0,tk.END)
                ent_4_guj_txt.insert(0,gujarati)
            except Exception as E:
                    print("Error :",E)
                    print('sorry,could not recognize') #display this in new window like alert box of tkinter
        return(text,hindi,gujarati)
    except Exception as E:
        print("Error :",E)#same thing, display alert box..most time mic error will occur here if occurs

def asr_h():
    try:
        user = str(ent_1_user.get())
        with sr.AudioFile (ent_path.get()) as source:
            audio_data = r.record(source)
            try:
                text=r.recognize_google(audio_data,language='hi-EN')
                translator= Translator(from_lang="hi-EN",to_lang="en") #lang. code taken from iso code list
                eng = translator.translate(text)
                translator= Translator(from_lang="hi-EN",to_lang="gu") #lang. code taken from iso code list
                gujarati = translator.translate(text)
                with open('Converted_hindi_audioTO_original_'+user+'.txt', 'ab') as f:
                        f.write(f'{text}\n'.encode())
                print('You said :{}'.format(text))
                with open('Converted_hindi_audioTO_eng_'+user+'.txt', 'a') as f:
                        f.write(eng+'\n')
                print('English translation :{}'.format(eng))
                with open('Converted_hindi_audioTO_gujarati_'+user+'.txt', 'ab') as f:
                       f.write(f'{gujarati}\n'.encode())
                print('Gujarati translation :{}'.format(gujarati))
                
                ent_2_original_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_2_original_txt.grid(row=3,column=1, sticky="e")
                lbl_2_original_txt = tk.Label(master=frm_entry, text="Spoken Speech:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_2_original_txt.grid(row=3, column=0, sticky="e")
                lbl_2_original_txt.grid(row=3, column=0, padx=10)
                
                ent_3_eng_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_3_eng_txt.grid(row=4,column=1, sticky="e")
                lbl_3_eng_txt = tk.Label(master=frm_entry, text="English Translation:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_3_eng_txt.grid(row=4, column=0, sticky="e")
                lbl_3_eng_txt.grid(row=4, column=0, padx=10)
                
                ent_4_guj_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_4_guj_txt.grid(row=5,column=1, sticky="e")
                lbl_4_guj_txt = tk.Label(master=frm_entry, text="Gujarati Translation:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_4_guj_txt.grid(row=5, column=0, sticky="e")
                lbl_4_guj_txt.grid(row=5, column=0, padx=10)
                
                ent_2_original_txt.delete(0,tk.END)
                ent_2_original_txt.insert(0,text)
                
                ent_3_eng_txt.delete(0,tk.END)
                ent_3_eng_txt.insert(0,eng)
                
                ent_4_guj_txt.delete(0,tk.END)
                ent_4_guj_txt.insert(0,gujarati)
            except Exception as E:
                print("Error :",E)
                print('sorry,could not recognize') #display this in new window like alert box of tkinter
        return(eng,text,gujarati)
    except Exception as E:
        print("Error :",E)

def asr_g():
    try:
        user = str(ent_1_user.get())
        with sr.AudioFile (ent_path.get()) as source:
            audio_data = r.record(source)
            try:
                text=r.recognize_google(audio_data,language='gu')
                translator= Translator(from_lang="gu",to_lang="hi-EN") #lang. code taken from iso code list
                hindi = translator.translate(text)
                translator= Translator(from_lang="gu",to_lang="en") #lang. code taken from iso code list
                eng = translator.translate(text)
                with open('Converted_gujarati_audioTO_original_'+user+'.txt', 'ab') as f:
                        f.write(f'{text}\n'.encode())
                print('You said :{}'.format(text))
                with open('Converted_gujarati_audioTO_eng_'+user+'.txt', 'a') as f:
                        f.write(eng+'\n')
                print('English translation :{}'.format(eng))
                with open('Converted_gujarati_audioTO_hindi_'+user+'.txt', 'ab') as f:
                        f.write(f'{hindi}\n'.encode())
                print('Hindi translation :{}'.format(hindi))
                
                ent_2_original_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_2_original_txt.grid(row=3,column=1, sticky="e")
                lbl_2_original_txt = tk.Label(master=frm_entry, text="Spoken Speech:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_2_original_txt.grid(row=3, column=0, sticky="e")
                lbl_2_original_txt.grid(row=3, column=0, padx=10)
                
                ent_3_eng_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_3_eng_txt.grid(row=4,column=1, sticky="e")
                lbl_3_eng_txt = tk.Label(master=frm_entry, text="English Translation:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_3_eng_txt.grid(row=4, column=0, sticky="e")
                lbl_3_eng_txt.grid(row=4, column=0, padx=10)
                
                ent_4_hindi_txt = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
                ent_4_hindi_txt.grid(row=5,column=1, sticky="e")
                lbl_4_hindi_txt = tk.Label(master=frm_entry, text="Hindi Translation:",fg='blue',font=("Times New Roman", 25))
                #lbl_2_original_txt = tk.Label(master=frm_entry)
                lbl_4_hindi_txt.grid(row=5, column=0, sticky="e")
                lbl_4_hindi_txt.grid(row=5, column=0, padx=10)
                
                ent_2_original_txt.delete(0,tk.END)
                ent_2_original_txt.insert(0,text)
                
                ent_3_eng_txt.delete(0,tk.END)
                ent_3_eng_txt.insert(0,eng)
                
                ent_4_hindi_txt.delete(0,tk.END)
                ent_4_hindi_txt.insert(0,hindi)
            except Exception as E:
                print("Error :",E)
                print('sorry,could not recognize') #display this in new window like alert box of tkinter
        return(eng,hindi,text)
    except Exception as E:
        print("Error :",E)

window = tk.Tk()
window.title("Automatic Speech Recognition")
window.resizable(width=True, height=True)
window.rowconfigure(0, minsize=80, weight=1)
window.columnconfigure(0, minsize=80, weight=1)
window.configure(bg='#dceccf')
window.geometry("800x440")

#Enter user name vadu label
#lbl1 = Label(window, text="Enter the user name :",font=("Times New Roman",25))
#lbl1.grid(column=0, row=0)

frm_entry = tk.Frame(master=window)
frm_entry.grid(row=0, column=0, padx=5)

ent_1_user = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
ent_1_user.grid(row=0, column=1, sticky="e")
lbl_1_user = tk.Label(text="Enter the user name :", master=frm_entry, fg='blue',font=("Times New Roman", 25))
#lbl_1_user = tk.Label(master=frm_entry)
lbl_1_user.grid(row=0, column=0, sticky="e")
lbl_1_user.grid(row=0, column=0, padx=10)

#SELECTION LIST VADU LABEL
#lbl2 = Label(window, text="Select the language you will speak: ",font=("Times New Roman",25),justify=["left"])
#lbl2.grid(row=1,column=0)
ent_path = tk.Entry(master=frm_entry, width=50,fg='black',font=("Times New Roman", 25))
ent_path.grid(row=1, column=1, sticky="e")
lbl_path = tk.Label(text="Enter the path of your Audio file :", master=frm_entry, fg='blue',font=("Times New Roman", 25))
#lbl_1_user = tk.Label(master=frm_entry)
lbl_path.grid(row=1, column=0, sticky="e")
lbl_path.grid(row=1, column=0, padx=10)

selected_action = tk.StringVar()
action_cb = ttk.Combobox(master=frm_entry,textvariable=selected_action,height=20,justify=tk.LEFT)
action_cb['values']= ('Hindi','English', 'Gujarati')
action_cb['state'] = 'readonly'
#action_cb.grid(row=1,column=1)
action_cb.grid(row=2,column=1, sticky="w")
action_cb_lbl = tk.Label(text="Select the language you will speak: ",master=frm_entry, fg='blue',font=("Times New Roman",25))
action_cb_lbl.grid(row=2, column=0, sticky="e")
action_cb_lbl.grid(row=2, column=0)

#action_cb.pack(fill=tk.X, padx=5, pady=5)
def action_changed(event):
    AB = selected_action.get()
    if AB=='Hindi':
        asr_h()
    elif AB=='English':
        asr_e()
    elif AB=='Gujarati':
        asr_g()
action_cb.bind('<<ComboboxSelected>>', action_changed)

#original speech to text nu label
#lbl3 = Label(window, text="Spoken Speech : ",font=("Times New Roman",25),justify=["left"])
#lbl3.grid(column=0, row=2)

window.mainloop()