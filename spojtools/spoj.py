import re
from urllib import request

LIST_SOLVED = 'List of solved classical problems:'
LIST_TODO = 'TODO list of classical problems:'
URL = 'http://www.spoj.com/users/'

REGEX_FORMAT = '<a href="/status/[A-Z][A-Z0-9]+,%s/">[A-Z][A-Z0-9]+</a></td>'

def getSolvedProblems(user):
	"""Returns sorted list of strings consisting of the SPOJ problems the given
	user has solved. If the user doesn't exist, an empty list is returned."""

	spojContent = str(request.urlopen(URL + user).read())

	if LIST_SOLVED not in spojContent:
		return []

	a = spojContent.index(LIST_SOLVED)
	b = spojContent.index(LIST_TODO)
	spojContent = spojContent[a:b]
	
	regex = REGEX_FORMAT % user
	matches = re.findall(regex, spojContent)
	problems = []
	for match in matches:
		m = re.search('[A-Z][A-Z0-9]+', match)
		problems.append(m.group())

	problems.sort()
	return problems

def getSolvedLists(user1, user2):
	"""Returns three sorted lists: s1, s2, and both.
	s1 contains the problems user1 has solved and user2 hasn't.
	s2 contains the problems user2 has solved and user1 hasn't.
	both contains the problems both user1 and user1 have solved ."""

	s1 = set(getSolvedProblems(user1))
	s2 = set(getSolvedProblems(user2))

	uniq1 = [s for s in s1 if s not in s2]
	uniq1.sort()
	
	uniq2 = [s for s in s2 if s not in s1]
	uniq2.sort()

	both = [s for s in s1 if s in s2]
	both.sort()

	return uniq1, uniq2, both