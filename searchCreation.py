from elasticsearch import Elasticsearch
# from elasticsearch import Elasticsearch, helpers
# from elasticsearch_dsl import Index
import re
from queryRequestJsonCreation import multi_match_cross, multi_match_phrase
reg = re.compile(r'[a-zA-Z]')

eSearch = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'author-index'

# synonym keywords
synonym_writer = ['ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','ලියන්','ලියූ']
synonym_eng_writer = ['author','write','wrote','writer','written','bookwriter']

synonym_birth_date = ['උපන්දිනය','ජන්ම දිනය','උපන්','උපත ලද','උපත','මෙලොවට','මෙලොව','එළිය','මෙලොවට','ඉපදුන', 'දින']

synonym_birth_place = ['තැන','ස්ථානය','ප්‍රදේශය','ගම','ප්‍රාන්තය', 'පළාත','රට']
synonym_eng_birth_place = ['country', 'village', 'province', 'birth place', 'place', 'place of birth']

synonym_education = ['ඉගෙනුම', 'අධ්‍යාපනය', 'ඉගෙන', 'ශික්ෂා', 'ඉගෙනුම', 'ශික්ෂා']

synonym_languages = ['භාෂාව', 'භාෂා', 'බස', 'බසින්']

synonym_books = ['පොත', 'පොත්', 'ග්‍රන්ථ', 'කවි', 'කවිය']

synonym_list = [ synonym_writer, synonym_eng_writer, synonym_birth_date, synonym_birth_place, synonym_eng_birth_place, synonym_education, synonym_languages, synonym_books]



def search(userQuery):
    tokens = userQuery.split()
    remainderTokens = userQuery.split()
    finalQuery = ""
    keywordFields = []
    finalQueryField = []
    synonymFields = ["name","name_english", "date_of_birth", "birth_place", "birth_place_english","education","languages", "list_of_books"]
    all_fields = ["name","name_english", "date_of_birth","birth_place", "birth_place_english", "education", "languages", "categories", "list_of_books", "description"]

    # remove synonyms from user query
    for word in tokens:
        for i in range(8):
            if word.strip() in synonym_list[i]:
                field = synonymFields[i]
                keywordFields.append(synonymFields[i])
                print(field, 'field added to the SEARCH FIELD LIST for the word', word)
                
                if field == "name" and re.match(reg, userQuery):
                    keywordFields.append(synonymFields[i+1])
                elif field == "name_english" and (not userQuery.isalpha()):
                    keywordFields.append(synonymFields[i-1])
                elif field == "birth_place" and re.match(reg, userQuery):
                    keywordFields.append(synonymFields[i+1])
                elif field == "birth_place_english" and (not userQuery.isalpha()):
                    keywordFields.append(synonymFields[i-1])

                remainderTokens.remove(word)

    # make final query by rest tokens
    if (len(remainderTokens)==0):
        finalQuery = userQuery
    else:
        finalQuery = " ".join(remainderTokens)

    #Boosting
    for field in all_fields:
        if (field in list(set(keywordFields))):
            finalQueryField.append(field+"^5")
        else:
            finalQueryField.append(field)

    # generate query json request
    if(len(keywordFields)==0):
        queryRequestJson = multi_match_cross(finalQuery, all_fields)
    else:
        queryRequestJson = multi_match_phrase(finalQuery, finalQueryField)

    print("\nQuery reqest body :: ",queryRequestJson)
    search_result = eSearch.search(index=INDEX, body=queryRequestJson)
    return search_result





