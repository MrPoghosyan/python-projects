import csv
import random

# Класс для представления человека
class Person:
    def __init__(self, name, flowers):
        self.name = name        # Имя человека
        self.flowers = flowers  # Количество цветов (дней полива)

# Класс для работы с CSV файлами
class CSVHandler:
    @staticmethod
    def read_flower_data(filename):
        people = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                person = Person(row['name'], int(row['flowers']))
                people.append(person)
        return people

    @staticmethod
    def write_queue(filename, queue):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['day', 'person'])  # Заголовки
            for day, person in enumerate(queue, start=1):
                writer.writerow([day, person])

# Класс для генерации очереди
class QueueGenerator:
    def __init__(self, people):
        self.people = people  # Список объектов Person
        self.total_days = sum(person.flowers for person in people)  # Общее количество дней

    # Проверка на наличие последовательных дней в общей очереди
    def has_consecutive_days(self, queue):
        for i in range(1, len(queue)):
            if queue[i] == queue[i - 1] and queue[i] is not None:
                return True
        return False

    # Генерация случайной очереди без последовательных дней
    def generate_queue(self):
        queue = [None] * self.total_days  # Инициализация списка с днями
        all_days = list(range(1, self.total_days + 1))  # Список всех дней

        for person in self.people:
            assigned_days = []
            while True:
                # Выбираем случайные уникальные дни для каждого человека
                assigned_days = random.sample(all_days, person.flowers)
                assigned_days.sort()

                # Проверяем, что у человека не будет последовательных дней
                has_consecutive = any(assigned_days[i] - assigned_days[i - 1] == 1 for i in range(1, len(assigned_days)))
                if not has_consecutive:
                    # Временная очередь с текущим распределением
                    temp_queue = queue[:]
                    for day in assigned_days:
                        temp_queue[day - 1] = person.name

                    # Проверяем, есть ли последовательные дни в общей очереди
                    if not self.has_consecutive_days(temp_queue):
                        break

            # Заполняем выбранные дни именем человека
            for day in assigned_days:
                queue[day - 1] = person.name

            # Убираем использованные дни из списка доступных
            all_days = [day for day in all_days if day not in assigned_days]

        return queue

# Основная программа
def main():
    # Чтение данных из файла
    csv_handler = CSVHandler()
    people = csv_handler.read_flower_data('file.csv')

    # Генерация очереди
    queue_generator = QueueGenerator(people)
    queue = queue_generator.generate_queue()

    # Запись результата в файл
    csv_handler.write_queue('queue.csv', queue)

if __name__ == '__main__':
    main()

