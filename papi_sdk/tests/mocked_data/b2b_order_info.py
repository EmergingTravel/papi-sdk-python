b2b_order_info_response = {
    "debug": None,
    "error": None,
    "status": "ok",
    "data": {
        "current_page_number": 1,
        "total_orders": 517,
        "total_pages": 517,
        "orders": [
            {
                "agreement_number": "test_01",
                "amount_payable": {
                    "amount": "0.00",
                    "currency_code": "PLN",
                },
                "amount_payable_vat": {
                    "amount": "0.00",
                    "currency_code": "PLN",
                },
                "amount_refunded": {
                    "amount": "56.22",
                    "currency_code": "PLN",
                },
                "amount_sell": {
                    "amount": "56.22",
                    "currency_code": "PLN",
                },
                "amount_sell_b2b2c": {
                    "amount": "0.00",
                    "currency_code": "PLN",
                },
                "api_auth_key_id": None,
                "cancellation_info": {
                    "free_cancellation_before": "2016-07-14T03:00:00:000000",
                    "policies": [
                        {
                            "end_at": "2016-07-14T03:00:00:000000",
                            "penalty": {
                                "amount": "0",
                                "currency_code": "RUB",
                            },
                            "start_at": None,
                        },
                        {
                            "end_at": "2016-07-16T03:00:00:000000",
                            "penalty": {
                                "amount": "900",
                                "currency_code": "RUB",
                            },
                            "start_at": "2016-07-14T03:00:00:000000",
                        },
                        {
                            "end_at": None,
                            "penalty": {
                                "amount": "900",
                                "currency_code": "RUB",
                            },
                            "start_at": "2016-07-16T03:00:00:000000",
                        },
                    ],
                },
                "cancelled_at": "2016-07-11T14:26:08:000000",
                "checkin_at": "2016-07-16",
                "checkout_at": "2016-07-17",
                "contract_slug": "test_01",
                "created_at": "2016-07-11T14:21:54:000000",
                "hotel_data": {"id": "test_hotel", "order_id": None},
                "nights": 1,
                "order_id": 517312989,
                "order_type": "hotel",
                "partner_data": {
                    "order_comment": None,
                    "order_id": "test_01",
                },
                "roomnights": 1,
                "rooms_data": [
                    {
                        "bedding_name": ["nobedding"],
                        "guest_data": {
                            "adults_number": 2,
                            "children_number": 0,
                            "guests": [
                                {
                                    "first_name": "Test",
                                    "last_name": "Test",
                                    "is_child": False,
                                    "age": None,
                                }
                            ],
                        },
                        "meal_name": "unknown",
                        "room_idx": 0,
                        "room_name": "Villa",
                    }
                ],
                "source": "b2b-site",
                "status": "cancelled",
                "supplier_data": {"name": "Extranet", "order_id": "test_01"},
                "taxes": [],
                "total_vat": {"amount": "0", "currency_code": "PLN"},
                "amount_payable_with_upsells": {
                    "amount": "0.00",
                    "currency_code": "PLN",
                },
                "invoice_id": "12980-00001",
                "is_checked": False,
                "meta_data": {"voucher_order_comment": None},
                "payment_data": {
                    "invoice_id": 63450,
                    "paid_at": None,
                    "payment_by": None,
                    "payment_due": "2016-07-25",
                    "payment_pending": "2016-07-17",
                    "payment_type": "deposit",
                },
                "upsells": {
                    "amount_payable": None,
                    "amount_payable_vat": None,
                    "amount_refunded": None,
                    "amount_sell": None,
                    "amount_sell_b2b2c": None,
                    "cancelled_at": None,
                    "created_at": None,
                    "free_cancellation_before": None,
                    "info": None,
                    "order_id": None,
                    "order_type": None,
                    "payment_data": None,
                    "status": None,
                    "type": None,
                },
                "user_data": {"email": "foo@bar.com"},
            }
        ],
    },
}
