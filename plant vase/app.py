from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            diameter = float(request.form["diameter"])
            height = float(request.form["height"])

            # Constants
            dowel_thickness = 1.6  # cm

            long_crosspiece = diameter + 2  # little extra room
            short_crosspiece = (long_crosspiece - dowel_thickness) / 2
            legs = height + 4  # elevate a bit

            result = {
                "long_crosspiece": round(long_crosspiece, 1),
                "short_crosspiece": round(short_crosspiece, 1),
                "legs": round(legs, 1)
            }
        except:
            result = "error"

    return render_template("index.html", result=result)
    
if __name__ == "__main__":
    app.run(debug=True)
