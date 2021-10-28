import json

#best_filds
def multi_match_agg_best(query, fields=['name','languages', 'categories']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"name filter": {
				"terms": {
					"field": "name.keyword",
					"size": 10
				}
			},
			"language filter":{
				"terms": {
					"field": "languages.keyword",
					"size": 10
				}
			},
			"birth_place filter":{
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"date_of_birth filter":{
				"terms": {
					"field": "date_of_birth.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_best(query, sort_num, fields=['name','languages', 'categories']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
		"aggs": {
			"name filter": {
				"terms": {
					"field": "name.keyword",
					"size": 10
				}
			},
			"language filter":{
				"terms": {
					"field": "languages.keyword",
					"size": 10
				}
			},
			"birth_place filter":{
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"date_of_birth filter":{
				"terms": {
					"field": "date_of_birth.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

#cross_filds
def multi_match_agg_cross(query, fields=['name','languages', 'categories']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"name filter": {
				"terms": {
					"field": "name.keyword",
					"size": 10
				}
			},
			"language filter":{
				"terms": {
					"field": "languages.keyword",
					"size": 10
				}
			},
			"birth_place filter":{
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"date_of_birth filter":{
				"terms": {
					"field": "date_of_birth.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_cross(query, sort_num, fields=['name','languages', 'categories']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"name filter": {
				"terms": {
					"field": "name.keyword",
					"size": 10
				}
			},
			"language filter":{
				"terms": {
					"field": "languages.keyword",
					"size": 10
				}
			},
			"birth_place filter":{
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"date_of_birth filter":{
				"terms": {
					"field": "date_of_birth.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q


#phrase_filds
def multi_match_agg_phrase(query, fields=['name','languages', 'categories']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"name filter": {
				"terms": {
					"field": "name.keyword",
					"size": 10
				}
			},
			"language filter":{
				"terms": {
					"field": "languages.keyword",
					"size": 10
				}
			},
			"birth_place filter":{
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"date_of_birth filter":{
				"terms": {
					"field": "date_of_birth.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def multi_match_agg_sort_phrase(query, sort_num, fields=['name','languages', 'categories']):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs": {
			"name filter": {
				"terms": {
					"field": "name.keyword",
					"size": 10
				}
			},
			"language filter":{
				"terms": {
					"field": "languages.keyword",
					"size": 10
				}
			},
			"birth_place filter":{
				"terms": {
					"field": "birth_place.keyword",
					"size": 10
				}
			},
			"date_of_birth filter":{
				"terms": {
					"field": "date_of_birth.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

