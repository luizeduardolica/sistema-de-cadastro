# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


# Trabalhando no Frame Logo --------------------

app_lg = Image.open('img\logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Poppins 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

# funcao para cadastrar alunos
def alunos():
    print('Aluno')


# funcao para adicionar cursos e turmas
def adicionar():
    # Criando frames para tabelas ----------
    frame_tabela_curso =  Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha =  Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma =  Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)


     # Detalhes do Curso ---------------------------

    l_nome = Label(frame_detalhes, text="Nome do Curso", height=1, anchor=NW, font=('Poppins 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nomecurso =  Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nomecurso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Poppins 10'), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao =  Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font=('Poppins 10'), bg=co1, fg=co4)
    l_preco.place(x=4, y=130)
    e_preco =  Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_preco.place(x=7, y=160)

    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Poppins 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Poppins 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=187, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='deletar'.upper(), width=10, overrelief=RIDGE, font=('Poppins 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=267, y=160)


    # Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['ID','Curso','Duração','Preço']

        df_list = []

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,150,80,60]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_curso.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()



    # Linha Separatória ------------------------------

    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Poppins 1'), bg=co0, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Poppins 1'), bg=co1, fg=co0)
    l_linha.place(x=372, y=10)


    # Linha Tabela ------------------------------

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Poppins 1'), bg=co0, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Poppins 1'), bg=co1, fg=co0)
    l_linha.place(x=4, y=10)


    # Detalhes da turma ---------------------------
    l_nome = Label(frame_detalhes, text="Nome da Turma", height=1, anchor=NW, font=('Poppins 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma =  Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_turma.place(x=407, y=40)

    l_curso = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=('Poppins 10'), bg=co1, fg=co4)
    l_curso.place(x=404, y=70)

    # Pegando os cursos
    cursos = ['Curso 1', 'Curso 2']
    curso = []

    for i in cursos:
        curso.append(i)

    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Poppins 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x=407, y=100)


    l_data_inicio = Label(frame_detalhes, text="Data de Início *", height=1, anchor=NW, font=('Poppins 10'), bg=co1, fg=co4)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white',  borderwidth=2, year=2023)
    data_inicio.place(x=407, y=160)

    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Poppins 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=507, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Poppins 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=587, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='deletar'.upper(), width=10, overrelief=RIDGE, font=('Poppins 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=667, y=160)


    # Tabela turmas
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # creating a treeview with dual scrollbars
        list_header = ['ID','Nome da Turma','Curso','Início']

        df_list = []

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            # adjust the column's width to the header string
            tree_turma.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turmas()



# funcao para salvar
def salvar():
    print('Salvar')



# Funcao de controle -------------------------------

def control(i):
    #cadastro de alunos
    if i == 'cadastro':
        for  widget in frame_detalhes.winfo_children():
            widget.destroy()

        for  widget in frame_tabela.winfo_children():
            widget.destroy()

        #chamando a funcao aluno
        alunos()
    
    if i == 'adicionar':
        for  widget in frame_detalhes.winfo_children():
            widget.destroy()

        for  widget in frame_tabela.winfo_children():
            widget.destroy()

        #chamando a funcao adicionar
        adicionar()

    if i == 'salvar':
        for  widget in frame_detalhes.winfo_children():
            widget.destroy()

        for  widget in frame_tabela.winfo_children():
            widget.destroy()

        #chamando a funcao salvar
        salvar()



# Criando Botões
app_img_cadastro = Image.open('img\\add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Poppins 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

app_img_adicionar = Image.open('img\\add.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=('Poppins 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)

app_img_salvar = Image.open('img\save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Poppins 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)






# Executando a janela
janela.mainloop()
