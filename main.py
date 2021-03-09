# name = input("Enter your name: ")

with open('wlist.txt') as txt:
    quiz = txt.read().split("\n")
    for item in quiz:
        if item[0] == 'Q':
            quest = item[2:]
            print(quest)
            r_ans = 0
            ans_num = 1
            success = 0
            count = quiz.index(item) + 1
            while True:
                if quiz[count][0] == 'L':
                    if quiz[count][2] == '+':
                        r_ans = ans_num
                        ans_text = quiz[count][3:]
                    else:
                        ans_text = quiz[count][2:]

                    print(f"{ans_num} - {ans_text}")
                    ans_num += 1
                else:
                    ans = int(input(">>> "))
                    
                    if ans == r_ans:
                        success += 1
                        print("Правильно, молодец!")
                    else:
                        print("Неправильно!")

                    break
                count += 1