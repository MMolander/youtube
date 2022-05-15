# Combine loops and conditionals to classify a
# dictionary of test scores and student ids into a
# data structure grouping passing and failing
# student ids

#dictionary of student_id -> score

student_scores = {
    "1" : 80,
    "2" : 50,
    "3" : 92,
    "4" : 70,
    "5" : 74,
    "6" : 68,
    "7" : 80,
    "8" : 82,
}

MIN_PASSING_GRADE = 70

def is_passing_score(score):
    """Returns True if the score is passing"""
    return score >= MIN_PASSING_GRADE


# pass_fail_dictionary = { "passing": [], "failing": [] }

def build_pass_fail_dictionary(scores):
    """Build dictionary of passing and failing student id lists"""

    # Initialize a dict with passing and failing keys
    # With empty lists for values

    pass_fail_dictionary = {
    "passing": [],
    "failing": [],
}

    # For each student id, look up its corresponding score
    # and evaluate if it is a passing score. If it is passing
    # append to the passing list, otherwise, append to failing
    for student_id in scores:
        if is_passing_score(scores[student_id]):
            pass_fail_dictionary["passing"].append(student_id)
        else:
            pass_fail_dictionary["failing"].append(student_id)

    return pass_fail_dictionary


report = build_pass_fail_dictionary(student_scores)
print(report)