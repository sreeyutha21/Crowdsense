from flask import Flask, render_template, jsonify, request

app = Flask(_name_)

# Manually controlled crowd values
crowd_data = {
    "Zone A": 50,
    "Zone B": 50,
    "Zone C": 50
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(crowd_data)

@app.route('/set-data', methods=['POST'])
def set_data():
    global crowd_data
    new_data = request.get_json()
    for zone in crowd_data:
        if zone in new_data:
            crowd_data[zone] = int(new_data[zone])
    return jsonify({"status": "updated"})

if _name_ == '_main_':
    app.run(debug=True)