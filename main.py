from flask import Flask, render_template, request
from searchCreation import search
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def searchApi():
    if request.method == 'GET':
        print ("GET METHOD")
        return render_template('interface.html',init='True')

    if request.method == 'POST':
        print ("POST METHOD")
        userQuery = request.form['searchTerm']
        print("\nuser Query  ::", userQuery,'\n') 

        search_result = search(userQuery)
        print ("\nresponse for user query :: \n",search_result)

        hits_result = search_result['hits']['hits']
        resultsCount = len(hits_result)

        return render_template('interface.html',query=userQuery, hits=hits_result,resultCount=resultsCount)


if __name__ == "__main__":
    app.run(debug=True)