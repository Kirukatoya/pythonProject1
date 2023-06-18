import math
per_hour = 8
service_channels = 6

service_time = 12
print("xb", per_hour)

# Расчет показателей
# Нагрузка системы
service_intensity = 60/service_time
system_load = per_hour / service_intensity
print("нагрузка системы",system_load)
# Вероятность простоя системы
def calculate_idle_probability(system_load, service_channels):
    idle_probability = 1

    for i in range(service_channels + 1):
        idle_probability += (system_load ** i) / math.factorial(i)

    idle_probability += (system_load ** (service_channels + 1)) / (math.factorial(service_channels) * (service_channels - system_load))

    return 1 / idle_probability
idle_probability = calculate_idle_probability(system_load, service_channels)
print("Веростность простоя системы",float(idle_probability))
# Вероятность образования очереди
poch = ((idle_probability**(service_channels+1)) / math.factorial(service_channels) * (service_channels - idle_probability))
print("Вероятность образования очереди",poch)
        # Средняя длина очереди
avg_queue_length = (service_channels / service_channels - service_intensity) * poch
print("Средняя длина очереди",avg_queue_length)
        # Среднее время ожидания в очереди
avg_waiting_time = avg_queue_length / per_hour
print("Среднее время ожидания в очереди",avg_waiting_time)
        # Среднее число занятых каналолов
avg_number_channels = system_load
print("Число занятых каналов",avg_number_channels)
        # Среднее время прибывания в системе
sistem_time = avg_waiting_time + service_time
print("Среднее время прибывания в системе",sistem_time)