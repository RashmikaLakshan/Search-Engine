import json, os

def __CleaningnUpdatingData(author_file, cleaned_authors_file):

   with open(author_file, encoding='utf-8') as f:
      data = json.load(f)

   cleanedData = []
   for i,obj in enumerate(data['Authors']):

      cleanedObj = {
         "name": obj["name"].strip() if ("name" in obj.keys()) else '',
         "name_english": obj["name_english"].strip() if ("name_english" in obj.keys()) else '',
         "date_of_birth": obj["date_of_birth"].strip() if ("date_of_birth" in obj.keys()) else '',
         "birth_place": obj["birth_place"].strip() if ("birth_place" in obj.keys()) else '',
         "birth_place_english": obj["birth_place_english"].strip() if ("birth_place_english" in obj.keys()) else '',
         "education": list(map(str.strip, obj["education"].strip().split(','))) if ("education" in obj.keys()) else '',
         "languages": list(map(str.strip, obj["languages"].strip().split(','))) if ("languages" in obj.keys()) else '',
         "categories": list(map(str.strip, obj["categories"].strip().split(','))) if ("categories" in obj.keys()) else '',
         "list_of_books": list(map(str.strip, obj["list_of_books"].strip().split(','))) if ("list_of_books" in obj.keys()) else '',
         "description":  obj["description"].strip() if ("description" in obj.keys()) else ''
      }

      cleanedData.append(cleanedObj)

   with open(cleaned_authors_file, 'w', encoding='utf-8') as jsonf:
            json.dump(cleanedData,jsonf, indent=4 , ensure_ascii=False)




THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
author_file = os.path.join(THIS_FOLDER, 'authors.json')
cleaned_authors_file = os.path.join(THIS_FOLDER, 'cleaned_authors.json')

__CleaningnUpdatingData(author_file, cleaned_authors_file)
