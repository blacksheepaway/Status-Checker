import requests
import PySimpleGUI as sg
import threading

#Função de checagem do site escolhido
def check_status(url):
    try:
        #Uso da função request
        response = requests.get(url)
        status = response.status_code
        #Resultados e 'traducao' dos códigos de status
        if status == 200:
            message = f'O servidor está em funcionamento. Código de status: {status}'
            sg.popup(message, title='Status do servidor', font=('Arial', 14), icon='success', button_color=('white', '#00cc00'))
        else:
            message = f'O servidor retornou um erro. Código de status: {status}'
            sg.popup_error(message, title='Status do servidor', font=('Arial', 14), button_color=('white', '#cc0000'))
    except requests.exceptions.RequestException as e:
        message = f'Não foi possível se conectar ao servidor. Erro: {e}'
        sg.popup_error(message, title='Status do servidor', font=('Arial', 14), button_color=('white', '#cc0000'))

#Função de checagem do site em um certo período de tempo
def check_status_periodic(url, interval_seconds, stop_event):
    while not stop_event.is_set():
        check_status(url)
        stop_event.wait(interval_seconds)

#Layout
sg.theme('DarkTeal2')
layout = [
    [sg.Text('Status do site', font=('Arial', 24), justification='center', pad=(0, 20))],
    [sg.Text('Digite o URL para verificar:', font=('Arial', 14), pad=(0, 20))],
    [sg.InputText('http://localhost:8080', font=('Arial', 14), key='url')],
    [sg.Text('Clique em "Verificar agora" para verificar manualmente o status do servidor', font=('Arial', 14), justification='center', pad=(0, 20))],
    [sg.Button('Verificar agora', font=('Arial', 14), size=(12, 1), pad=(0, 20), button_color=('white', '#5555ff'), focus=True, bind_return_key=True)],
    [sg.Text('Programe as suas verificações:', font=('Arial', 14), pad=(0, 20))],
    [sg.Input(default_text='10', size=(5, 1), font=('Arial', 14), key='interval_seconds'), sg.Text('seconds', font=('Arial', 14))],
    [sg.Button('Iniciar', font=('Arial', 14), size=(8, 1), pad=(0, 20), button_color=('white', '#00cc00'), focus=True), sg.Button('Stop', font=('Arial', 14), size=(8, 1), pad=(0, 20), button_color=('white', '#cc0000'))],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar', visible=False)]
]

window = sg.Window('Status do site', layout)

interval_seconds = None
stop_event = threading.Event()
t = None

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Verificar agora':
        progress_bar = window['progressbar']
        progress_bar.update(0, visible=True)
        for i in range(100):
            progress_bar.update(i+1)
            if i == 50:
                check_status(values['url'])
        progress_bar.update(0, visible=False)
    elif event == 'Iniciar':
        if interval_seconds is None:
            try:
                interval_seconds = int(values['interval_seconds'])
                if interval_seconds > 0:
                    stop_event.clear()
                    t = threading.Thread(target=check_status_periodic, args=(values['url'], interval_seconds, stop_event))
                    t.daemon = True
                    t.start()
                    window['Iniciar'].update(disabled=True)
                    window['interval_seconds'].update(disabled=True)
                    window['Parar'].update(disabled=False)
            except ValueError:
                pass
    elif event == 'Stop':
        if t is not None:
            stop_event.set()
            t.join()
            t = None
            interval_seconds = None
            window['Iniciar'].update(disabled=False)
            window['interval_seconds'].update(disabled=False)
            window['Parar'].update(disabled=True)
    elif event == 'url':
        url = values['url']

window.close()
