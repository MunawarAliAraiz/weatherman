import time

def wpm(user_input, elapsed_time):
    words = user_input.split()
    elapsed_time = elapsed_time / 60
    return int(len(words)//elapsed_time)

def matchSentence(user_input, sentence):
    mistake = 0
    try:
        for i in range(len(sentence)):
            if user_input[i] != sentence[i]:
                mistake = mistake + 1
    except:
        mistake = mistake+1
    
    accuracy = len(sentence) - mistake
    accuracy =  accuracy/len(sentence)*100
    return mistake, accuracy

print("\t\t||**** Typing Test ****||")
input('Press Enter to Start....')
time1 = time.time()
sentence = "A Quick Brown Fox Jumps Over the Lazy Dog"
user_input = input(f"{sentence}\nStart Typing from here: ")
time2 = time.time()
elapsed_time = time2-time1
# print(f'Elaspsed Time {elapsed_time}')
mis, acc = matchSentence(user_input, sentence)

print(f"No. of Mistakes: {mis}\nAccuracy: {acc}")
print(f"WPM: {wpm(user_input, elapsed_time)}")


print("Testing Branches in Github1")
print("Testing Branches in Github2")
print("Testing Branches in Github3")

