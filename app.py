import time

from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time")
def current_time():
    return render_template(
        "partials/time.html", current_time=time.strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/reset-counter")
def counter():
    return render_template("partials/counter.html", count=0)


@app.route("/increment")
def increment():
    count = request.args.get("count", 0, type=int)
    new_count = count + 1
    return render_template("partials/counter.html", count=new_count)


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
    turbo = render_template("partials/turbo_stream.html", name=name)
    return Response(turbo, mimetype="text/vnd.turbo-stream.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
