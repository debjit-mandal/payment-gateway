from flask import Flask, jsonify, request, render_template
import os
import stripe
import logging
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app.config['SESSION_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True

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

        logging.info(f"Charge successful for {amount} {currency}")
        return jsonify(message="Payment completed successfully"), 200

    except stripe.error.CardError as e:
        logging.error(f"Card error: {e.error.message}")
        return jsonify(message=str(e.error.message)), 400
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify(message=str(e)), 400


if __name__ == '__main__':
    app.run(debug=True, port=8080)
