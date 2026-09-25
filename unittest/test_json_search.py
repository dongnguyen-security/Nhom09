import unittest

from recursive_json_search import json_search
from test_data import data, key1


class json_search_test(unittest.TestCase):
	def test_search_found(self):
		"""Find the issue summary nested inside dictionaries and lists."""
		results = json_search(key1, data)

		self.assertIn(
			"Network Device 10.10.20.82 Is Unreachable From Controller",
			results,
		)

	def test_search_not_found(self):
		"""Return an empty list when the requested key is absent."""
		self.assertEqual(json_search("missingKey", data), [])

	def test_is_a_list(self):
		"""Always return a list of matching values."""
		self.assertIsInstance(json_search(key1, data), list)

	def test_unauthorized_viewer_cannot_read_apikey(self):
		"""Prevent a viewer from reading the protected API key."""
		self.assertEqual(json_search("apiKey", data, role="viewer"), [])

	def test_authorized_admin_can_read_apikey(self):
		"""Allow an administrator to read the API key."""
		self.assertEqual(
			json_search("apiKey", data, role="admin"),
			["SNMP-COMMUNITY-STRING-7f3a9c"],
		)

	def test_operator_can_read_management_ip(self):
		"""Allow an operator to read the management IP address."""
		self.assertEqual(
			json_search("managementIpAddress", data, role="operator"),
			["10.10.20.21"],
		)


if __name__ == "__main__":
	unittest.main()
