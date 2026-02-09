from tkinter import * 
from tkinter import ttk 
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date 

#cores 

color1 = "#3b3b3b" 
color2 = '#333333'
color3 = '#ffffff'
color4 = "#fcc058"

window = Tk()
window.title('Calculadora de idade')
window.geometry('310x410')

window.configure(bg=color1)#backgroundcolor 

style = ttk.Style(window)

style.theme_use('clam')

#frames 

top_frame = Frame(window,width=310, height=140, padx=0, pady=0,
                  relief='flat', bg=color2)

top_frame.grid(row=0,column=0)

bottom_frame = Frame(window, width=310, height=410,
                     padx=0, pady=0, relief='flat',
                     bg=color1)

bottom_frame.grid(row=1, column=0, sticky=NW)

#labels top frame

app_calculator = Label(top_frame, text='Calculadora de ', width=25, height=1, padx=3,
                       relief='flat', anchor='center', font=('Ivy 15 bold'),
                       bg=color2, fg=color3)


app_calculator.place(x=0, y=30)

app_of_rage = Label(top_frame, text='idade', width=11, height=1, padx=0,
                    relief='flat', anchor='center', 
                    font=('Arial 35 bold'), bg=color2, fg=color3)

app_of_rage.place(x=0, y=70)

#labels bottom frame 

l_initial_date = Label(bottom_frame, text='data inicial', height=1, padx=0, pady=0,
                       relief='flat', anchor=NW, font=('Ivy 9'), bg=color1, fg=color3)

l_initial_date.place(x=50, y=30 )


cal_l_initial_date = DateEntry(bottom_frame, width=10,
                      background='darkblue', foreground='w', borderwidth =2, date_pattern='mm/dd/y', year=2026)

cal_l_initial_date.place(x=150, y=30 )

l_birth_date = Label(bottom_frame, text='birth date', height=1, padx=0, pady=0,
                     relief='flat', anchor=NW, font=('Ivy 9'), bg=color1, fg=color3)
l_birth_date.place(x=50, y=70)


cal_l_birth_date = DateEntry(bottom_frame, width=10, bg='darkblue', fg='white',
                               borderwidtht=2, date_pattern = 'mm/dd/y', year =2000)

cal_l_birth_date.place(x=150, y=70)

app_years = Label(bottom_frame, text='27', height=1, padx=0,
                  relief='flat', anchor='center', font=('Ivy 25 bold'), bg=color1, fg=color3)
app_years.place(x=60, y=135)

app_label_years = Label(bottom_frame, text='years', height=1, padx=0,
                        relief='flat', anchor='center', font=('Ivy 11 bold'), bg=color1,
                        fg=color3)

app_label_years.place(x=50, y=175)

app_months = Label(bottom_frame, text='27', height=1, padx=0,
                   relief='flat',anchor='center', font=('Ivy 12 bold'), bg=color1, 
                   fg=color3)
app_months.place(x=140, y=135)

app_label_mounths = Label(bottom_frame, text='Months', height=1, padx=0,
                       relief='flat', anchor='center', font=('Ivy 11 bold'), bg= color1,fg=color3 )
app_label_mounths.place(x=220, y=135)
app_days = Label(bottom_frame, text='27', padx=0, height=1,
                 relief='flat', anchor='center', font=('Ivy 10 bold'),
                 bg= color1, fg=color3)
app_days.place(x=140, y= 180)
app_labels_days = Label(bottom_frame, text='days', height=1, padx=0,
                   relief='flat', anchor='center', font=('Ivy 12 bold'), 
                   bg= color1, fg=color3)

app_labels_days.place(x=210, y=175)


def calcular_age():
    initial_date_str = cal_l_initial_date.get()
    birth_Date_str = cal_l_birth_date.get()
    month_1, day_1 , year_1 = [int(f) for f in initial_date_str.split('/')]
    initial_date = date(year_1, month_1, day_1)

    month_2, day_2 , year_2 = [int(f) for f in birth_Date_str.split('/')]
    birth_date = date(year_2, month_2, day_2)

    years = relativedelta(initial_date, birth_date).years
    month = relativedelta(initial_date,birth_date).month
    days = relativedelta(initial_date, birth_date).days


    app_years['text'] = years
    app_months['text'] = month
    app_days['text'] = days 

#botão calcular

b_calcular = Button(bottom_frame, text='calcular idade', width=20,height=1,
                    bg=color1, fg=color3, font=('Ivy 10 bold'), relief=RAISED,
                    overrelief=RIDGE , command=calcular_age)

b_calcular.place(x=90, y=220)

window.mainloop()