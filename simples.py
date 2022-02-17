 
 # Apenas uma interface simples para testar seus codigos.
 # Mas atente que o codigo DEVEM estar dentro de uma função, SEMPRE.
  
import PySimpleGUI as sg
  

def voto(ano): # Não fez diferença se ficava dentro ou fora da classe, so atenção na identação
    from datetime import date 
    from emoji import emojize # só pra praticar, SQN (^_^)
    """
    # ao importar uma biblioteca, depedendo de onde ela esta
    # Ela sera usada pelo programa inteiro, mas se ficar dentro
    # da função, ela só funcionará durante a execução, economi-
    # zando memoria.
    """
    atual = date.today().year # não coloque parenteses no year 
    idade = atual - ano      
    if idade < 16:
         # observe que o return pode retornar um 'print()'
        return emojize(f'{idade} anos: NÂO PODE VOTAR :rosto_gritando_de_medo:', language='pt')
    elif 16<= idade <= 18 or idade > 65:
        return emojize(f'{idade} anos: VOTO OPCIONAL :rosto_sorridente_com_óculos_escuros:', language='pt')
    else:
        return emojize(f'{idade} anos: VOTO OBRIGATÓRIO :rosto_de_palhaço:',language='pt')

class Simples_Tela:
    def __init__(self): # self é alguma coisa generico, (sempre usar?)
        sg.theme('LightGrey2') # tema preferencial (achei bonito, foda-se)
        # Define o conteúdo da janela
        layout = [[sg.Text("Qual seu ano de nascimento?")],
                [sg.Input(key='idade')], # entrada dos textos
                [sg.Button('Ok'), sg.Button('Quit')], # dois botôes
                [sg.Text(size=(50,10), key='-OUTPUT-')]] # atenção na saida

        # Cria a janela
        self.window = sg.Window('Janela do Windows').layout(layout)        

        # Exibir e interage com a janela usando um Loop de Evento        
    def iniciar(self):
        while True:
            event, values = self.window.read()
            nasc = int(values['idade']) # como era um valor de entrada (input), tranformei num int pra usar
            #print(voto(nasc)) # coloquei pra fora pois atrapalhava no terminal
            # Veja se o usuário quer parar ou a janela foi fechada
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
            # Saída de uma mensagem para a janela, no update, ele age como o print, preste atenção
            self.window['-OUTPUT-'].update(voto(nasc) + " \n\nObrigado por usar o PySimpleGUI", text_color='black')

        # Finalize removendo-se da tela
        self.window.close()

    
tela = Simples_Tela()
tela.iniciar()