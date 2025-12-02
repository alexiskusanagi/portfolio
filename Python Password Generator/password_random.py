import sys
import random

print('Digite 1 para gerar Senha Aleatória de 8 caracteres \nou 0 para Sair')

comando = int(input())

if comando == 0:
    sys.exit()

elif comando == 1:
    
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%¨&*()_+^:><"

    senha = ""

    for char in range(8):
        senha += random.choice(caracteres)
    print(f'Senha Gerada: {senha}')

else :
    print('operação inválida. Fechando sistema')   
    sys.exit() 

"""
1. Gerador de Senhas Seguras
Crie um programa que gera senhas aleatórias com letras, números e símbolos.

Pode incluir opções como tamanho da senha e se deve conter caracteres especiais.

Mostra domínio de strings, randomização e input/output.

📊 2. Calculadora de Despesas Mensais
O usuário informa gastos (alimentação, transporte, lazer etc.).

O programa soma e mostra gráficos simples (usando matplotlib).

Demonstra manipulação de listas/dicionários e visualização de dados.

🎲 3. Jogo da Forca ou Jogo da Velha
Implementar lógica de jogo em texto (terminal).

Pode evoluir para versão com interface simples usando tkinter.

Mostra controle de fluxo, loops e manipulação de strings.

📂 4. Organizador de Arquivos
Script que lê uma pasta e organiza arquivos em subpastas (imagens, PDFs, vídeos etc.).

Usa módulo os e shutil para manipulação de arquivos.

Útil e demonstra automação de tarefas reais.

🌦️ 5. Aplicativo de Previsão do Tempo (API)
Consome uma API gratuita de clima (como OpenWeatherMap).

Usuário digita a cidade e recebe temperatura, umidade e descrição do tempo.

Mostra requisições HTTP (requests) e tratamento de JSON.

🎯 Extra (se quiser impressionar mais)
Conversor de Moedas usando API de câmbio.

Agenda de Tarefas com salvamento em arquivo .json.

Chatbot simples com respostas pré-programadas.

👉 Esses projetos são todos viáveis com Python básico + VS Code, sem necessidade de 
frameworks avançados. Eles mostram que você sabe lidar com entrada/saída, manipulação de dados, 
lógica de programação e integração com bibliotecas simples

"""