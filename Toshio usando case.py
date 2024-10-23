mes=int(input('Qual Mês você nasceu (1-12)'))
match mes:
    case 1:
        mes_extenso = "Janeiro"
    case 2:
        mes_extenso = "Fevereiro"
    case 3:
        mes_extenso = "Março"
    case 4:
        mes_extenso = "Abril"
    case 5:
        mes_extenso = "Maio"
    case 6:
        mes_extenso = "Junho"
    case 7:
        mes_extenso = "Julho"
    case 8:
        mes_extenso = "Agosto"
    case 9:
        mes_extenso = "Setembro"
    case 10:
        mes_extenso = "Outubro"
    case 11:
        mes_extenso = "Novembro"
    case 12:
        mes_extenso = "Dezembro"
    case _:
        mes_extenso = "Número inválido. Deve ser entre 1 e 12."


print(mes_extenso)
