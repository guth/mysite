from django.test import TestCase

from . import spoj

# TODO: Learn how Python does mocking and mock the remote calls.
class SpojTests(TestCase):
	def test_get_solved_problems_with_results(self):
		problems = spoj.getSolvedProblems("guth")
		self.assertTrue(len(problems) >= 116)
		self.assertIn("CERC07K", problems)

	# TODO: This now throws 404 not found. Update test accordingly.
	# def test_get_solved_problems_with_nonexistent_user(self):
	# 	problems = spoj.getSolvedProblems("abc123ThisUserDoesntExist456")
	# 	self.assertEquals(problems, [])