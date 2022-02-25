if __name__ == "__main__":
    #initialize word database
    answers = open('5.txt','rt')
    words = answers.readlines()
    words_stripped = []
    for word in words:
        word = word.strip('\n')
        words_stripped.append(word)
    
    wordle = [0,0,0,0,0]
    correct_letters = [] #yellow tagged
    solved = False
    while solved == False:
        green = []
        yellow = []
        shortlist = [] #wrong answers
        if len(words_stripped) > 2:
            #ask initial word
            first_word = input("Enter your word: ")
            
            #Check for green flags
            is_green = input("are there green letters? (y/n): ")
            if is_green.upper() == "Y":
                print("Enter which letters are green by entering the letter followed by the index")
                print(f"example:{first_word} {first_word[0]}0 {first_word[3]}3")
                green_letters = input(f"Enter green letters and its index: ")

                green_letters = green_letters.split()
                green = green_letters
                green_to_check = []

                #get entries
                for entry in green_letters:
                    wordle[int(entry[1])] = entry[0]
                    green_to_check.append(entry[0])
                    if entry[0] in correct_letters:
                        correct_letters.remove(entry[0])
                
                #count green letters unlocked
                green_counter = 0
                for letter in wordle:
                    if letter != 0:
                        green_counter += 1
                
                for word in words_stripped:
                    green_count = 0
                    for letter in wordle:
                        if letter != 0:
                            if word[wordle.index(letter)] == letter:
                                green_count += 1
                            
                    if word in words_stripped:
                        if green_count != green_counter:
                            if word not in shortlist:
                                shortlist.append(word)

            #remove shortlist elements from options
            for i in shortlist:
                if i in words_stripped:
                    words_stripped.remove(i)
            print(f"From that information, there are {len(words_stripped)} possible answer/s ")

            #yellow tagged letters
            is_yellow = input("are there yellow letters? (y/n): ")

            #Check for yellow flags
            if is_yellow.upper() == "Y":
                print("Enter which letters are yellow by entering the letter followed by the index")
                print(f"example:{first_word} {first_word[0]}0 {first_word[3]}3")
                yellow_letters = input(f"Enter yellow letters and its index: ")

                #check letters flagged yellow
                yellow_letters = yellow_letters.split()
                yellow = yellow_letters
                for entry in yellow_letters:
                    if entry[0] not in correct_letters:
                        correct_letters.append(entry[0])
                
                #remove words not containing flagged letters
                if len(correct_letters) > 0:
                    for word in words_stripped:
                        for letter in correct_letters:
                            if letter not in word:
                                if word not in shortlist:
                                    shortlist.append(word)
                                    break
                
                #remove words with correct letter/s in the wrong order
                for entry in yellow_letters:
                    for word in words_stripped:
                        if word[int(entry[1])] == entry[0]:
                            if word not in shortlist:
                                shortlist.append(word)

            #remove shortlist elements from options
            for i in shortlist:
                if i in words_stripped:
                    words_stripped.remove(i)
            shortlist.clear()
            print(f"From that information, there are {len(words_stripped)} possible answer/s ")
        
            #remove words with gray letters
            gray_letters = []
            correct_string = ''
            not_gray = yellow + green
            for i in not_gray:
                correct_string += i
            
            for j in first_word:
                if j not in correct_string:
                    gray_letters.append(j)

            for k in gray_letters:
                for word in words_stripped:
                    if k in word:
                        shortlist.append(word)

            for i in shortlist:
                if i in words_stripped:
                    words_stripped.remove(i)
            shortlist.clear()
            print(f"From that information, there are {len(words_stripped)} possible answer/s ")

            if len(words_stripped) <= 15:
                for word in words_stripped:
                    print(word)

        else:
            words_stripped.sort()
            for word in words_stripped:
                print(word)
            solved = True
        
        







    
    

