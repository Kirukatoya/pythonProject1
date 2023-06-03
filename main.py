

#import math
# функция расчета интенсивности обслуживания
def service_intensity(service_rate, num_of_channels):
    return service_rate * num_of_channels

# функция расчета интенсивности потока
def arrival_intensity(arrival_rate):
    return arrival_rate

# функция расчета нагрузки системы
def system_load(arrival_rate, service_rate, num_of_channels):
    return arrival_rate / (service_rate * num_of_channels)

# функция расчета вероятности простоя системы
def idle_probability(arrival_rate, service_rate, num_of_channels):
    rho = system_load(arrival_rate, service_rate, num_of_channels)
    return min((1 - rho) ** num_of_channels, 1)

# функция расчета средней длины очереди
def avg_queue_length(arrival_rate, service_rate, num_of_channels):
    rho = system_load(arrival_rate, service_rate, num_of_channels)
    return (rho ** (num_of_channels + 1)) / (num_of_channels * math.factorial(num_of_channels) * (1 - rho))

# функция расчета среднего времени ожидания
def avg_waiting_time(arrival_rate, service_rate, num_of_channels):
    rho = system_load(arrival_rate, service_rate, num_of_channels)
    return avg_queue_length(arrival_rate, service_rate, num_of_channels) / (arrival_rate * (1 - idle_probability(arrival_rate, service_rate, num_of_channels)))

# пользовательский ввод
arrival_rate = float(input("Введите интенсивность потока: "))
num_of_channels = int(input("Введите количество каналов обслуживания: "))
queue_limit = int(input("Введите ограничение на длину очереди: "))

# расчет интенсивности обслуживания
service_rate = arrival_rate / (system_load(arrival_rate, 1, num_of_channels) * num_of_channels)

# расчеты
intensity_of_service = service_intensity(service_rate, num_of_channels)
intensity_of_arrivals = arrival_intensity(arrival_rate)
system_loading = system_load(arrival_rate, service_rate, num_of_channels)
idle_probability_of_system = idle_probability(arrival_rate, service_rate, num_of_channels)
average_queue_length = avg_queue_length(arrival_rate, service_rate, num_of_channels)
average_waiting_time = avg_waiting_time(arrival_rate, service_rate, num_of_channels)

# вывод результатов
print("Интенсивность обслуживания: ", intensity_of_service)
print("Интенсивность потока: ", intensity_of_arrivals)
print("Нагрузка системы: ", system_loading)
print("Вероятность простоя системы: ", idle_probability_of_system)
print("Средняя длина очереди: ", average_queue_length)
print("Среднее время ожидания: ", average_waiting_time)

# рекомендации по оптимизации
if idle_probability >0.13:
    print("Рекомендуется увеличить количество каналов обслуживания.")
else:
    print("Рекомендуется сократить количество к")