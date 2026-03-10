from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = '/Users/carol/Desktop/ai_class_db/pharma.db'

def query_db(query, args=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    results = cursor.fetchall()
    conn.close()
    return [dict(row) for row in results]

@app.route('/')
def index():
    drugs = query_db('SELECT * FROM drugs')
    years = query_db('SELECT DISTINCT year FROM time_periods ORDER BY year')
    return render_template('index.html', drugs=drugs, years=years)

@app.route('/api/sales')
def get_sales():
    drug_id = request.args.get('drug_id', '')
    year = request.args.get('year', '')
    month = request.args.get('month', '')
    hour = request.args.get('hour', '')
    weekday = request.args.get('weekday', '')
    normalized = request.args.get('normalized', 'false')

    value_col = 'units_sold_normalized' if normalized == 'true' else 'units_sold'

    query = f'''
        SELECT 
            t.datum, t.year, t.month, t.hour, t.weekday,
            d.drug_code, d.drug_category,
            s.{value_col} as units_sold
        FROM sales s
        JOIN time_periods t ON s.period_id = t.period_id
        JOIN drugs d ON s.drug_id = d.drug_id
        WHERE 1=1
    '''
    args = []

    if drug_id:
        query += ' AND s.drug_id = ?'
        args.append(drug_id)
    if year:
        query += ' AND t.year = ?'
        args.append(year)
    if month:
        query += ' AND t.month = ?'
        args.append(month)
    if hour:
        query += ' AND t.hour = ?'
        args.append(hour)
    if weekday:
        query += ' AND t.weekday = ?'
        args.append(weekday)

    query += ' LIMIT 500'

    results = query_db(query, args)
    return jsonify(results)

@app.route('/api/summary')
def get_summary():
    summary = query_db('''
        SELECT 
            d.drug_code,
            d.drug_category,
            ROUND(SUM(s.units_sold), 2) as total_sales,
            ROUND(AVG(s.units_sold), 4) as avg_sales,
            ROUND(MAX(s.units_sold), 2) as max_sales
        FROM sales s
        JOIN drugs d ON s.drug_id = d.drug_id
        GROUP BY d.drug_id
        ORDER BY total_sales DESC
    ''')
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)