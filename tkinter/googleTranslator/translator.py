# Aula: https://youtu.be/vNEwbfsZ-Js
# Tutorial ttk styles: pythontutorial.net/tkinter/ttk-style/
# Temas ttk: ttkthemes.readthedocs.io/en/latest/themes.html
# Temas ttk bootstrap: ttkbootstrap.readthedocs.io/en/latest/themes
# Tema CustomTkinter: github.com/TomSchimansky/CustomTkinter
# Tema Azure-ttk-theme: github.com/rdbende/Azure-ttk-theme
# Coleção de widgets para o tkinter: github.com/Dogeek/tkinter-pp
# API google translator: pypi.org/project/googletrans/

# Necessário instalar
# pacman -S tk
# pip install googletrans==3.1.0a0
# pip install ttkthemes
# pip install ttkbootstrap

from tkinter import ttk, Text
#from ttkthemes import ThemedTk
from ttkbootstrap import Style
from googletrans import Translator

translator = Translator()

# pt - portuguese | en - english | es - spanish | it - italian
def trans(evento=None): # Ignora o evento do window.bind
    text   = text_input.get('1.0', 'end')
    src    = combo_input.get()
    dest   = combo_output.get()
    result = translator.translate(text=text, src=src, dest=dest)

    text_output.configure(state='normal')
    text_output.delete('1.0', 'end')
    text_output.insert('1.0', result.text)
    text_output.configure(state='disabled')

    #return result

#window = Tk() # Tema padrão do Tk

# Temas ( adapta | aquativo | arc | black | blue | breeze | clearlooks | elegance | equilux | itft1
# keramik | kroc | plastik | radiance | scid themes | smog | winxpblue | yaru )
#window = ThemedTk(theme='breeze') # Temas oficiais do ttk

window = Style(theme='minty').master # Temas do ttk bootstrap
window.title('Google Translator')

# Frames
frame_general = ttk.Frame()
frame_input   = ttk.Frame(frame_general)
frame_output  = ttk.Frame(frame_general)

label_input  = ttk.Label(frame_input, text='Input')
label_output = ttk.Label(frame_output, text='Output')

# Janelas de seleção de idiomas
languages    = ['pt', 'en', 'es', 'it']
combo_input  = ttk.Combobox(frame_input, values=languages)
combo_output = ttk.Combobox(frame_output, values=languages)
combo_input.set('pt')
combo_output.set('en')

text_input  = Text(frame_general, height=10, width=50, font=(None, 15))
text_output = Text(frame_general, height=10, width=50, font=(None, 15), state='disabled')

button_translate = ttk.Button(frame_general, text='Translate', command=trans)

# Mostrar
label_input.grid(row=0, column=0, padx=10, pady=10)
combo_input.grid(row=0, column=1, padx=10, pady=10)
frame_input.pack()
text_input.pack(padx=10, fill='both', expand='yes')

label_output.grid(row=0, column=0, padx=10, pady=10)
combo_output.grid(row=0, column=1, padx=10, pady=10)
frame_output.pack()
text_output.pack(padx=10, fill='both', expand='yes')

button_translate.pack(padx=20, pady=10, fill='both')

frame_general.pack(fill='both')

# Traduz ao apertar enter
window.bind('<Return>', trans)

window.mainloop()



