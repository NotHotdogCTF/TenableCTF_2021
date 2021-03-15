import re
'''
:param blob: blob of data to parse through (string)
:param group_name: A single Group name ("Green", "Red", or "Yellow",etc...)

:return: A list of all user names that are part of a given Group
'''
def ParseNamesByGroup(blob, group_name):
	results = []
	dicts = re.findall('(?<=\[).*?(?=\])',blob)
	for element in dicts:
		
		element = '{' + element + '}'
		element = eval(element)
		if(element['Group'] == group_name):
			results.append(element['user_name'])
	return(results)
			
data = raw_input()
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print result_names_list
