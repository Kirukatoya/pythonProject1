
import math

# запрашиваем параметры у пользователя
arrival_rate = float(input("Введите среднее количество покупателей в час: "))/60
service_time = float(input("Введите среднее время обслуживания в минутах: "))
cashier_count = int(input("Введите среднее количество касс в зоне кассового узла: "))


# интенсивность обслуживания
service_rate = 1 / arrival_rate

# коэффициент загрузки системы
utilization = arrival_rate / (cashier_count * service_rate)

# вероятность простоя системы
p_0 = 1 / (1 + sum([(cashier_count * utilization) ** i / math.factorial(i) for i in range(1, cashier_count + 1)]) + (cashier_count * utilization) ** cashier_count / (math.factorial(cashier_count) * (1 - utilization)))

# средняя длина очереди
q_length = ((cashier_count * utilization) ** (cashier_count + 1) * p_0) / (math.factorial(cashier_count) * (1 - utilization) ** 2)

# среднее время ожидания в очереди
wait_time = q_length / arrival_rate

print(f"Интенсивность потока заявок: {arrival_rate:.3f}")
print(f"Интенсивность обслуживания: {service_rate:.3f}")
print(f"Коэффициент загрузки системы: {utilization:.3f}")
print(f"Вероятность простоя системы: {p_0:.3f}")
print(f"Средняя длина очереди: {q_length:.3f}")
print(f"Среднее время ожидания в очереди: {wait_time:.3f}")



