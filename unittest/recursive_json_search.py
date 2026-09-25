from policy import POLICY


def json_search(key, input_object, role=None):
	"""Return every value associated with ``key`` in nested JSON data."""
	allowed_roles = POLICY.get(key)
	if role is not None and allowed_roles is not None and role not in allowed_roles:
		return []

	results = []

	if isinstance(input_object, dict):
		if key in input_object:
			results.append(input_object[key])
		for value in input_object.values():
			results.extend(json_search(key, value, role))
	elif isinstance(input_object, list):
		for value in input_object:
			results.extend(json_search(key, value, role))

	return results
