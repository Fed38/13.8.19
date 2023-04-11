num_tickets = int(input("Введите количество билетов: "))
total_cost = 0
discount = 0

for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        ticket_cost = 0
    elif 18 <= age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390
    total_cost += ticket_cost

if num_tickets > 3:
    discount = total_cost * 0.1
    total_cost -= discount

print("Общая стоимость билетов: ", total_cost, "руб.")
