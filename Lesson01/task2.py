try:
    seconds = int(input("Введите секунды: "))
except ValueError:
    print("Вы ввели не число!")

hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
sec = (seconds - (hours * 3600) - (minutes * 60)) % 60

print(f"{hours}:{minutes}:{sec}")