FILE = 'wlist.txt'

with open(FILE) as txt:

    all_quests = 0
    success = 0
    quiz = txt.read().split("\n")

    for item in quiz:

        if item[0] == 'Q':
            quest = item[2:]
            print(quest+"\n")
            r_ans = 0
            ans_num = 1
            count = quiz.index(item) + 1
            all_quests += 1
            while count < len(quiz) and quiz[count][0] == 'L':
                if quiz[count][2] == '+':
                    r_ans = ans_num
                    ans_text = quiz[count][3:]
                else:
                    ans_text = quiz[count][2:]

                print(f"{ans_num} - {ans_text}")
                ans_num += 1
                count += 1

            ans = int(input(">>> "))
            
            if ans == r_ans:
                success += 1
                print("Success")
            else:
                print("Error!")
            print("\n")
                
    print(f"Quiz over! Success: {success}, Error: {all_quests - success}, All: {all_quests}")