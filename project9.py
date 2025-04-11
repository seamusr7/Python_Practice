student_scores = [1,3,24,23,64,78,222,45,34,23,76,11,446]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)