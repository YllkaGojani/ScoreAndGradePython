def scoreAndGrade():
	for i in range (0, 10):
		score = input('Your score:')	
		if(score >= 60) and (score <= 69):
			grade= 'D'
			print 'Score:',score,';Your grade is:',grade
		elif(score >69) and (score <= 79):
			grade = 'C'
			print 'Score:',score,';Your grade is:',grade
		elif(score >79) and (score <= 89):
			grade = 'B'
			print 'Score:',score,';Your grade is:',grade
		elif(score >89) and (score <= 100):
			grade = 'A'
			print 'Score:',score,';Your grade is:',grade
		else:
			grade = 'undefined'
			print 'Score:',score,';Your grade is:',grade
	print 'End of the program. Bye!'		


scoreAndGrade()
#Nice work on catching any scores outside of the range 60 - 100... grade = 'undefined'!
