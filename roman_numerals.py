def convert(roman):
    # Roma rakamları ve karşılık gelen integer değerleri
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Yanlış girdi kontrolü için kurallar
    invalid_combinations = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]

    # Yanlış Roma rakamları kontrolü
    for combo in invalid_combinations:
        if combo in roman:
            return "Geçersiz Roma rakamı dizisi"

    # Geçersiz karakterler kontrolü
    for char in roman:
        if char not in roman_to_int:
            return "Geçersiz karakter"

    # Tek haneli Roma rakamları kontrolü
    if len(roman) == 1:
        return roman_to_int[roman]

    total = 0
    prev_value = 0

    # Roma rakamlarını işlemek
    for char in roman:
        current_value = roman_to_int[char]
        if current_value > prev_value:
            # Çıkarmalı kural
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value

    # 4999 sınırı
    if total > 4999:
        return "Sayı 4999'dan büyük olamaz"

    return total
