from tkinter import * #interface gráfica
from tkinter import filedialog # importar arquivo
from tkinter import ttk
from auxilio_funcs_new import standard, completarTabela, retorna_nome_arquivo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image # colocar imagem no tkinter
import webbrowser
import pandas as pd








# --------------------------- INTERFACE GERAL ---------------------------#
root = Tk()
root.state('zoomed')
# Ícone da barra
root.iconbitmap('favicon.ico')
# Título
root.title("TEORIA ATUARIAL 1: Calculadora de funções biométricas")
# Dimensão e cor do background
root.geometry("1500x600")  
root.config(bg='#3c403d')
# Setando imagem hourglass
img = Image.open("hourglass.png")
#print(img.mode) # A imagem deve ser do tipo RGBA para o background ser transparente
img_resized = img.resize((80, 110), Image.Resampling.LANCZOS) #resize (width, height)
img = ImageTk.PhotoImage(img_resized)
label_image = Label(root, image=img, bg="#3c403d")
label_image.place(x = 1000, y=2)
# Botão de opções
standard.pop(0) 
my_list = standard
options = StringVar(root)
options.set(my_list[0])
om1 = OptionMenu(root, options, *my_list) 
om1.configure(bg='#303330', height= 1, width=2, fg = '#e0dcd1', activebackground='#6a017a', cursor='hand2')
om1["highlightthickness"] = 0 
om1["menu"].config(bg="#303330", fg="#e0dcd1") 
om1.place(x = 20, y = 10)








# --------------------------- IMAGEM GITHUB ---------------------------#
img_github = Image.open("github4.png")
img_github_resized = img_github.resize((70, 40), Image.Resampling.LANCZOS) 
img_github = ImageTk.PhotoImage(img_github_resized)
label_image_github = Label(root, image=img_github, bg="#3c403d")
label_image_github.place(x = 15, y=695)






filepath = None
df_gui = None
w_df_gui = None
idade_min = DoubleVar()
idade_max = DoubleVar() 
        


def openFile():
    l8.place_forget()
    tv1.place_forget()
    treescolly.place_forget()
    treescrollx.place_forget()
    global filepath 
    global df_gui
    global w_df_gui

    filepath_aux = filedialog.askopenfilename()
    nomeArquivo = retorna_nome_arquivo(filepath_aux)
    if len(nomeArquivo) <= 22:
        l8.config(text=f'{nomeArquivo}', bg='#6a017a', font=("Ubuntu", 8), fg = '#e0dcd1', height=1, relief=SUNKEN)
        l8.place(x=206, y=12)
    else:
        l8.config(text=f'{nomeArquivo[0:16]}...', bg='#6a017a', font=("Ubuntu", 8), fg = '#e0dcd1', height=1, relief=SUNKEN)
        l8.place(x=206, y=12)
    filepath = nomeArquivo
    df_gui = completarTabela(filepath_aux)
    w_df_gui = len(df_gui.index)-1
    

    df = pd.DataFrame(df_gui)
    for column in list(df.columns):
        if column == 'x':
            # df[column] = df[column].apply(lambda x: int(x))
            # df[column] = df[column].apply(lambda x: str(x))
            pass
        elif column == 'l_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        elif column == 'd_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        elif column == 'q_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        elif column == 'p_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        elif column == 'L_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        elif column == 'T_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        elif column == 'e_x':
            df[column] = df[column].apply(lambda x: round(x, 2))
        elif column == 'u_x':
            df[column] = df[column].apply(lambda x: round(x, 8))
        else:
            df[column] = df[column].apply(lambda x: round(x, 8))
    
    tv1.place(relheight=0.96, relwidth=0.98)
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescolly.set)
    treescrollx.pack(side='bottom', fill='x')
    treescolly.pack(side='right', fill='y')
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist() 
    for row in df_rows:
        tv1.insert("", "end", values=row)

def callback(url):
    webbrowser.open_new(url)








# --------------------------- IMAGEM/LINK GITHUB ---------------------------#
link_label = Label(root, text= "github.com/jgpds", bg='#3c403d', fg='#cb42f5', cursor='hand2', font=('Ubuntu', 13, 'italic', UNDERLINE))
link_label.place(x = 80, y = 700)
link_label.bind("<Button-1>", lambda e: callback("https://github.com/jgpds/"))
b2 = Button(root, text="Escolha o arquivo", command= openFile, cursor='hand2')
b2.place(x=100, y=10)
b2.configure(bg='#303330', fg = '#e0dcd1', activebackground='#6a017a')


def imprimirOpcao(df_aux, idade_min, idade_max):
    print(f'df_aux{df_aux}')
    print(f'idade min : {idade_min}')
    print(f"idade max : {idade_max}")
    plt.clf()
    opcao = options.get()
    l7 = Label(root, text=f'Opção selecionada: {opcao}', bg='#3c403d', font=("Ubuntu", 10), fg = '#e0dcd1')
    l7.place(x=80, y=50)


    f = plt.figure(figsize=(6,4), dpi=100, facecolor='#3c403d', edgecolor='w')
    axes = f.add_subplot()#.plot(df_aux['x'], df_aux[opcao], '-ok')
    axes.set_title(f"Idade vs {opcao}")
    print(f"df_aux['x']: {df_aux['x']}")
    axes.plot(df_aux['x'], df_aux[opcao], '-ok')
    axes.set_ylabel(f"{opcao}")
    axes.set_xlabel("Idade")
    axes.set_facecolor("#cb42f5")
    chart = FigureCanvasTkAgg(f, root)
    chart.get_tk_widget().place(x=983, y=150)



def calculate_results(idade_min, idade_max):
    df_aux = df_gui.loc[idade_min:idade_max]
    return df_aux 


def show1():
    l1.place_forget()
    l2.place_forget()
    l5.place_forget()
    l6.place_forget()
    label_interpretacao.place_forget()
    if idade_max.get() < idade_min.get():
        l5.config(text="**AVISO: A idade máxima deve ser maior ou igual que a idade mínima**".upper(),
         font=("Ubuntu", 14, 'bold'), fg = "#8f0101", bg='#3c403d', justify=CENTER)
        l5.place(x=100 , y=110)
        
    elif idade_max.get() == idade_min.get():
        df_aux = calculate_results(int(idade_min.get()), int(idade_max.get()))
        l6.config(text=f"Idade = {int(idade_min.get())}", font=("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
        l6.place(x = 370, y = 50)  
        imprimirOpcao(df_aux, int(idade_min.get()), int(idade_max.get()))      
    else:
        df_aux = calculate_results(int(idade_min.get()), int(idade_max.get()))
        sel = "Idade minima = " + str(int(idade_min.get()))
        sel2 = "Idade máxima = " + str(int(idade_max.get())) 
        l1.config(text = sel, font =("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
        l2.config(text = sel2, font =("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
        l1.place(x = 350, y = 50) 
        l2.place(x = 350, y = 70)
        imprimirOpcao(df_aux, int(idade_min.get()), int(idade_max.get()))  
 








# ------------------- LABELS AND BUTTONS CONFIGURATION ---------------------#
s1 = Scale( root, variable = idade_min,  
           from_ = 0, to = w_df_gui,  
           orient = VERTICAL, bg='#303330', fg = '#e0dcd1', highlightthickness=1,
            highlightbackground='black', activebackground="#6a017a", cursor='hand2') 

s2 = Scale( root, variable = idade_max,  
           from_ = 0, to = w_df_gui,  
           orient = VERTICAL, bg='#303330', fg = '#e0dcd1', highlightthickness=1,
            highlightbackground='black', activebackground="#6a017a", cursor='hand2')
b1 = Button(root, text ="CALCULAR",  
            command = show1,  
            bg = '#303330', width=20, font=('Ubuntu', 12), fg = '#e0dcd1',
             borderwidth= 3, activebackground="#6a017a", cursor='hand2')   
l1 = Label(root) 
l2 = Label(root)
l3 = Label(root)
l4 = Label(root)
l5 = Label(root)
l6 = Label(root)
l8 = Label(root)
label_interpretacao = Label(root)
label_guide = Label(root)
label_guide.config(text="1. Selecione uma função biométrica;\n2. Selecione uma idade mínima e máxima;\n3. Clique em 'CALCULAR'.",
 font=("Ubuntu", 9), bg='#111211', fg = '#e0dcd1', relief='raised', bd=9)
label_guide.place(x=635, y=10, height=100, width=345)
l3.config(text = "Idade mínima", font=("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
l4.config(text = "Idade máxima", font=("Ubuntu", 10), bg='#3c403d', fg = '#e0dcd1')
s1.place(x=20, y = 200, height= 160) 
s2.place(x=20, y = 400, height= 160) 
l3.place(x=75, y = 250)
l4.place(x=75, y= 450)  
b1.place(x=350, y= 10)
label_aux = Label(root)
label_aux.config(bg='#111211', fg = '#e0dcd1', bd=9, relief='raised')
label_aux.place(x=180, y=150, height=410, width=800)   
tv1 = ttk.Treeview(label_aux)
treescolly = Scrollbar(label_aux, orient="vertical", command=tv1.yview)
treescrollx = Scrollbar(label_aux, orient="horizontal", command=tv1.xview)

 
root.mainloop() 


# Fontes:
# mudar cor do background do matplotlib https://www.youtube.com/watch?v=8pfgM0QVjhY&ab_channel=GihanPanapitiya
# por o plot no tkinter https://www.youtube.com/watch?v=TiSHudXAMsM&ab_channel=EssentialEngineering
# imagem png rgba https://www.pinpng.com/ https://www.pngwing.com/en/free-png-pgglw
# Criando um executável a partir do script https://www.youtube.com/watch?v=izi1Lw5uLZo&ab_channel=RfZorzi
# Converter pra ico https://www.icoconverter.com/
# mudando foreground color de uma imagem rgba https://onlinepngtools.com/change-png-color
# pegar hexcolor de uma imagem ou gif https://imagecolorpicker.com/en
# editar gif https://ezgif.com/effects
# remover hexcolor (com margem de erro) de um gif https://onlinegiftools.com/remove-gif-background

# TODO: Mudar as cores para as cores azul e laranja que tem na pasta dos wallpapers, (posso usar o site de pegar a hex color)
# TODO: Mudar o estilo do botão pra um mais moderno
# TODO: Se a pessoa apertar em calcular sem antes ter escolhido um arquivo retornar mensagem "Para calcular, primeiro escolha um arquivo válido no botão 'escolher arquivo'"
# TODO: Mostrar um erro quando o usuario escolher um arquivo inválido
# TODO: Completar interpretação das funções. Pensei por exemplo, na interpretação de e_x quando a pessoa coloca um intervalo
# de idades retornar "A expectativa de vida da idade x, x+1, x+2, ..., y" e quando for uma idade exata (idade_min = idade_max)
# retornar "A expectativa de vida à idade exata x é y"
# TODO: Cogitar colocar um gif como esse https://www.google.com/search?q=hourglass+gif&sxsrf=ALiCzsa5PGRWku8TuUeMrRNkBaeYPuoTZg:1663516499365&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjI4Zbw2Z76AhVaGbkGHc2iCVAQ_AUoAXoECAEQAw&biw=1536&bih=714&dpr=1.25#imgrc=hWQL02Q6wRQqmM
# ou nesse (que seria ideal) https://loading.io/spinner/sandglass/ https://prnt.sc/DRftLMIwla7i
# TODO: Cogitar colocar outra cor no background do programa, pensei em nessa cor do tema do dracula e laranja ou rosa
# TODO: Mudar o calculo da última observação de algumas funções biometricas. (pensei em repetir o valor do indice anterior, porque acho q isso nao vai afetar tanto o grafico)
# TODO: Adicionar latex das formulas das funções no label da interpretação
# TODO: Fazer um input no tkinter q pegue a raiz da tabua (l_x) que por padrão está em 10000
# TODO: Adicionar video ao readme explicando como usar
# TODO: Criar opção de exportar arquivo excel (um botão) com a tabela completa