from flask import Flask, render_template, request

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
    "content" : "London is groovy."
    }
]

@app.route("/", methods=['GET', 'POST'])
def home():
    data = list(filter(lambda x: x['city'] == 'London', tab_content))
    if request.method == "POST":
        city_name = request.form['city']
        # post_data = request.form.to_dict()
        # city_name = post_data['city_name']
        data = list(filter(lambda x: x['city'] == city_name, tab_content))
        print(data)
        return render_template('index.html', tab_content = tab_content, tab_details = data)
    return render_template('index.html', tab_content = tab_content, tab_details = data)

if __name__ == "__main__":
    app.run(debug=True)