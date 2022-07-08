from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


tab_content = [
    {
        "city": "London",
        "content": "London is cool."
    },
    {
        "city": "Rome",
        "content": "Rome is sweet."
    },
    {
        "city": "Paris",
        "content": "Paris is groovy."
    }
]


@app.route("/", methods=['GET', 'POST'])
def home():
    data = list(filter(lambda x: x['city'] == 'London', tab_content))
    if request.method == "POST":
        data = request.form.to_dict()
        if 'city' in data:
            city_name = data['city']
            data = list(filter(lambda x: x['city'] == city_name, tab_content))
            return jsonify(data)
        elif 'content' in data:
            open_city_tab = data['open_city_tab']
            city_content = data['content']
            for item in tab_content:
                if item['city'] == open_city_tab:
                    item['content'] = city_content
            data = list(
                filter(lambda x: x['city'] == open_city_tab, tab_content))
            return jsonify(data)

    return render_template('index.html', tab_names=tab_content)


if __name__ == "__main__":
    app.run(debug=True)
