import os
os.system("cls")

opc=0
quantT=0
quantC=0
T={}
C={}
total_corrido = 0
corridas = [
    {"nome": "Corrida das Estações", "data": "2024-11-10"},
    {"nome": "Corrida Track & Field - Recife", "data": "2024-12-01"},
    {"nome": "Meia Maratona Agamenon Magalhães", "data": "2024-11-15"},
    {"nome": "Meia Maratona da Cidade", "data": "2025-01-20"},
]

def Fadd():
    if addT_C=="T":
        with open('treinos.txt','a') as arquivotxt:
            try:
                data = input("Digite a data da ocasião (formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (em KM): "))
                tempo = float(input("Digite o tempo de duração (em Horas): "))
                localizacao = input("Digite a localização do lugar: ")
                condicoes_climaticas =input("Digite a condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                T[quantT]=(f"{quantT}º TREINO-> |Data: {data}|Distância: {distancia}Km|Tempo de duração: {tempo}h|Localização: {localizacao}|Condição climática: {condicoes_climaticas}\n")
                arquivotxt.write(T[quantT])
            except ValueError:
                print("Alguma informação digitada é inválida")
    elif addT_C=="C":
        with open('competicoes.txt','a') as arquivotxt:
            try:
                data = input(" Digite a data da ocasião (formato DD-MM-YYYY): ")
                distancia = float(input(" Digite a distância percorrida (em KM): "))
                tempo = float(input(" Digite o tempo de duração (em horas): "))
                localizacao = input(" Digite a localização do lugar: ")
                condicoes_climaticas =input("Digite a condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                C[quantC]=(f"{quantC}ª COMPETIÇÃO-> |Data: {data}|Distância: {distancia}Km|Tempo de duração: {tempo}h|Localização: {localizacao}|Condição climática: {condicoes_climaticas}\n")
                arquivotxt.write(C[quantC])
            except ValueError:
                print("Alguma informação digitada é inválida")

def Fvizu():
    if vizuT_C=="T":
        with open('treinos.txt','r') as arquivotxt:
            for i in arquivotxt:
                print(i)
    elif vizuT_C=="C":
        with open('competicoes.txt','r') as arquivotxt:
            for i in arquivotxt:
                print(i)
    else:
        print("Opção inválida")

def Fupdt():    
    if updtT_C=="T":
        try:
            with open('treinos.txt','r') as arquivotxt:
                numUpdt=int(input("Digite o número do treino que você quer atualizar: "))
                Treino=arquivotxt.readlines()
    
                nova_data = input("Digite a nova data do treino (formato DD-MM-YYYY): ")
                nova_distancia = float(input("Digite a nova distância percorrida (em KM): "))
                novo_tempo = float(input("Digite o novo tempo de duração (em horas): "))
                nova_localizacao = input("Digite a nova localização do lugar: ")
                nova_condicoes_climaticas =input("Digite a nova condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                Treino[numUpdt-1]=(f"{numUpdt}º TREINO-> |Data: {nova_data}|Distância: {nova_distancia}Km|Tempo de duração: {novo_tempo}h|Localização: {nova_localizacao}|Condição climática: {nova_condicoes_climaticas}\n")

            with open('treinos.txt','w') as arquivotxt:
                arquivotxt.writelines(Treino[numUpdt-1])
        except ValueError:
            print("Erro ao atualizar treino")

    elif updtT_C=="C":
        try:
            with open('competicoes.txt','r') as arquivotxt:
                numUpdt=int(input("Digite o número da competição que você quer atualizar: "))
                Competicao=arquivotxt.readlines()
    
                nova_data = input("Digite a nova data da competição (formato DD-MM-YYYY): ")
                nova_distancia = float(input("Digite a nova distância percorrida (em KM): "))
                novo_tempo = float(input("Digite o novo tempo de duração (em Horas): "))
                nova_localizacao = input("Digite a nova localização da competição: ")
                nova_condicoes_climaticas =input("Digite a nova condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                Competicao[numUpdt-1]=(f"{numUpdt}ª COMPETIÇÃO-> |Data: {nova_data}|Distância: {nova_distancia}Km|Tempo de duração: {novo_tempo}h|Localização: {nova_localizacao}|Condição climática: {nova_condicoes_climaticas}\n")

            with open('competicoes.txt','w') as arquivotxt:
                arquivotxt.writelines(Competicao[numUpdt-1])
        except ValueError:
            print("Erro ao atualizar competição")
    
def Fexc():
    if excT_C=="T":

        try:
            with open('treinos.txt','r') as arquivotxt:
                numExc=int(input("Digite o número do registro que você quer excluir: "))
                TreinoExc=arquivotxt.readlines()
                if 1<=numExc<=len(TreinoExc):
                    del TreinoExc[numExc-1]

        except ValueError:
            print("Número inválido")

        with open('treinos.txt','w') as arquivotxt:
            arquivotxt.writelines(TreinoExc)

    elif excT_C=="C":
        try:
            with open('competicoes.txt','r') as arquivotxt:
                numExc=int(input("Digite o número do registro que você quer excluir: "))
                CompExc=arquivotxt.readlines()
                if 1<=numExc<=len(CompExc):
                    del CompExc[numExc-1]

        except ValueError:
            print("Número inválido")

        with open('competicoes.txt','w') as arquivotxt:
            arquivotxt.writelines(CompExc)

print("Digite 1 para fazer um registro")
print("Digite 2 para visualizar os registros")
print("Digite 3 para atualizar os registros")
print("Digite 4 para excluir um registro")
print("Digite 5 para adicionar metas e desafios")
print("Digite 6 para atualizar metas e desafios")
print("Digite 7 para acessar datas das corridas mais proximas")
print("Digite 8 para parar")
while opc!=8:
    opc=int(input("Digite o que você quer fazer: "))
    
    if opc==1:
        print("Digite T para treino \nDigite C para competição")
        addT_C=input("Quer registrar um treino ou uma competição?: ").upper()
        if addT_C=="T":
                quantT+=1
        elif addT_C=="C":
                quantC+=1
        else:
                print("Opção inválida")
        Fadd()
        
    elif opc==2:
        print("Digite T para treino \nDigite C para competição")
        vizuT_C=input("Quer vizualizar os registros dos treinos ou das competições?: ").upper()
        Fvizu()

    elif opc==3:
        print("Digite T para treino \nDigite C para competição")
        updtT_C=input("Quer atualizar os registros dos treinos ou das competições?: ").upper()
        Fupdt()

    elif opc==4:
        print("Digite T para treino \nDigite C para competição")
        excT_C=input("Quer excluir um registro de treino ou de competição?: ").upper()
        Fexc()
    
    elif opc==5:
        def atualizar_progresso(km_corrido, meta_anual, total_corrido):
            total_corrido += km_corrido
            km_restante = meta_anual - total_corrido
            if km_restante > 0:
                print(f"Faltam {km_restante} km para cumprir a meta anual.")
            else:
                print(f"Parabéns, Pedro! Você já atingiu a meta anual com {total_corrido} km percorridos.")
            return total_corrido

            km_jan = float(input("Quantos km você correu em janeiro? "))
            total_corrido = atualizar_progresso(km_jan, meta_anual, total_corrido)

            km_fev = float(input("Quantos km você correu em fevereiro? "))
            total_corrido = atualizar_progresso(km_fev, meta_anual, total_corrido)

            km_mar = float(input("Quantos km você correu em março? "))
            total_corrido = atualizar_progresso(km_mar, meta_anual, total_corrido)

            km_abr = float(input("Quantos km você correu em abril? "))
            total_corrido = atualizar_progresso(km_abr, meta_anual, total_corrido)

            km_maio = float(input("Quantos km você correu em maio? "))
            total_corrido = atualizar_progresso(km_maio, meta_anual, total_corrido)

            km_jun = float(input("Quantos km você correu em junho? "))
            total_corrido = atualizar_progresso(km_jun, meta_anual, total_corrido)

            km_jul = float(input("Quantos km você correu em julho? "))
            total_corrido = atualizar_progresso(km_jul, meta_anual, total_corrido)

            km_ago = float(input("Quantos km você correu em agosto? "))
            total_corrido = atualizar_progresso(km_ago, meta_anual, total_corrido)

            km_set = float(input("Quantos km você correu em setembro? "))
            total_corrido = atualizar_progresso(km_set, meta_anual, total_corrido)

            km_out = float(input("Quantos km você correu em outubro? "))
            total_corrido = atualizar_progresso(km_out, meta_anual, total_corrido)

            km_nov = float(input("Quantos km você correu em novembro? "))
            total_corrido = atualizar_progresso(km_nov, meta_anual, total_corrido)
    
            km_dez = float(input("Quantos km você correu em dezembro? "))
            total_corrido = atualizar_progresso(km_dez, meta_anual, total_corrido)

    elif opc==7 
        def buscar_corrida_mais_proxima(data_inserida):
            corridas_futuras = [corrida for corrida in corridas if corrida["data"] > data_inserida]

            if not corridas_futuras:
                return "Não há corridas a céu aberto após essa data."

            corrida_proxima = min(corridas_futuras, key=lambda x: x["data"])

            return f"A corrida mais próxima é: {corrida_proxima['nome']} na data {corrida_proxima['data']}."

        data_usuario = input("Insira uma data (formato YYYY-MM-DD): ")
        resultado = buscar_corrida_mais_proxima(data_usuario)
        print(resultado)
          
