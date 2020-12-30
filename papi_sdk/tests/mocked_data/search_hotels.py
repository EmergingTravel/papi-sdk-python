b2b_hotels_response = {
    "debug": {
        "request": {
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "currency": None,
            "residency": "ru",
            "timeout": None,
            "language": "ru",
            "guests": [{"adults": 1, "children": []}],
            "upsells": {
                "early_checkin": {"time": "2020-08-05T10:00:00"},
                "late_checkout": {"time": "2020-08-06T15:00:00"},
                "only_eclc": True,
            },
            "ids": ["test_hotel"],
        },
        "key_id": 1,
        "validation_error": None,
    },
    "error": None,
    "status": "ok",
    "data": {
        "hotels": [
            {
                "id": "test_hotel",
                "rates": [
                    {
                        "daily_prices": ["9.90"],
                        "meal": "nomeal",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "9.90",
                                    "show_amount": "9.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "1.65",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "14.17",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T04:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-04T04:59:00",
                                                "end_at": None,
                                                "amount_charge": "9.90",
                                                "amount_show": "9.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "9.90",
                                                        "amount_net": "9.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "9.90",
                                                        "amount_net": "9.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T04:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "29.45",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "2.00",
                                                "show_price": "2.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "2.00",
                                                        "amount_net": "2.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "2.00",
                                                        "amount_net": "2.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "2.00",
                                                "show_price": "2.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "2.00",
                                                        "amount_net": "2.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "2.00",
                                                        "amount_net": "2.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "9.90",
                                            "amount_net": "9.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "9.90",
                                            "amount_net": "9.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 5,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 1,
                            "club": 0,
                        },
                        "room_name": "Одноместный люкс (дуплекс)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 20,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "170.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "9.52",
                            "currency_code": "PLN",
                        },
                    },
                    {
                        "daily_prices": ["10.90"],
                        "meal": "nomeal",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "10.90",
                                    "show_amount": "10.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "1.82",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "15.00",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T14:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-04T14:59:00",
                                                "end_at": None,
                                                "amount_charge": "10.90",
                                                "amount_show": "10.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "10.90",
                                                        "amount_net": "10.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "10.90",
                                                        "amount_net": "10.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T14:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "32.43",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "3.00",
                                                "show_price": "3.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "3.00",
                                                        "amount_net": "3.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "3.00",
                                                        "amount_net": "3.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "3.00",
                                                "show_price": "3.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "3.00",
                                                        "amount_net": "3.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "3.00",
                                                        "amount_net": "3.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "10.90",
                                            "amount_net": "10.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "10.90",
                                            "amount_net": "10.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 5,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 1,
                            "club": 0,
                        },
                        "room_name": "Одноместный люкс (дуплекс)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 20,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "180.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "9.52",
                            "currency_code": "PLN",
                        },
                    },
                    {
                        "daily_prices": ["50.90"],
                        "meal": "nomeal",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "50.90",
                                    "show_amount": "50.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "8.48",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "75.00",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T14:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-04T14:59:00",
                                                "end_at": None,
                                                "amount_charge": "50.90",
                                                "amount_show": "50.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "50.90",
                                                        "amount_net": "50.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "50.90",
                                                        "amount_net": "50.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T14:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "151.44",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "11.00",
                                                "show_price": "11.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "11.00",
                                                "show_price": "11.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "50.90",
                                            "amount_net": "50.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "50.90",
                                            "amount_net": "50.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 1,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Economy (2 отдельные кровати)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 25,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "900.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "50.42",
                            "currency_code": "PLN",
                        },
                    },
                    {
                        "daily_prices": ["50.90"],
                        "meal": "nomeal",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "50.90",
                                    "show_amount": "50.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "8.48",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "75.00",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T14:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-04T14:59:00",
                                                "end_at": None,
                                                "amount_charge": "50.90",
                                                "amount_show": "50.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "50.90",
                                                        "amount_net": "50.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "50.90",
                                                        "amount_net": "50.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T14:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "151.44",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "11.00",
                                                "show_price": "11.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "11.00",
                                                "show_price": "11.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "11.00",
                                                        "amount_net": "11.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "50.90",
                                            "amount_net": "50.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "50.90",
                                            "amount_net": "50.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 1,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 1,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Economy (двухъярусная кровать)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 40,
                        "amenities_data": [
                            "bunk-bed",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "900.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "50.42",
                            "currency_code": "PLN",
                        },
                    },
                    {
                        "daily_prices": ["56.90"],
                        "meal": "half-board-dinner",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "56.90",
                                    "show_amount": "56.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "9.48",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "83.33",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T04:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-04T04:59:00",
                                                "end_at": None,
                                                "amount_charge": "56.90",
                                                "amount_show": "56.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "56.90",
                                                        "amount_net": "56.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "56.90",
                                                        "amount_net": "56.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T04:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "169.29",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "12.00",
                                                "show_price": "12.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "12.00",
                                                "show_price": "12.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "56.90",
                                            "amount_net": "56.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "56.90",
                                            "amount_net": "56.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 1,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Economy (2 отдельные кровати)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 25,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "1000.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "56.02",
                            "currency_code": "PLN",
                        },
                    },
                    {
                        "daily_prices": ["56.90"],
                        "meal": "nomeal",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "56.90",
                                    "show_amount": "56.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "9.48",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "83.33",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-05T14:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-05T14:59:00",
                                                "end_at": None,
                                                "amount_charge": "56.90",
                                                "amount_show": "56.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "56.90",
                                                        "amount_net": "56.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "56.90",
                                                        "amount_net": "56.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-05T14:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "169.29",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "12.00",
                                                "show_price": "12.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "12.00",
                                                "show_price": "12.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "56.90",
                                            "amount_net": "56.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "56.90",
                                            "amount_net": "56.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 1,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 1,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Economy (двухъярусная кровать)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 40,
                        "amenities_data": [
                            "bunk-bed",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "1000.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "50.42",
                            "currency_code": "PLN",
                        },
                    },
                    {
                        "daily_prices": ["56.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "56.90",
                                    "show_amount": "56.90",
                                    "currency_code": "PLN",
                                    "show_currency_code": "PLN",
                                    "by": None,
                                    "is_need_credit_card_data": False,
                                    "is_need_cvc": False,
                                    "type": "deposit",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "9.48",
                                                "currency_code": "PLN",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "83.33",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T04:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "0.00",
                                                        "amount_net": "0.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                            {
                                                "start_at": "2020-08-04T04:59:00",
                                                "end_at": None,
                                                "amount_charge": "56.90",
                                                "amount_show": "56.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "56.90",
                                                        "amount_net": "56.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "56.90",
                                                        "amount_net": "56.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T04:59:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "169.29",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "12.00",
                                                "show_price": "12.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "12.00",
                                                "show_price": "12.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "12.00",
                                                        "amount_net": "12.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "56.90",
                                            "amount_net": "56.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "56.90",
                                            "amount_net": "56.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 1,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Economy (двуспальная кровать)",
                        "serp_filters": ["has_breakfast", "has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 23,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "1000.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "56.02",
                            "currency_code": "PLN",
                        },
                    },
                ],
                "bar_price_data": {
                    "hotel": {"price": "9.52", "currency": "PLN"},
                    "room_groups": [
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 1,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 1,
                                "family": 0,
                                "capacity": 2,
                                "club": 0,
                            },
                            "price": "50.42",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 5,
                                "quality": 0,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 0,
                                "family": 0,
                                "capacity": 1,
                                "club": 0,
                            },
                            "price": "9.52",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 1,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 3,
                                "family": 0,
                                "capacity": 2,
                                "club": 0,
                            },
                            "price": "50.42",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 1,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 4,
                                "family": 0,
                                "capacity": 2,
                                "club": 0,
                            },
                            "price": "50.42",
                            "currency": "PLN",
                        },
                    ],
                },
            }
        ],
        "total_hotels": 1,
    },
}
affiliate_hotels_response = {
    "debug": {
        "request": {
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "currency": None,
            "residency": "ru",
            "timeout": None,
            "language": "ru",
            "guests": [{"adults": 1, "children": []}],
            "ids": ["test_hotel"],
        },
        "key_id": 2,
        "validation_error": None,
    },
    "error": None,
    "status": "ok",
    "data": {
        "hotels": [
            {
                "id": "test_hotel",
                "rates": [
                    {
                        "daily_prices": ["167.00"],
                        "meal": "nomeal",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "167.00",
                                    "show_amount": "167.00",
                                    "currency_code": "RUB",
                                    "show_currency_code": "RUB",
                                    "by": "credit_card",
                                    "is_need_credit_card_data": True,
                                    "is_need_cvc": True,
                                    "type": "now",
                                    "tax_data": {
                                        "taxes": [
                                            {
                                                "name": "vat",
                                                "included_by_supplier": True,
                                                "amount": "27.83",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "resort_fee",
                                                "included_by_supplier": False,
                                                "amount": "3905.48",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "environmental_fee",
                                                "included_by_supplier": False,
                                                "amount": "14.17",
                                                "currency_code": "RUB",
                                            },
                                            {
                                                "name": "city_tax",
                                                "included_by_supplier": False,
                                                "amount": "1.61",
                                                "currency_code": "RUB",
                                            },
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T04:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T04:59:00",
                                                "end_at": None,
                                                "amount_charge": "167.00",
                                                "amount_show": "167.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T04:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 5,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 1,
                            "club": 0,
                        },
                        "room_name": "Одноместный люкс (дуплекс)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 20,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "170.00",
                            "currency_code": "RUB",
                            "from_time": "12:00:00",
                        },
                    }
                ],
            }
        ],
        "total_hotels": 1,
    },
}
