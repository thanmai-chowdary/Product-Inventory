from flask import Flask, render_template, request, redirect, url_for
from models import db, Product

app = Flask(__name__)

# MySQL database connection configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://inventory_user:Pandu%402002@localhost:3306/inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables before the first request
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        new_product = Product(name=name, quantity=int(quantity))
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
