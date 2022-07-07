from flask import Flask, render_template, request, jsonify

app = Flask(__name__)



tab_content = [
    {
    "city" : "London",
    "content" : "London is cool."
    },
    {
    "city" : "Rome",
    "content" : "Rome is sweet."
    },
    {
    "city" : "Paris",
    "content" : "Paris is groovy."
    }
]



@app.route("/", methods=['GET', 'POST'])
def home():
    data = list(filter(lambda x: x['city'] == 'London', tab_content))
    if request.method == "POST":
        post_data = request.form.to_dict()
        city_name = post_data['city']
        data = list(filter(lambda x: x['city'] == city_name, tab_content))
        return jsonify(data)
    
    return render_template('index.html', tab_names = tab_content)

if __name__ == "__main__":
    app.run(debug=True)