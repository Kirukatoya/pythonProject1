import math
# Получение входных данных от пользователя
avg_customers_per_hour = float(input("Введите среднее количество посетителей автомойки за 1 час: "))
avg_service_time = float(input("Введите среднее время обслуживания одного посетителя (в минутах): "))
avg_service_channels = int(input("Введите среднее количество каналов обслуживания: "))
queue_limit = int(input("Введите ограничение на длину очереди: "))

# Расчет интенсивности обслуживания
service_intensity = 1 / avg_service_time

# Расчет нагрузки системы
system_load = avg_customers_per_hour / service_intensity

# Расчет вероятности простоя системы
if abs(system_load / avg_service_channels) == 1:  # Проверяем, что значения примерно равны
    idle_probability = round(1 - (system_load / (avg_customers_per_hour / avg_service_time)), 2)
else:
    idle_probability = round((1 - (system_load / avg_service_channels)) / (1 - ((system_load / avg_service_channels) ** (queue_limit + 1 - avg_service_channels))), 2)

# Расчет средней длины очереди
avg_queue_length = (idle_probability * (service_intensity ** avg_service_channels) / (math.factorial(avg_service_channels) * ((service_intensity / avg_service_channels) ** (queue_limit + 1 - avg_service_channels)))) / ((1 - (idle_probability * ((service_intensity / avg_service_channels) ** (queue_limit - avg_service_channels + 1)))) + (idle_probability * (service_intensity ** avg_service_channels) / (math.factorial(avg_service_channels) * ((service_intensity / avg_service_channels) ** (queue_limit + 1 - avg_service_channels)))))

# Расчет среднего времени ожидания в очереди
avg_waiting_time = avg_queue_length / avg_customers_per_hour

# Вывод результатов
print("Интенсивность обслуживания: ", service_intensity)
print("Нагрузка системы: ", system_load)
print("Вероятность простоя системы: ", idle_probability * 100, "%")
print("Средняя длина очереди: ", avg_queue_length)
print("Среднее время ожидания в очереди: ", avg_waiting_time, " минут(ы)")

# Делаем рекомендацию по оптимизации
if idle_probability <= 0.13:
    print("Рекомендуется увеличить число каналов обслуживания")
else:
    print("Ре")