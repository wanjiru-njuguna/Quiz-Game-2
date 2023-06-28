# Questions for the game





class Question:
  def __init__(self, _question, _answers, _answer):
    self.question = _question        # Question itself
    self.answers = _answers          # Dictionary of answers: key=unique int, value=multiple-choice answer as a string
    self.correct_answer = _answer    # Key in 'answers' that is the correct answer







list_of_questions = [
    
    Question("What is the smallest country in the world?", 
           {
             0:"USA", 
             1:"Zimbabwe", 
             2:"Vatican", 
             3:"Russia",
             4:"Poland",
           },
           2
           ),

    Question("What is the largest country in Africa by area?", 
            {

             0:"Algeria",
             1:"Ghana",
             2:"Nigeria",
             5:"Kenya",
            },
            0
            ),

    Question("What is the smallest country in Africa by area?",
            {
             0:"Burundi",
             1:"Somalia",
             2:"Seychelles",
             3:"Rwanda",
            },
            2
            ),
    Question("What is the name of the continent's largest lake?",
             {
               0:"Lake victoria",
               1:"Lake Nakuru",
               2:"Lake Naivasha",
               3:"Lake olborosat",
             },
             0
             ),
    Question("What is the longest river in Africa?",
            {
                0:"Nile",
                1:"Tana",
                2:"Delta",
                3:"Congo",

            },
            0
            ),
    Question("What is the highest mountain in Africa?",
             {
               0:"Mt. Kilimanjaro",
               1:"Mt. Kenya",
               2:"Mt. Elgon"
             },
             0
             ),


  



  
    

  ]



