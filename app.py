from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
import os
import stripe

load_dotenv()

app = Flask(__name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html', key=os.getenv('STRIPE_PUBLISHABLE_KEY'))


@app.route('/charge', methods=['POST'])
def create_charge():
    try:
        amount = int(request.form.get('amount'))
        currency = request.form.get('currency')
        description = request.form.get('description')
        token = request.form.get('stripeToken')

        stripe.Charge.create(
            amount=amount,
            currency=currency,
            description=description,
            source=token
        )

        return jsonify(message="Payment completed successfully"), 200

    except Exception as e:
        return jsonify(message=str(e)), 400


if __name__ == '__main__':
    app.run(debug=True)
