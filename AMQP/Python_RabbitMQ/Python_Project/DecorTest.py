from pyfiglet import Figlet

invita = Figlet(font='invita')

def fprint(text):
    print(invita.renderText(text))

fprint("Andrew?")