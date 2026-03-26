# iniciar_o_dia

Automação simples em Python usando **PyAutoGUI** para abrir sites e programas automaticamente no início do dia.

---

## Instalação

1. Criar ambiente virtual (venv)
No terminal, execute:
```bash
python -m venv venv
```

Ative a venv:

Windows (Prompt de Comando):
```bash
venv\Scripts\activate.bat
```

2. Instalar dependências
```bash
pip install -r requirements.txt
```

Executar o projeto
Com a venv ativada, rode:

```bash
python src/iniciar_o_dia.py
```


Criar Executável

Gere o executável:
```bash
pyinstaller --onefile --noconsole  src/iniciar_o_dia.py
```

O arquivo .exe será criado na pasta dist/.
Copie-o para a área de trabalho e renomeie para iniciar_o_dia.exe.



## Estrutura do Projeto

```text
iniciar_o_dia/
├── src/
│   └── iniciar_o_dia.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Principais Comandos PyAutoGUI
Clique: pyautogui.click(x, y)

Duplo clique: pyautogui.doubleClick()

Direito: pyautogui.rightClick()

Digitar texto: pyautogui.write("texto")

Pressionar tecla: pyautogui.press("enter")

Atalho de teclado: pyautogui.hotkey("ctrl", "c")

## Posição do mouse:

python

import pyautogui
print(pyautogui.position())


## Observações
Personalize os sites e programas no arquivo src/iniciar_o_dia.py.

Adicione venv/, dist/ e build/ ao .gitignore para não subir arquivos desnecessários.