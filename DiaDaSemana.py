from datetime import datetime

# Date String in dd/mm/yyyy HH:MM:SS format
dt_string = "27/07/2023"

# Convert string to datetime object
dt_object = datetime.strptime(dt_string, "%d/%m/%Y")
print(dt_object)
day_of_week = dt_object.weekday()


def diaSemana(day_of_week):
    match day_of_week:
        case 0:
            return "Segunda-feira"
        case 1:
            return "Terça-feira"
        case 2:
            return "Quarta-feira"
        case 3:
            return "Quinta-feira"
        case 4:
            return "Sexta-feira"
        case 5:
            return "Sábado"
        case 6:
            return "Domingo"


diaSem = diaSemana(day_of_week)
print(diaSem)
