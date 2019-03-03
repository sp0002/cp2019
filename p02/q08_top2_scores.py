# nStudents = int(input("Number of students(At least 2): "))
# if nStudents < 2:
	# nStudents = 2
# name_score = {}
# for i in range(nStudents):
	# name_temp = input("Name of student: ")
	# score_temp = float(input("Score of {}: ".format(name_temp)))
	# name_score[score_temp] = name_temp
# print("Highest score: {}".format(name_score.get(max(name_score.keys()))))
# name_score.pop(max(name_score.keys()))
# print("Second highest score: {}".format(name_score.get(max(name_score.keys()))))
#
#
nStudents = int(input("Number of students(At least 2): "))
if nStudents < 2:
	nStudents = 2
name_top = ""
name_snd = ""
score_top = 0.0
score_snd = 0.00
for i in range(nStudents):
	name_temp = input("Name of student: ")
	score_temp = float(input("Score of {}: ".format(name_temp)))
	if score_temp > score_snd:
		if score_temp > score_top:
			score_snd = score_top
			name_snd = name_top
			score_top = score_temp
			name_top = name_temp
		elif score_temp == score_top:
			score_snd = score_temp
			name_snd = name_temp
		elif score_temp < score_top:
			score_snd = score_temp
			name_snd = name_temp
			
print("Highest score: {}".format(name_top))
print("Second highest score: {}".format(name_snd))