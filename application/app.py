from flask import Flask, request, render_template, jsonify


from material_processing import extract_noun_chunks

# Create a Flask application
app = Flask(__name__)


# Define a route and its handler
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    jsonData = extract_noun_chunks(data["query"])
    return {"data": jsonData}


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
