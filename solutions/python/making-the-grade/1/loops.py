"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    result = []

    for grade in student_scores:
        result.append(round(grade))

    return result


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    count = 0

    for grade in student_scores:
        if grade <= 40:
            count += 1 
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    above = []

    for grade in student_scores:
        if grade >= threshold:
            above.append(grade)
        else:
            continue

    return above

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grades_range = []
    lowest = 41
    step = (highest - lowest + 1) / 4 

    for grades in range(lowest, highest, round(step)):
        grades_range.append(grades)

    return grades_range
        


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    result_list = []

    for index, (student_scores, student_names) in enumerate(zip(student_scores, student_names), start = 1):
        result_list.append(f"{index}. {student_names}: {student_scores}")

    return result_list


def perfect_score(student_info):

   
    for info in student_info:
        if info[1] == 100:
            return info
    return []

            
