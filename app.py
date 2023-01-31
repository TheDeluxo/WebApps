from flask import Flask, render_template, request


app = Flask(__name__)

# @ is called decorator
@app.route('/')
def index():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "World"
    return render_template("index.html", placeholder=name)  # "placeholder" is the variable in the html file
                                                            # "name" is the variable in the py file
    
    
    if __name__ == "__main__":
        app.run(debug=false, host='0.0.0.0')
