from roman_numerals import convert

if __name__ == "__main__":
    # 1) Tek haneli Roma sayılarını çevirmek
    print("1) Tek haneli Roma rakamları:")
    print("I =", convert("I"))  # 1
    print("V =", convert("V"))  # 5
    print("X =", convert("X"))  # 10
    print("L =", convert("L"))  # 50
    print("C =", convert("C"))  # 100
    print("D =", convert("D"))  # 500
    print("M =", convert("M"))  # 1000
    print()

    # 2) Toplamalı Roma numaralarını kontrol etmek
    print("2) Toplamalı Roma rakamları:")
    print("II =", convert("II"))  # 2
    print("III =", convert("III"))  # 3
    print("VI =", convert("VI"))  # 6
    print("VII =", convert("VII"))  # 7
    print("XI =", convert("XI"))  # 11
    print("XII =", convert("XII"))  # 12
    print("XIII =", convert("XIII"))  # 13
    print("LX =", convert("LX"))  # 60
    print()

    # 3) Çıkarmalı Roma sayılarını kontrol etmek
    print("3) Çıkarmalı Roma rakamları:")
    print("IV =", convert("IV"))  # 4
    print("IX =", convert("IX"))  # 9
    print("XC =", convert("XC"))  # 90
    print("XL =", convert("XL"))  # 40
    print()

    # 4) Aynı sayıda toplamalı ve çıkarmalı işlemler
    print("4) Hem toplama hem çıkarma işlemleri:")
    print("XLVI =", convert("XLVI"))  # 46
    print("XCVIII =", convert("XCVIII"))  # 98
    print("CDXLVI =", convert("CDXLVI"))  # 446
    print("MCMXCVII =", convert("MCMXCVII"))  # 1997
    print()

    # 5) Yanlış girdileri ele almak
    print("5) Yanlış girdiler:")
    print("A =", convert("A"))  # Geçersiz karakter
    print("B =", convert("B"))  # Geçersiz karakter
    print("E =", convert("E"))  # Geçersiz karakter
    print("F =", convert("F"))  # Geçersiz karakter
    print("G =", convert("G"))  # Geçersiz karakter
    print("H =", convert("H"))  # Geçersiz karakter
    print("IIII =", convert("IIII"))  # Geçersiz Roma rakamı dizisi