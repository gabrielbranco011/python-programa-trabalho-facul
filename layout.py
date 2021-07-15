from criptografia import criptografar
import PySimpleGUI as sg

# Deve ter 16, 24 ou 32 bytes de comprimento


class GeradorDeSenha:
    def __init__(self):
        sg.theme('reddit')
        interface = [
            [sg.Text('Tipo de criptografia', auto_size_text=True),
             sg.Checkbox('AES-128', key='128', auto_size_text=True), sg.Checkbox('AES-192', key='192', auto_size_text=True), sg.Checkbox('AES-256', key='256', auto_size_text=True)],
            [sg.Input(size=(35, 10), key='texto', pad=((0, 0), (10, 10)), font=('Bold', 14))],
            [sg.Button('Criptografar', size=(10, 2), pad=(0, 0))],
            [sg.Output(size=(40, 7), font=('Bold', 16), pad=((0, 0), (10, 10)))]
        ]
        self.janela = sg.Window('Criptografia', interface)

    def Inicializador(self):
        while True:
            evento, valor = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break

            if evento == 'Criptografar' and valor['128']:
                texto = valor['texto']
                texto_criptografado = criptografar(texto, 16)
                print('AES-128 = ', texto_criptografado[0])
                print(f'Chave = {texto_criptografado[1]} \n')
            if evento == 'Criptografar' and valor['192']:
                texto = valor['texto']
                texto_criptografado = criptografar(texto, 24)
                print('AES-192 = ', texto_criptografado[0])
                print(f'Chave = {texto_criptografado[1]} \n')
            if evento == 'Criptografar' and valor['256']:
                texto = valor['texto']
                texto_criptografado = criptografar(texto, 32)
                print('AES-256 = ', texto_criptografado[0])
                print(f'Chave = {texto_criptografado[1]} \n')
