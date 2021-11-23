from elasticsearch import Elasticsearch, helpers
# from elasticsearch_dsl import Index
import json,re,os
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'author-index'


def createIndex():
    settings = {
        "settings": {
            "index":{
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis" :{
                "analyzer":{
                    "sinhala-analyzer":{
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter":["edge_ngram_custom_filter"]
                    }
                },
                "filter" : {
                    "edge_ngram_custom_filter":{
                        "type": "edge_ngram",
                        "min_gram" : 2,
                        "max_gram" : 50,
                        "side" : "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                    "name": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "name_english": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "date_of_birth": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "birth_place": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "birth_place_english": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "education": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "languages": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "categories": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "list_of_books": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    },
                    "description": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                    }
            }
        }
    }

    result = client.indices.create(index=INDEX , body =settings)
    print (result)


def read_authors():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file1 = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file1, 'cleaned_authors.json')
    
    with open(my_file,'r',encoding='utf8') as tra_file:
        tra_authors = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(tra_authors) if a not in tra_authors[num + 1:]]
        return results_list


def clean_function(description):
    if (description):
        processed_list = []
        desc_lines = description.split('\n')
        
        for place,s_line in enumerate(desc_lines):
            process_line = re.sub('\s+',' ',s_line)
            punc_process_line = re.sub('[.!?\\-]', '', process_line)
            processed_list.append(punc_process_line)
        
        sen_count = len(processed_list)
        final_processed_list = []
        
        for place,s_line in enumerate(processed_list):
            if (s_line=='' or s_line==' '):
                if (place!= sen_count-1 and (processed_list[place+1]==' ' or processed_list[place+1]=='')) :
                    pass
                else:
                    final_processed_list.append(s_line)
            else:
                final_processed_list.append(s_line)
        final_description = '\n'.join(final_processed_list)
        return final_description
    else:
        return None

def data_generation(authors):  
    for author in authors:

        name = author["name"]
        name_english = author["name_english"]
        description = clean_function(author["description"])
        categories = author["categories"]
        list_of_books = author["list_of_books"]
        date_of_birth = author["date_of_birth"]
        birth_place = author["birth_place"]
        birth_place_english = author["birth_place_english"]
        education = author["education"]
        languages = author["languages"]
        
        yield {
            "_index": INDEX,
            "_source": {
                "name": name,
                "name_english": name_english,
                "date_of_birth": date_of_birth,
                "birth_place": birth_place,
                "birth_place_english": birth_place_english,
                "education": education,
                "languages": languages,
                "categories": categories,
                "list_of_books":list_of_books,
                "description":description
            },
        }


createIndex()
authors = read_authors()
helpers.bulk(client,data_generation(authors))