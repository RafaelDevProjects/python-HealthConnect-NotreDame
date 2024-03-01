from datetime import datetime
import re
import sqlite3
from funcoes import *

def pega_cpf():
    cpf = input("CPF do paciente:")
    while len(cpf) != 11 or not cpf.isdigit() or not validar_cpf(cpf):
        print("CPF inválido. Deve conter 11 dígitos numéricos e ser válido.")
        cpf = input("CPF do paciente:")
    return cpf

def pega_idade():
    idade = verifica_num(input("Idade do paciente:"), "Idade do paciente:",
                             "A idade deve ser cadastrada em números inteiros (1, 10, 55, 80 etc...)")
    return idade

def pega_data_nascimento():
    while True:
        data_nascimento = input("Data de nascimento do paciente DD-MM-YYYY:")
        if verifica_data(data_nascimento):
            return data_nascimento
        else:
            print("Data de nascimento inválida, deve ser preenchida neste formato: DD-MM-YYYY")

def pega_telefone():
    telefone = input("Telefone para contato do paciente ex (dd) 92118-4570:")
    telefone_formatado = verifica_telefone(telefone)
    while telefone_formatado is None:
        telefone = input("Telefone para contato do paciente ex (dd) 92118-4570:")
        telefone_formatado = verifica_telefone(telefone)
    return telefone_formatado

def pega_sexo():
    lista_sexo = ["m", "f"]
    opcao_sexo = input("Sexo do paciente <f/m> :").strip().lower()
    sexo = escolher_opcao(opcao_sexo[0], lista_sexo, "Sexo do paciente:", f"O sexo deve ser uma opção válida ex:{lista_sexo}")
    return sexo


def pega_tipo_sanguineo():
    imprimir_tabela_tipos_sanguineos()
    lista_sangue = ["a-", "a+", "b+", "b-", "ab+", "ab-", "o+", "o-"]
    tipo_sanguineo = escolher_opcao_lista(input("Tipo Sanguíneo do paciente:"), lista_sangue,"Tipo Sanguíneo do paciente:", f"O tipo sanguíneo deve ser uma opção existente ex:{lista_sangue}")


def pega_alergia():
    opcao_alergia = input("O paciente tem alguma alergia?").strip().lower()
    opcao_alergia = escolher_opcao(opcao_alergia[0], ["s", "n"], "O paciente tem alguma alergia?",
                                    "Digite uma resposta válida!")
    if opcao_alergia == "s":
        alergia = input("Qual?")
    else:
        alergia = "vazio"

    return alergia

def pega_doenca_cronica():
    opcao_saude_cronico = input("O paciente tem algum problema de saúde crônico?").strip().lower()
    opcao_saude_cronico = escolher_opcao(opcao_saude_cronico[0], ["s", "n"],"O paciente tem algum problema de saúde crônico?","Digite uma resposta válida!")

    if opcao_saude_cronico == "s":
        saude_cronico = input("Qual?")
    else:
        saude_cronico = "vazio"
    
    return saude_cronico

def pega_prioritario():
    lista_prioritario = ["pcd", "idoso", "gestante"]
    opcao_prioridade = input("O paciente é prioritário?").strip().lower()
    opcao_prioridade = escolher_opcao(opcao_prioridade[0], ["s", "n"],
                                        "O paciente é prioritário?", "Digite uma resposta válida!")
    if opcao_prioridade == "s":
        prioritario = escolher_opcao_lista(input(f"Qual das categorias ({', '.join(lista_prioritario)}): "), lista_prioritario,f"Qual das categorias ({', '.join(lista_prioritario)}):",f'A opção deve ser uma destas: {", ".join(lista_prioritario)}')
    else:
        prioritario = "vazio"

    return prioritario

def pega_exame():
    lista_exames = ["raio-x", "ultrassom", "tomografia", "ressonancia", "ecocardiograma"]
    exame = escolher_opcao_lista(input(f"Exame que deseja realizar ({', '.join(lista_exames)}): "), lista_exames, f"Exame que deseja realizar ({', '.join(lista_exames)}):", "Escolha entre uma das opções apresentadas!")
    