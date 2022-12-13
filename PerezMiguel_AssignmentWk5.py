#Program will include a list of four student names. Each student will have three grades--one for the discussion, one for the quiz and one for the programming assignment. 
#Program will also compute the weighted average grade for each student in a group of four students.
#Program will also determine which student has the highest average.
#Program will include a function that accepts the student name, prompts the user for the three grades and computes and returns the average.
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 17, 2022

#----Function----

def get_weighted_scores(name):
    #Weights
    Discussion_W = 0.20
    Quiz_W = 0.50
    Assignment_W = 0.30
    
    #Prompts user for three grades
    discussion_score = float(input(f'{name}, enter your grade for discussion: '))
    quiz_score = float(input(f'{name}, enter your grade for quiz: '))
    assignment_score = float(input(f'{name}, enter your grade for assignment: '))
    
    #Computes and returns the average.
    average = discussion_score * Discussion_W + quiz_score * Quiz_W + assignment_score * Assignment_W
    return average


def main():
    
    #Names of students
    names = ['Madeline Alvarenga', 'Miguel Perez', 'Roseario Sanchez', 'Odalys Saavedra']

    #for loop, that function should be called successively and the name of the student and the student's grade should be displayed.

    highest_score = 0
    top_student_name = ''
    for n in range(len(names)):
        wt_score = get_weighted_scores(names[n])
        print(f'\n{names[n]} weighted score: {wt_score:.2f}\n\n')
        if n == 0 or highest_score < wt_score:
            highest_score = wt_score
            top_student_name = names[n]

    print(f'The student with the highest average is {top_student_name} with : {highest_score:.2f}')


main()
