from Flask import flask, app

@app.route('/')
def main():
    context = {
        'name' : name,
        'age' : age,
    }
    return render_template(home.html, name=name, age=age)

def render_template():
    return 