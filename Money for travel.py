#Ощий расход топлива = Расстояние/100*расход топлива
#Цена = Общий расход топлива * цена за литр топлив

consuption_fuel = 0
all_km = 0
price_litr = 0
all_consuption = 0
all_price = 0

consuption_fuel = float(input("Введите расход топлива автомобиля на 100км:"))
all_km = float(input("Введите протяженность пути в км:"))
price_litr = float(input("Введите цену за 1л топлива:"))


if (consuption_fuel >= 0 and all_km >= 0):
    all_consuption = all_km / 100 * consuption_fuel
    all_price = all_consuption * price_litr
    print("Общий расход топлива на путь:", int(all_consuption * 100 / 100), "л.")
    print("Общая сумма затрат", int(all_price * 100 / 100), "руб.")
if (consuption_fuel <= 0 and all_km <= 0):
    print("Ошибка ввода данных. Значения должны быть больше 0 !")