from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('data.csv')
import pandas as pd

# Load the dataset
df = pd.read_csv('data.csv')


# Now you can use the filled 'Brand Name' column for your further processing


@app.route('/')
def index():
    # Pass the unique brand names directly to the template
    brand_counts = {
        'Samsung': 621,
        'Apple': 312,
        'Blu': 291,
        'Lg': 270,
        'Nokia': 219,
        'Htc': 189,
        'Motorola': 189,
        'Sony': 183,
        'Blackberry': 159,
        'Huawei': 102,
        'Posh mobile': 54,
        'Indigi': 49,
        'Plum': 42,
        'Otterbox': 40,
        'Juning': 39,
        'Asus': 38,
        'Zte': 36,
        'Sky devices': 34,
        'Lenovo': 33,
        'Verykool': 33
    }
    # Get unique brand names
    brand_names = list(brand_counts.keys())
    return render_template('index.html', brands=brand_names)

@app.route('/products', methods=['POST'])
def products():
    # Get the selected brand name from the form
    selected_brand = request.form['brand']
    df['Score'] = df['Score'].round(3)
    # Filter dataset based on the selected brand
    brand_products = df[(df['Brand Name'] == selected_brand)]

    # Sort the filtered data by 'PS' and 'Score' columns
    sorted_products = brand_products.sort_values(by=['PS', 'Score'], ascending=False)

    # Get top 15 products
    top_15_products = sorted_products.head(15)

    # Render the template with the top 15 products
    return render_template('products.html', products=top_15_products)

@app.route('/getTopProducts', methods=['POST'])
def getTopProducts():
    # Get the specified PS from the form data
    ps = int(request.form['PS'])
    df['Score'] = df['Score'].round(3)
    # Filter dataset based on the specified PS
    filtered_products = df[(df['PS'] == ps)]
    # Sort the filtered data by 'PS' column and get top 15 products
    top_15_products = filtered_products.sort_values(by='Score', ascending=False).head(15)

    # Render the template with the top 15 products
    return render_template('product.html', products=top_15_products)

if __name__ == '__main__':
    app.run(debug=True)
