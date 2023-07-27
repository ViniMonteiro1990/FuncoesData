from datetime import datetime
import calendar

# pega o dia atual
data = datetime.today()
print(data)
ultimoDiaMes = calendar.monthrange(data.year, data.month)
# retorna uma lista, pegar a segunda posição
print(ultimoDiaMes[1])
