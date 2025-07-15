import time

from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time")
def current_time():
    return f'<turbo-frame id="time"><div id="time">Current time: {time.strftime("%Y-%m-%d %H:%M:%S")}</div></turbo-frame>'


@app.route("/reset-counter")
def counter():
    return "<turbo-frame id='counter'><div id='counter'>Count: 0</div></turbo-frame>"


@app.route("/increment")
def increment():
    count = request.args.get("count", 0, type=int)
    new_count = count + 1
    return f'<turbo-frame id="counter"><div id="counter">Count: {new_count}</div></turbo-frame>'


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f'<turbo-frame id="form-response"><div id="form-response">Form response: {name}</div></turbo-frame>'


@app.route("/add", methods=["POST"])
def get_name():
    app.logger.info(
        "Getting or setting a name, returning a stream and changing content type of response"
    )
    import random

    if request.form.get("name") is not None and request.form.get("name") != "":
        name = request.form.get("name")
    else:
        names = [
            "Alice Cooper",
            "Bob Wilson",
            "Charlie Brown",
            "Diana Prince",
            "Eve Adams",
        ]
        name = random.choice(names)
    turbo = f'<turbo-stream action="prepend" target="guest_list"><template><li>{name}</li></template></turbo-stream>'
    return Response(turbo, mimetype="text/vnd.turbo-stream.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
