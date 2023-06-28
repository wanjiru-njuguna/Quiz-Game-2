import Questions
import random


num_of_questions = 3       # Number of questions that we want a player to play in our game

questions = Questions.list_of_questions     # List of questions






# Shuffle our list of questions in a random order
random.shuffle(questions)


num_play_questions = min(num_of_questions, len(questions))
score = 0

# Game loop
for q in range(0, num_play_questions):

   # q = index in the list of questions 'questions'
   # ques_class = one Question class element in the 'questions' list
   ques_class = questions[q]

   print(f"QUESTION {q + 1}: {ques_class.question}")


   #randomize the multiple choice answers by converting the dictionary into a list.
   random_answers = list(ques_class.answers.items())
   random.shuffle(random_answers )

   # Print multiple choice answers
   a = 'A'
   #for answer in ques_class.answers.values():
   answer_numbers=[]
   for k, answer in random_answers:
      answer_numbers.append(k)
      print(f"  {a}: {answer}")
      a = chr(ord(a) + 1)

   # Ask user for their answer
   while True:
      user_answer = input("Your answer: ")
      if len (user_answer) != 1:
         print("Please type one character")
      else:
         user_answer = user_answer.upper()
         if user_answer >= 'A' and user_answer < a:
            break
         else:
            print("Answer out of range!")


   # checking for the correct answer
   
   index_user_answer = ord(user_answer) - ord('A')
   
   key_user_answer = answer_numbers[index_user_answer]

   correct_answer_key = ques_class.correct_answer
   if correct_answer_key == key_user_answer:
      print("You got it!")
      score += 1
   else:
      print("Your answer is incorrect!")

# printing the total scores
print(f" You got {score} out of {num_play_questions} questions right! ")



# End of game - can show the score
print("Game is over")

    





