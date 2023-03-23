import PySimpleGUI as sg
'''
GUI interface

'''
# text1="'using device:{}'.format(device)"
# text2="'Chitchat Robot Starting'"
# text3="chatbot: 说点别的吧，好吗？"

global query 

def get_context(text):
    return text

def getinput():
    return query

def gui(text1, text2, input_text3, answer_text4)
    sg.theme('GreenTan')
    layout = [[sg.Image("image/show.png")],#如何平铺展示
            [sg.Text('WELOCME TO JIAN N !', size=(40, 1),expand_x=True)],
            [sg.InputText()],
            [sg.Text(text1, size=(40, 1),expand_x=True)],#加字体，大小
            [sg.Text(text2, size=(40, 1),expand_x=True)],#加字体，大小
            [sg.Output(size=(110, 20), font=('Helvetica 10'))],
            [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
            sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
            sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('JIAN N', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

    while True:    
        event, value = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):
            break
        if event == 'SEND':
            query = value['-QUERY-'].rstrip()
            # EXECUTE YOUR COMMAND HERE
            print('question:{}'.format(query), flush=True)
            print('{}'.format(answer_text4), flush=True)#显示回答

    window.close()