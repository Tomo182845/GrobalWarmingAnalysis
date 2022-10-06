import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

#define
NUM_OF_DAY_PER_YEAR  = 366 # including Leap year.
NUM_OF_RESEARCH_YEAR = 21
FIRST_RESEARCH_YEAR  = 2001
LAST_RESEARCH_YEAR   = FIRST_RESEARCH_YEAR + NUM_OF_RESEARCH_YEAR - 1

YEAR_DISP = range(FIRST_RESEARCH_YEAR,LAST_RESEARCH_YEAR + 1,1)
DISP_FLAG = [False for _ in range(NUM_OF_RESEARCH_YEAR)]

TempratuereData = np.zeros((NUM_OF_RESEARCH_YEAR, NUM_OF_DAY_PER_YEAR))

radio_dic = {
    '-1-': 'Max',
    '-2-': 'Min',
    '-3-': 'Ave',
}

#Read excel file.
df = pd.read_excel('TempratuereData_Tokyo.xlsx', index_col=0)

for i in range(len(df)):
    TempratuereData[df['Year'][i] - FIRST_RESEARCH_YEAR][df['CountDate'][i]-1] = df['Hightemperature'][i]

#Function
def resetFlag():
    for i in range(NUM_OF_RESEARCH_YEAR):
        DISP_FLAG[i] = False

def makeFigure():
    fig = plt.figure(figsize=(16,14))
    for i in range(NUM_OF_RESEARCH_YEAR):
        if DISP_FLAG[i] == True:
            plt.plot(TempratuereData[i],label = str(YEAR_DISP[i]))
        
    plt.title("Temperature of Tokyo ")
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.legend(loc='upper right')
    plt.grid(linestyle='dotted')

    fig.savefig("GrobalWarming_Tokyo.png")


#Diaplay GUI
sg.theme('DarkTeal7')

layout = [
    [sg.Text('Display temperature of Tokyo ')],
    [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_dic.items()],
    [sg.Checkbox("2001", default=False)],
    [sg.Checkbox("2002", default=False)],
    [sg.Checkbox("2003", default=False)],
    [sg.Checkbox("2004", default=False)],
    [sg.Checkbox("2005", default=False)],
    [sg.Checkbox("2006", default=False)],
    [sg.Checkbox("2007", default=False)],
    [sg.Button('Display figure', key='disp')],
    [sg.Output(size=(80,20))]
]

# ステップ4. ウィンドウの生成
window = sg.Window('Temperature at Tokyo', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED: #ウィンドウのXボタンを押したときの処理
        break

    if event == 'disp':
        resetFlag()
        for value in values.items():
            if value[1]:
                DISP_FLAG[value[0]] = True
        makeFigure()

        print("Make figures :",end ="")
        for i in range(NUM_OF_RESEARCH_YEAR):
            if DISP_FLAG[i] == True:
                print(str(YEAR_DISP[i]) + ",",end ="")
        print("\n")
    
window.close()