from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    students = [
    {"id": 1, "name": "Aarav", "marks": 95},
    {"id": 2, "name": "Diya", "marks": 72},
    {"id": 3, "name": "Karan", "marks": 45}
]
    return render_template("home.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)

