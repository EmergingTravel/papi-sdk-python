b2b_order_booking_form_response = {
    "debug": None,
    "error": None,
    "status": "ok",
    "data": {
        "order_id": 847820663,
        "partner_order_id": "test_01",
        "payment_types": [
            {
                "amount": "18.9",
                "currency_code": "PLN",
                "is_need_credit_card_data": False,
                "is_need_cvc": False,
                "type": "deposit",
            },
            {
                "amount": "4.97",
                "currency_code": "USD",
                "is_need_credit_card_data": True,
                "is_need_cvc": True,
                "type": "now",
            },
            {
                "amount": "4.98",
                "currency_code": "EUR",
                "is_need_credit_card_data": True,
                "is_need_cvc": True,
                "type": "now",
            },
            {
                "amount": "3.98",
                "currency_code": "GBP",
                "is_need_credit_card_data": True,
                "is_need_cvc": True,
                "type": "now",
            },
            {
                "amount": "347.21",
                "currency_code": "RUB",
                "is_need_credit_card_data": True,
                "is_need_cvc": True,
                "type": "now",
            },
        ],
        "item_id": 1,
        "upsell_data": [],
    },
}

order_booking_form_error = {
    "debug": None,
    "error": "double_booking_form",
    "status": "error",
    "data": None,
}

affiliate_order_booking_form_response = {
    "debug": None,
    "error": None,
    "status": "ok",
    "data": {
        "order_id": 96155470,
        "partner_order_id": "test_02",
        "payment_types": [
            {
                "amount": "355",
                "currency_code": "RUB",
                "is_need_credit_card_data": True,
                "is_need_cvc": True,
                "type": "now",
            }
        ],
        "item_id": 2,
    },
}
