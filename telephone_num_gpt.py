import re

def normalize_phone_number(phone):
    # Удаляем все символы, кроме цифр и '+'
    cleaned_phone = re.sub(r'[^0-9+]', '', phone)
    
    # Если номер начинается с '8', заменяем его на '+7'
    if cleaned_phone.startswith('8'):
        cleaned_phone = '+7' + cleaned_phone[1:]
    
    # Если код не указан, считаем его равным 495
    if len(cleaned_phone) == 7:
        cleaned_phone = '+7495' + cleaned_phone
    
    return cleaned_phone

def main():
    # Ввод данных
    new_number = normalize_phone_number(input())
    existing_numbers = [normalize_phone_number(input()) for _ in range(3)]
    
    # Проверка на совпадение и вывод результатов
    for number in existing_numbers:
        if new_number == number:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
