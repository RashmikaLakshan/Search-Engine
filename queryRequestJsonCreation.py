import json

#cross_filds
def multi_match_cross(query, fields=['name','languages', 'categories']):
	print("\nuse multi match cross fields function for generate search request")
	request = {
		"size": 103,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		}
	}

	requestJson = json.dumps(request)
	return requestJson


#phrase_filds
def multi_match_phrase(query, fields=['name','languages', 'categories']):
	print("\nuse multi match phrase prefix function for generate search request")
	request = {
		"size": 103,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "phrase_prefix"
			}
		}
	}

	requestJson = json.dumps(request)
	return requestJson
