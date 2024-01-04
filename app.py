from flask import Flask, render_template, request
import googlesearch
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    x=googlesearch.search(str(query),advanced=True, num_results=20)
    return render_template('result.html', query=query, results=x)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000,)
