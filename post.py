from flask import Flask, jsonify, request
app = Flask(__name__)
Diary = [
    {
        "id": 1,
        "Title": "Swimming",
        "Description": "This is so goood",
        "Time": "2:00-3:00"
    },
    {
        "id": 2,
        "Title": "Reading",
        "Description": "I shall have to read the physics book.",
        "Time": "3:00-7:00"
    }
]


# Adding an entry
@app.route('/diary/api/v1/entry', methods=['POST'])
def add_entry():
    entry = {
        "id": Diary[-1]["id"] + 1,
        "Title": request.json['Title'],
        "Description": request.json['Description'],
        "Time": request.json['Time']
    }
    Diary.append(entry)
    # 201 is a status code showing success
    return jsonify({"My_diary": Diary}), 201


if __name__ == '__main__':
    app.run(debug=True)
