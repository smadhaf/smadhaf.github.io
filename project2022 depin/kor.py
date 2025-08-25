
def print_korean_vowel(char):
    vowels = {
        'A': [
            '아 아 아 아 아',
            '아 아 아 아 아',
            '아 아 아 아 아',
            '아 아 아 아 아',
        ],
        'I': [
            '이 이 이 이 이',
            '이 이 이 이 이', 
            '이 이 이 이 이',
            '이 이 이 이 이',
        ],
        'U': [
            '우 우 우 우 우',
            '우 우 우 우 우',
            '우 우 우 우 우',
            '우 우 우 우 우',
        ],
        'E': [
            '에 에 에 에 에',
            '에 에 에 에 에',
            '에 에 에 에 에',
            '에 에 에 에 에',
        ],
        'O': [
            '오 오 오 오 오',
            '오 오 오 오 오',
            '오 오 오 오 오',
            '오 오 오 오 오',
        ]
    }

    if char in vowels:
        for line in vowels[char]:
            print(line)
    else:
        print('Input yang bener woii')


while True:
    input_char = input("Masukkan : ")
    if input_char.lower() == 'q':
        print("Program berhenti.")
        break
    print_korean_vowel(input_char)
    print()  