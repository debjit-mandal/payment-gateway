.. highlight:: rst

============================
simple-payment-gateway
============================

This is a basic payment integration using Stripe's Python SDK.

* Setup Stripe Account:

  - First, sign up for a `Stripe Account <https://stripe.com>`_
  - Go to `Dashboard <https://dashboard.stripe.com/test/apikeys>`_


* Some necessary packages must be installed for running the code::

        pip install Flask stripe python-dotenv

**In the** ``.env`` **file please replace the** ``SECRET_KEY`` **with your Stripe Secret Key and** ``PUBLISHABLE_KEY`` **with your Stripe Publishable Key. These can be found in the Stripe Dashboard.**

* **To run the code locally**:



1. *Fork this repository*

2. ::

    git clone https://github.com/debjit-mandal/simple-payment-gateway.git

3. ::
        
    cd simple-payment-gateway

4. ::

    python app.py


5. *Visit* `http://localhost:5000 <http://localhost:5000>`_ *to view the frontend.*

Feel free to suggest any kind of improvments.
