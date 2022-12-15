
def score(word):
    letter_values = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 2: ["D", "G"], 3: ["B", "C", "M", "P"], 4: ["F","H","V","W","Y"], 5: ["K"], 8: ["J", "X"], 10: ["Q","Z"]}
    score_list = []

    # if len(word) < 1:
    #     return 0 
    word_upper = word.upper()
    for character in word_upper:
        for letter_value, letters in letter_values.items():
            for letter in letters:
                if letter == character: 
                    score_list.append(letter_value)
                    # print(score_list)

    word_score = sum(score_list)
    return word_score

print(score(""))