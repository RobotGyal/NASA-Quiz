# NASA Quiz!

![Image]('pic.jpg')

## Prepare to test your skills in the ultimately short NASA quiz!

## Motivation
This project was made for the purpose of working with python to practice functions, etc. 

## Technologies
* Python

## Code Snippet
```
    print(colors.blink, "\nCorrect: ", len(correct_questions))
    print("Incorrect: ", len(incorrect_questions))

    if len(correct_questions) < 2:
        print(colors.blue, "\nYou put in good effort but try for higher next time!")
    elif len(correct_questions) >= 2 and len(correct_questions) < 5:
        print(colors.blue, "\nNot too shabby!")
    else:
        print(colors.blue, "\nYou are a master at NASA. Good Job Space Cadet!")

```

## How to Use / Installation
* Clone repo to local device git clone https://github.com/RobotGyal/NASA-Quiz.git 
* In command line run `python3 backwards.py'

## Credit
[Spec](https://github.com/Make-School-Courses/CS-1.1-Intro-to-Programming/blob/master/Projects/quizfan.md)