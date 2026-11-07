import random, subprocess, os

while True:
    print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
    menu_selection = input("1. New Game\n2. Last Game Answer\n3. Add a new word\n4. Remove a word\n5. Clear screen\n6. Exit\n> ")
    if menu_selection == "1":
        subprocess.call("cls" if os.name == "nt" else "clear")
        with open("wordlist.txt", "r") as read_wordlist:
            words = read_wordlist.read()
        print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
        chosen_word = random.choice(words.strip().split())
        written_words = []
        x = 0
        while x < 6:
            answer = [0, 0, 0, 0, 0]
            chosen_word_list = list(chosen_word)
            guess = input("\n Guess word: ")
            while len(guess) != 5:
                guess = input(" Please enter a 5 letter word\n Guess word: ")
            while guess not in words:
                guess = input(" Please enter a valid word (Add it to the list if this is an error)\n Guess word: ")
            if guess == chosen_word:
                input(f"\033[1;49;32m{guess}\033[0m\nYou won!\nPress Enter to return to main menu...")
                break
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
            subprocess.call("cls" if os.name == "nt" else "clear")
            append_word = ""
            for b in range(5):
                append_word += f"\033[1;49;{answer[b]}m{guess[b]}\033[0m"
            written_words.append(append_word)
            print("\n ██╗       ██╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗\n ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝\n ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║██║     █████╗  \n  ████╔═████║ ██║  ██║██╔══██╗██║  ██║██║     ██╔══╝  \n  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝███████╗███████╗\n   ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝\n")
            for c in written_words:
                print("   "+c)
            x += 1
        del words
        if x == 6:
            input(f"\nYou lost!\nThe word was: {chosen_word}\nPress Enter to return to main menu...")
        subprocess.call("cls" if os.name == "nt" else "clear")
    elif menu_selection == "2":
        if "chosen_word" in locals():
            subprocess.call("cls" if os.name == "nt" else "clear")
            print(f"\nThe answer for the last game was: {chosen_word}\n")
        else:
            subprocess.call("cls" if os.name == "nt" else "clear")
            print("\nThere is no last game\n")
    elif menu_selection == "3":
        new_entry = input("Type a 5 letter word to add to the list (you can add more than one by spacing them): ")
        new_entry = new_entry.strip().split()
        entry_isok = True
        for d in new_entry:
            if len(d) != 5:
                entry_isok = False
                new_entry = input("Ensure to type 5 letter words!\nType a 5 letter word to add to the list (you can add more than one by spacing them): ")
        while entry_isok == False:
            for d in new_entry:
                if len(d) != 5:
                    entry_isok = False
                    new_entry = input("Ensure to type 5 letter words!\nType a 5 letter word to add to the list (you can add more than one by spacing them): ")
        subprocess.call("cls" if os.name == "nt" else "clear")
        print("\nAdded:")
        for e in new_entry:
            print(" "+e)
        with open("wordlist.txt", "a") as add_entry_to_wordlist:
            for f in new_entry:
                add_entry_to_wordlist.write(" "+f)
    elif menu_selection == "4":
        del_entry = input("Type a 5 letter word to remove from the list (you can remove more than one by spacing them): ")
        del_entry = del_entry.strip().split()
        entry_isok = True
        for d in del_entry:
            if len(d) != 5:
                entry_isok = False
                del_entry = input("Ensure to type 5 letter words!\nType a 5 letter word to remove from the list (you can remove more than one by spacing them): ")
        while entry_isok == False:
            for d in del_entry:
                if len(d) != 5:
                    entry_isok = False
                    del_entry = input("Ensure to type 5 letter words!\nType a 5 letter word to remove from the list (you can remove more than one by spacing them): ")
        subprocess.call("cls" if os.name == "nt" else "clear")
        print("\nRemoved:")
        for e in del_entry:
            print(" "+e)
        with open("wordlist.txt", "r+") as add_entry_to_wordlist:
            wordlist_content = add_entry_to_wordlist.read()
            for f in del_entry:
                wordlist_content = wordlist_content.replace(f" {f}", "")
            add_entry_to_wordlist.write(wordlist_content)
    elif menu_selection == "5":
        subprocess.call("cls" if os.name == "nt" else "clear")
    elif menu_selection == "6":
        subprocess.call("cls" if os.name == "nt" else "clear")
        break