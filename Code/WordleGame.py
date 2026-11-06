import random, subprocess

with open("wordlist.txt", "r") as read_wordlist:
    words = read_wordlist.read()
    words = words.split()

print()
print(" ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")

chosen_word = random.choice(words)
written_words = []
for i in range(6):
    answer = [0, 0, 0, 0, 0]
    chosen_word_list = list(chosen_word)
    guess = input("\n Guess word: ")
    while len(guess) != 5:
        guess = input(" Please enter a 5 letter word\n Guess word: ")
    while guess not in words:
        guess = input(" Please enter a valid word (Add it to the list if this is an error)\n Guess word: ")
    if guess == chosen_word:
        print(f"\033[1;49;32m{guess}\033[0m\nYou won!")
        exit()
    for j in range(5):
        if guess[j] == chosen_word[j]:
            answer[j] = 32
            chosen_word_list.remove(chosen_word[j])
    for a in range(5):
        if answer[a] == 0:
            if guess[a] in chosen_word_list:
                answer[a] = 33
                chosen_word_list.remove(guess[a])
            else:
                answer[a] = 31
    subprocess.call("clear")
    append_word = ""
    for b in range(5):
        append_word += f"\033[1;49;{answer[b]}m{guess[b]}\033[0m"
    written_words.append(append_word)
    print()
    print(" ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
    print()
    for c in written_words:
        print("   "+c)
print(f"\nYou lost!\nThe word was: {chosen_word}")
