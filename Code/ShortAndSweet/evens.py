def AreNumbersEven(numbers):
	answers = []
	for number in numbers:
		if(number%2==0):
			answers.append(True)
		else:
			answers.append(False)  
	return answers
# Read space delimited integers from stdin and 
# pass a list of them to AreNumbersEven()
numbers = raw_input()
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print even_odd_boolean_list 
