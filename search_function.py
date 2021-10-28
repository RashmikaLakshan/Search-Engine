from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
import advanced_queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
# INDEX = 'song-index'
INDEX = 'author-index'
sinhala_popularity = []
# sinhala_popularity=['හොඳම','හොදම','ප්‍රචලිත','ප්‍රසිද්ධ','ජනප්‍රිය','ජනප්‍රියම']
# english_popularity=['best','famous','top','most famous','toopest']

# synonym_artist = ['ගායකයා','ගයනවා','ගායනා','ගායනා','ගැයු','ගයන','ගයපු']
# synonym_eng_artist = ['sing', 'artist','singer','sung','sang']

synonym_writer = ['ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','ලියන්','ලියූ']
# synonym_eng_writer = ['lyricist','write','wrote','writer','songwriter','written']
# synonym_eng_writer = ['author','write','wrote','writer','written','bookwriter']

# synonym_music = ['සංගීත','සංගීතවත්','සංගීතය']
# synonym_eng_music = ['composer','music','composed','compose','musician']

synonym_birth_date = ['උපන්දිනය','ජන්ම දිනය','උපන්','උපත ලද','උපත','මෙලොවට ආ','මෙලොව එළිය දුන්','එළිය දුටු','මෙලොවට','ඉපදුන', 'වන දින']
# synonym_eng_birth_date = ['date of birth','birthday','date','birth']

synonym_birth_place = ['තැන','ස්ථානය','ප්‍රදේශය','ගම','ප්‍රාන්තය', 'පළාත','රට']
# synonym_eng_birth_place = ['country', 'village', 'province', 'birth place', 'place', 'place of birth']

synonym_education = ['ඉගෙනුම ලැබූ', 'අධ්‍යාපනය', 'ඉගෙන ගත්ත', 'ශික්ෂා ලැබූ', 'ඉගෙනුම', 'ශික්ෂා']

synonym_languages = ['භාෂාව', 'භාෂා', 'බස', 'බසින්']



synonym_list = [ synonym_writer, synonym_birth_date, synonym_birth_place, synonym_education, synonym_languages]



def search(search_query):
    processed_query = ""
    tokens = search_query.split()
    processed_tokens = search_query.split()
    search_fields = []
    sort_num = 0
    field_list = ["name","date_of_birth", "birth_place","education","languages" ]
    all_fields = ["name","date_of_birth","birth_place", "education", "languages", "categories", "list_of_books", "description"]
    final_fields = []

    for word in tokens:
        print (word)

        if (word in sinhala_popularity):
            processed_tokens.remove(word)
            print('Start sort by views')
            sort_num = 986

        if word.isdigit():
            sort_num = int(word)
            processed_tokens.remove(word)
            print ('Identified sort number',sort_num)

        for i in range(0, 5):
            if word in synonym_list[i]:
                print('Adding field', field_list[i], 'for ', word, 'search field list')
                search_fields.append(field_list[i])
                # if(i%2==0):
                #     search_fields.append(field_list[i+1])
                # else:
                #     search_fields.append(field_list[i -1])
                search_fields.append(field_list[i])
                processed_tokens.remove(word)

    if (len(processed_tokens)==0):
        processed_query = search_query
    else:
        processed_query = " ".join(processed_tokens)

    ###Boosting
    # for field in all_fields:
    #     if (field in search_fields):
    #         final_fields.append(field+"^5")
    #     else:
    #         final_fields.append(field)
    final_fields = search_fields

    if (sort_num==0):
        print('Faceted Query')
        if(len(search_fields)==0):
            query_es = advanced_queries.multi_match_agg_cross(processed_query, all_fields)
        elif (len(search_fields) == 2):
            query_es = advanced_queries.multi_match_agg_phrase(processed_query, all_fields)
        else:
            query_es = advanced_queries.multi_match_agg_cross(processed_query, final_fields)

    else:
        print('Range Query')
        if (len(search_fields) == 0):
            query_es = advanced_queries.multi_match_agg_sort_cross(processed_query, sort_num, all_fields)
        elif (len(search_fields) == 2):
            query_es = advanced_queries.multi_match_agg_sort_phrase(processed_query, sort_num, all_fields)
        else:
            query_es = advanced_queries.multi_match_agg_sort_cross(processed_query, sort_num, final_fields)

    print("QUERY BODY")
    print(query_es)
    search_result = client.search(index=INDEX, body=query_es)
    return search_result





