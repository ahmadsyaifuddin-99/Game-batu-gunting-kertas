import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "r" and computer_choice == "s") or (player_choice == "s" and computer_choice == "p") or (player_choice == "p" and computer_choice == "r"):
        return "Player wins"
    else:
        return "Computer wins"

def main():
    print("=== Permainan Batu, Gunting, Kertas ===")
    print("Pilihan: r (rock), p (paper), s (scissors)")
    print("========================================")

    choices = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:
        player_choice = input("Pemain, masukkan pilihan Anda: ").lower()
        if player_choice not in choices:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        computer_choice = random.choice(list(choices.keys()))
        print("Komputer memilih: ", choices[computer_choice])

        result = determine_winner(player_choice, computer_choice)
        print("Hasil: ", result)

        play_again = input("Ingin bermain lagi? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Terima kasih telah bermain!")

if __name__ == '__main__':
    main()
