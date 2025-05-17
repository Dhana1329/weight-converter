from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

TO_KG = {
    'kg': 1,
    'lbs': 0.453592,
    'g': 0.001,
    'oz': 0.0283495,
    'st': 6.35029
}

FROM_KG = {
    'kg': 1,
    'lbs': 2.20462,
    'g': 1000,
    'oz': 35.274,
    'st': 0.157473
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    try:
        weight = float(data.get('weight', 0))
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')

        if from_unit not in TO_KG or to_unit not in FROM_KG:
            return jsonify({'error': 'Invalid units'}), 400

        kg = weight * TO_KG[from_unit]
        converted = kg * FROM_KG[to_unit]

        return jsonify({
            'original_weight': weight,
            'from_unit': from_unit,
            'converted_weight': round(converted, 2),
            'to_unit': to_unit
        })

    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
