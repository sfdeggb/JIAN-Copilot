
import PySimpleGUI as sg
'''
'''
sg.theme('GreenTan')

layout = [[sg.Image("D:/python/NLP-PY/UnilmChatchitRobot/image/show.png",size=(110,10))],
    	  [sg.Text('WELOCME TO JIAN N !', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

while True:    
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break
    if event == 'SEND':
        query = value['-QUERY-'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('question:{}'.format(query), flush=True)

window.close()