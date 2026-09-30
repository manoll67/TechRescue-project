budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
video_cards_price = video_cards * 250
processors_price = processors * (video_cards_price * 0.35)
ram_price = ram * (video_cards_price * 0.10)

total_price = video_cards_price + processors_price + ram_price

if video_cards > processors:
    total_price *= 0.85
if total_price <= budget:
    print(f'You have {budget - total_price:.2f} leva left!')
else:    print(f'Not enough money! You need {total_price - budget:.2f} leva more!') 


