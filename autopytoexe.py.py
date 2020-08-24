from tkinter.filedialog import *
import tkinter as tk
from tkinter import *
from pymsgbox import *
import os
import platform

so = platform.system()
if 'Lin' in so:
 tela = Tk()
 tela.title('Auto PyToExe')
 tela.geometry('268x307+250+250')
 tela.configure(background = '#6CA0EA')
 tela.minsize(268,315)
 tela.maxsize(268,315)
 def bt1_function():
  f1 = filedialog.askopenfilename()
  tb1.insert(tk.INSERT, f1)
 def bt2_function():
  f2 = askopenfilename()
  tb2.insert(tk.INSERT, f2)

 def sem_cmd():
  opcao["text"] = 'Opção atual: Terminal desabilitado'
 def com_cmd():
  opcao["text"] = 'Opção atual: Terminal habilitado'

 def confirmar():
  alert(text='A compilação do seu projeto foi iniciada', title='Convertendo...', button='OK')
  if opcao["text"] == 'Opção atual: Terminal desabilitado':
   opf = '-w '
  else:
   opf = ''
  icone = tb1.get()
  if icone == '':
   ico = ''
   alert(text='Nenhum ícone escolhido. O programa será compilado com o ícone padrão', title='', button='OK')
  else:
   ico = icone
  path = tb2.get()
  if path == '':
   alert(text='O caminho do script não foi informado, não é possível iniciar a compilação', title='Erro', button='OK')
  else:
   try:
    opcao["text"] = 'Status: Conversão em andamento'
    if icone == '':
     os.system('mkdir AutoPyToExe & cd AutoPyToExe & pyinstaller -y -F "%s" %s' % (path, opf))
    else:
     os.system('mkdir AutoPyToExe & cd AutoPyToExe & pyinstaller -i "%s" -y -F "%s" %s' % (ico, path, opf))
   except:
    try:
     alert(text='Seu pyinstaller não está instalado, o programa instalou automaticamente', title='Pyinstaller', button='OK')
     os.system('pip install pyinstaller')
    except:
     alert(text='Não foi detectado o "pip" no seu computador. Instale e execute novamente o programa, para instalar o pyinstaller automaticamente', title='"pip" não encontrado', button='OK')
   opcao["text"] = 'Status: Compilado com sucesso'

 l1 = Label(font = ('overstrike', 15),text=' Local do ícone:')
 l1.place(x = '5', y = '10')
 l1.configure(background = '#6CA0EA')
 tb1 = Entry(width = 20, fg = '#BD14FF')
 tb1.place(x = '10', y = '44')
 bt1 = Button(font = ('overstrike', 8), text = 'Localizar', fg = '#000000' , command = bt1_function)
 bt1.configure(background='#6CADEA')
 bt1.place(x = '183', y = '42')

 l2 = Label(font = ('overstrike', 15),text=' Local do script:')
 l2.place(x = '5', y = '80')
 l2.configure(background = '#6CA0EA')
 tb2 = Entry(width = 20, fg = '#BD14FF')
 tb2.place(x = '10', y = '114')
 bt2 = Button(font = ('overstrike', 8), text = 'Localizar', command = bt2_function, fg = '#000000')
 bt2.place(x = '183', y = '112')
 bt2.configure(background='#6CADEA')

 l3 = Label(font = ('overstrike', 15),text=' Opções do programa:')
 l3.place(x = '5', y = '150')
 l3.configure(background = '#6CA0EA')
 bt3 = Button(font = ('arial', 11), text = 'Com console', width = 11, command=com_cmd)
 bt3.place(x = '139', y = '188')
 bt3.configure(background='#6CADEA')

 bt4 = Button(font = ('arial', 11), text = 'Sem console', width = 11, command = sem_cmd)
 bt4.place(x = '9', y = '188')
 bt4.configure(background='#6CADEA')

 opcao = Label(font = ('arial', 10),text='Opção atual: ')
 opcao.place(x = '11', y = '225')
 opcao.configure(background='#6CA0EA')

 confirmar = Button(font = ('overstrike', 12), text = 'Converter para .exe', width = 22, fg = '#000000', command = confirmar)
 confirmar.place(x = '10', y = '254')
 confirmar.configure(background='#6CADEA')

 creditos = Label(font=('overstrike', 9), text = 'Feito por Canal TI (Kaleb Silva) © | Tkinter', fg = '#42ebf4')
 creditos.place(x = '10', y = '290')
 creditos.configure(background='#6CA0EA')
 
else:
 tela = Tk()
 tela.title('Auto PyToExe')
 tela.geometry('268x310+250+250')
 tela.configure(background = '#6CA0EA')
 tela.minsize(268,315)
 tela.maxsize(268,315)
 def bt1_function():
  f1 = filedialog.askopenfilename()
  tb1.insert(tk.INSERT, f1)
 def bt2_function():
  f2 = askopenfilename()
  tb2.insert(tk.INSERT, f2)

 def sem_cmd():
  opcao["text"] = 'Opção atual: Console (CMD) desabilitado'
 def com_cmd():
  opcao["text"] = 'Opção atual: Console (CMD) habilitado'

 def confirmar():
  alert(text='A compilação do seu projeto foi iniciada', title='Convertendo...', button='OK')
  if opcao["text"] == 'Opção atual: Console (CMD) desabilitado':
   opf = '-w '
  else:
   opf = ''
  icone = tb1.get()
  if icone == '':
   ico = ''
   alert(text='Nenhum ícone escolhido. O programa será compilado com o ícone padrão', title='', button='OK')
  else:
   ico = icone
  path = tb2.get()
  if path == '':
   alert(text='O caminho do script não foi informado, não é possível iniciar a compilação', title='Erro', button='OK')
  else:
   try:
    opcao["text"] = 'Status: Conversão em andamento'
    if icone == '':
     os.system('md AutoPyToExe & cd AutoPyToExe & pyinstaller -y -F "%s" %s' % (path, opf))
    else:
     os.system('md AutoPyToExe & cd AutoPyToExe & pyinstaller -i "%s" -y -F "%s" %s' % (ico, path, opf))
   except:
    try:
     alert(text='Seu pyinstaller não está instalado, o programa instalou automaticamente', title='Pyinstaller', button='OK')
     os.system('pip install pyinstaller')
    except:
     alert(text='Não foi detectado o "pip" no seu computador. Instale e execute novamente o programa, para instalar o pyinstaller automaticamente', title='"pip" não encontrado', button='OK')
   opcao["text"] = 'Status: Compilado com sucesso'

 l1 = Label(font = ('overstrike', 15),text=' Local do ícone:')
 l1.place(x = '5', y = '10')
 l1.configure(background = '#6CA0EA')
 tb1 = Entry(width = 30, fg = '#BD14FF')
 tb1.place(x = '10', y = '44')
 bt1 = Button(font = ('overstrike', 8), text = 'Localizar', fg = '#000000' , command = bt1_function)
 bt1.configure(background='#6CADEA')
 bt1.place(x = '203', y = '42')

 l2 = Label(font = ('overstrike', 15),text=' Local do script:')
 l2.place(x = '5', y = '80')
 l2.configure(background = '#6CA0EA')
 tb2 = Entry(width = 30, fg = '#BD14FF')
 tb2.place(x = '10', y = '114')
 bt2 = Button(font = ('overstrike', 8), text = 'Localizar', command = bt2_function, fg = '#000000')
 bt2.place(x = '203', y = '112')
 bt2.configure(background='#6CADEA')

 l3 = Label(font = ('overstrike', 15),text=' Opções do programa:')
 l3.place(x = '5', y = '150')
 l3.configure(background = '#6CA0EA')
 bt3 = Button(font = ('arial', 11), text = 'Com console', width = 12, command=com_cmd)
 bt3.place(x = '137', y = '188')
 bt3.configure(background='#6CADEA')

 bt4 = Button(font = ('arial', 11), text = 'Sem console', width = 12, command = sem_cmd)
 bt4.place(x = '11', y = '188')
 bt4.configure(background='#6CADEA')

 opcao = Label(font = ('arial', 10),text='Opção atual: ')
 opcao.place(x = '11', y = '225')
 opcao.configure(background='#6CA0EA')

 confirmar = Button(font = ('overstrike', 13), text = 'Converter para .exe', width = 26, fg = '#000000', command = confirmar)
 confirmar.place(x = '11', y = '254')
 confirmar.configure(background='#6CADEA')

 creditos = Label(font=('overstrike', 9), text = 'Feito por Canal TI (Kaleb Silva) © | Tkinter', fg = '#42ebf4')
 creditos.place(x = '10', y = '290')
 creditos.configure(background='#6CA0EA')
 
tela.mainloop()
