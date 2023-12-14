# Mencetak header/judul "SEVEN SEGMENT DISPLAY" dan identitas saya
print("\n(❁´◡`❁) SEVEN SEGMENT DISPLAY (❁´◡`❁)")
print("Name     : FIRLIANY FIRDAUS")
print("NIM      : D121231077")
print("Class    : B_Informatika\n")

# Definisikan beberapa kode warna ANSI escape sequence untuk digunakan dalam terminal
COLOR_WHITE = "\033[1;37m"
COLOR_GREEN = "\033[1;92m"
COLOR_YELLOW = "\033[1;33m"
COLOR_RESET = "\033[0m"

# Pola segmen: 1 (segmen menyala), 0 (segmen mati)
def Decimal_to_Binary(decimal):
    return bin(decimal)[2:] #Mengonversi angka desimal ke biner menggunakan fungsi 'bin()'

#daftar 2D yang mewakili tampilan SevenSegment
def Decimal_to_SevenSegment(decimal):
    segment = [
        [1, 1, 1, 0, 1, 1, 1],  # 0
        [0, 0, 1, 0, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 0, 1],  # 2
        [1, 0, 1, 1, 0, 1, 1],  # 3
        [0, 1, 1, 1, 0, 1, 0],  # 4
        [1, 1, 0, 1, 0, 1, 1],  # 5
        [1, 1, 0, 1, 1, 1, 1],  # 6
        [1, 0, 1, 0, 0, 1, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1]   # 9
    ]
    return segment[decimal]

# Menampilkan/mencetak tebal angka desimal, biner, dan seven segmen dengan nama segmen (a, b, c, d, e, f, g) dan nilai setiap segmen (1/0)
def Draw_Table(decimal, binary, seven_segment):
    print(f"\nAngka Desimal: {COLOR_WHITE}{decimal}{COLOR_RESET}")
    print(f"Bilangan Biner: {COLOR_WHITE}{binary}{COLOR_RESET}")
    print(f"Seven Segment : {COLOR_WHITE}{seven_segment}{COLOR_RESET}")

# Menampilkan tampilan karakter ASCII Seven-Segment 
def Print_SevenSegment(Segment):
    horizontal = f"{COLOR_GREEN}#####{COLOR_YELLOW}\n" #baris
    vertical = f"{COLOR_GREEN}!! {COLOR_YELLOW}"    #kolom

    for i in range(len(Segment)):
        if i % 3 == 0 or i == 0:
            if Segment[i] == 1:
                print(horizontal, end="")
            else:
                print()
        else:
            if Segment[i] == 1:
                print(vertical, end="")
            else:
                print("   ", end="")
            if i == 2 or i == 5:
                print()

Exit = False  # Membuat loop utama untuk meminta input pengguna dan menampilkan tampilan seven segment dengan angka yang dimasukkan
while not Exit:
    F = int(input("Masukkan angka (0-9): "))
    if 0 <= F < 10:
        Segment = Decimal_to_SevenSegment(F)
        print(f"\n{COLOR_YELLOW}Tampilan seven segment dari {F} :{COLOR_RESET}\n")
        Print_SevenSegment(Segment)
        Draw_Table(F, Decimal_to_Binary(F), Segment)
    else:
        Exit = True
        print("\nRentang angka (0-9)\n")
