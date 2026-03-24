from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', "r") as json_file:
        data = json.load(json_file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def get_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')
    if source == 'json':
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
    else:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            products = list(reader)
    if product_id:
        filtered = [p for p in products if str(p.get('id')) == str(product_id)]
        if not filtered:
            return render_template('product_display.html', error='Product not found', products=[])
        products = filtered
    return render_template('product_display.html', products=products, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)