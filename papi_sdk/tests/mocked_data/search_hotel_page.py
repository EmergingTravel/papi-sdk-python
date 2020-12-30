b2b_hotel_page_response = {
    "debug": {
        "b2b_request": {
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
            "id": "test_hotel",
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
                        "daily_prices": ["97.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "97.90",
                                    "show_amount": "97.90",
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
                                                "amount": "16.32",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "97.90",
                                                "amount_show": "97.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "98.00",
                                                        "amount_net": "97.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "98.00",
                                                        "amount_net": "97.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "20.00",
                                                "show_price": "20.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "20.00",
                                                "show_price": "20.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "98.00",
                                            "amount_net": "97.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "98.00",
                                            "amount_net": "97.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Standard (двуспальная кровать) (двуспальная кровать king size, тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-cfcbed18-bd30-5299-8484-84324c28a77b",
                    },
                    {
                        "daily_prices": ["97.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "97.90",
                                    "show_amount": "97.90",
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
                                                "amount": "16.32",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "97.90",
                                                "amount_show": "97.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "98.00",
                                                        "amount_net": "97.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "98.00",
                                                        "amount_net": "97.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "20.00",
                                                "show_price": "20.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "20.00",
                                                "show_price": "20.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "20.00",
                                                        "amount_net": "20.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "98.00",
                                            "amount_net": "97.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "98.00",
                                            "amount_net": "97.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Standard (2 отдельные кровати) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-1f3fd417-7765-5653-915a-300ce68f9560",
                    },
                    {
                        "daily_prices": ["144.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "144.90",
                                    "show_amount": "144.90",
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
                                                "amount": "24.15",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
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
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "144.90",
                                                "amount_show": "144.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "144.90",
                                                        "amount_net": "144.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "144.90",
                                                        "amount_net": "144.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "6.19",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "29.00",
                                                "show_price": "29.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "29.00",
                                                        "amount_net": "29.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "29.00",
                                                        "amount_net": "29.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "29.00",
                                                "show_price": "29.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "29.00",
                                                        "amount_net": "29.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "29.00",
                                                        "amount_net": "29.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "144.90",
                                            "amount_net": "144.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "144.90",
                                            "amount_net": "144.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Standard (двуспальная кровать) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 981,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "31.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "123.96",
                            "currency_code": "PLN",
                        },
                        "book_hash": "h-eca4e776-f44c-5716-8d3c-4d9d749e937c",
                    },
                    {
                        "daily_prices": ["160.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "160.90",
                                    "show_amount": "160.90",
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
                                                "amount": "26.82",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "160.90",
                                                "amount_show": "160.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "161.00",
                                                        "amount_net": "160.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "161.00",
                                                        "amount_net": "160.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "33.00",
                                                "show_price": "33.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "33.00",
                                                "show_price": "33.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "161.00",
                                            "amount_net": "160.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "161.00",
                                            "amount_net": "160.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 4,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Business (2 отдельные кровати) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-f4bb3906-9fcb-5bb5-a5e0-f19a40a7194c",
                    },
                    {
                        "daily_prices": ["160.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "160.90",
                                    "show_amount": "160.90",
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
                                                "amount": "26.82",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "160.90",
                                                "amount_show": "160.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "161.00",
                                                        "amount_net": "160.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "161.00",
                                                        "amount_net": "160.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "33.00",
                                                "show_price": "33.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "33.00",
                                                "show_price": "33.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "33.00",
                                                        "amount_net": "33.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "161.00",
                                            "amount_net": "160.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "161.00",
                                            "amount_net": "160.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 4,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Business (двуспальная кровать) (двуспальная кровать king size, тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-b415f7bc-c335-584a-a5eb-4969f78cf4aa",
                    },
                    {
                        "daily_prices": ["199.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "199.90",
                                    "show_amount": "199.90",
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
                                                "amount": "33.32",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
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
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "199.90",
                                                "amount_show": "199.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "199.90",
                                                        "amount_net": "199.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "199.90",
                                                        "amount_net": "199.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "8.54",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "40.00",
                                                "show_price": "40.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "40.00",
                                                        "amount_net": "40.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "40.00",
                                                        "amount_net": "40.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "40.00",
                                                "show_price": "40.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "40.00",
                                                        "amount_net": "40.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "40.00",
                                                        "amount_net": "40.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "199.90",
                                            "amount_net": "199.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "199.90",
                                            "amount_net": "199.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 5,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Superior (двуспальная кровать) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 312,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "43.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "171.62",
                            "currency_code": "PLN",
                        },
                        "book_hash": "h-f245d0a4-fbaf-59cc-86f5-69c3a54fc06d",
                    },
                    {
                        "daily_prices": ["231.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "231.90",
                                    "show_amount": "231.90",
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
                                                "amount": "38.65",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "231.90",
                                                "amount_show": "231.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "232.00",
                                                        "amount_net": "231.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "232.00",
                                                        "amount_net": "231.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "47.00",
                                                "show_price": "47.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "47.00",
                                                "show_price": "47.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "232.00",
                                            "amount_net": "231.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "232.00",
                                            "amount_net": "231.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 4,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный полулюкс (двуспальная кровать) (двуспальная кровать king size, тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-e3a39df7-ff05-5e9d-a65c-9b3957b7ce27",
                    },
                    {
                        "daily_prices": ["231.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "231.90",
                                    "show_amount": "231.90",
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
                                                "amount": "38.65",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "231.90",
                                                "amount_show": "231.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "232.00",
                                                        "amount_net": "231.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "232.00",
                                                        "amount_net": "231.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "47.00",
                                                "show_price": "47.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "47.00",
                                                "show_price": "47.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "47.00",
                                                        "amount_net": "47.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "232.00",
                                            "amount_net": "231.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "232.00",
                                            "amount_net": "231.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 4,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный полулюкс (2 отдельные кровати) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-5f35bd1d-2f03-593d-9287-8c579f7da8a9",
                    },
                    {
                        "daily_prices": ["238.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "238.90",
                                    "show_amount": "238.90",
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
                                                "amount": "39.82",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
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
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "238.90",
                                                "amount_show": "238.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "238.90",
                                                        "amount_net": "238.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "238.90",
                                                        "amount_net": "238.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "10.20",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "48.00",
                                                "show_price": "48.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "48.00",
                                                        "amount_net": "48.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "48.00",
                                                        "amount_net": "48.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "48.00",
                                                "show_price": "48.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "48.00",
                                                        "amount_net": "48.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "48.00",
                                                        "amount_net": "48.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "238.90",
                                            "amount_net": "238.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "238.90",
                                            "amount_net": "238.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 4,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Business (двуспальная кровать) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 117,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "52.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "204.99",
                            "currency_code": "PLN",
                        },
                        "book_hash": "h-fa54d921-ee14-5618-a175-adb6c944ba6b",
                    },
                    {
                        "daily_prices": ["269.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "269.90",
                                    "show_amount": "269.90",
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
                                                "amount": "44.98",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "269.90",
                                                "amount_show": "269.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "270.00",
                                                        "amount_net": "269.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "270.00",
                                                        "amount_net": "269.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "54.00",
                                                "show_price": "54.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "54.00",
                                                        "amount_net": "54.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "54.00",
                                                        "amount_net": "54.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "54.00",
                                                "show_price": "54.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "54.00",
                                                        "amount_net": "54.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "54.00",
                                                        "amount_net": "54.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "270.00",
                                            "amount_net": "269.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "270.00",
                                            "amount_net": "269.90",
                                            "amount_commission": "0.10",
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
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный люкс (двуспальная кровать)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-fe6b5ac8-f7eb-508f-bede-5fd572fd8c90",
                    },
                    {
                        "daily_prices": ["343.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "343.90",
                                    "show_amount": "343.90",
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
                                                "amount": "57.32",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "343.90",
                                                "amount_show": "343.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "344.00",
                                                        "amount_net": "343.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "344.00",
                                                        "amount_net": "343.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "69.00",
                                                "show_price": "69.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "69.00",
                                                "show_price": "69.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "344.00",
                                            "amount_net": "343.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "344.00",
                                            "amount_net": "343.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 5,
                            "quality": 4,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный люкс Business (двуспальная кровать)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-34b2f31f-61e9-55a4-820d-401963dfe8be",
                    },
                    {
                        "daily_prices": ["344.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "344.90",
                                    "show_amount": "344.90",
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
                                                "amount": "57.48",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
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
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "344.90",
                                                "amount_show": "344.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "344.90",
                                                        "amount_net": "344.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "344.90",
                                                        "amount_net": "344.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "14.73",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "69.00",
                                                "show_price": "69.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "69.00",
                                                "show_price": "69.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "69.00",
                                                        "amount_net": "69.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "344.90",
                                            "amount_net": "344.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "344.90",
                                            "amount_net": "344.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 4,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 0,
                            "club": 0,
                        },
                        "room_name": "Полулюкс",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 28,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "75.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "295.58",
                            "currency_code": "PLN",
                        },
                        "book_hash": "h-17278bae-1b55-5312-88dd-d33752e085a0",
                    },
                    {
                        "daily_prices": ["399.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "399.90",
                                    "show_amount": "399.90",
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
                                                "amount": "66.65",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
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
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "399.90",
                                                "amount_show": "399.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "399.90",
                                                        "amount_net": "399.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "399.90",
                                                        "amount_net": "399.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "17.08",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "80.00",
                                                "show_price": "80.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "80.00",
                                                        "amount_net": "80.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "80.00",
                                                        "amount_net": "80.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "80.00",
                                                "show_price": "80.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "80.00",
                                                        "amount_net": "80.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "80.00",
                                                        "amount_net": "80.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "399.90",
                                            "amount_net": "399.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "399.90",
                                            "amount_net": "399.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 0,
                            "club": 0,
                        },
                        "room_name": "Номер Standard",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 9,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "87.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "343.24",
                            "currency_code": "PLN",
                        },
                        "book_hash": "h-6d8688f5-c3c6-5081-877c-ebf5eb80439b",
                    },
                    {
                        "daily_prices": ["418.90"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "418.90",
                                    "show_amount": "418.90",
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
                                                "amount": "69.82",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
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
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "418.90",
                                                "amount_show": "418.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "419.00",
                                                        "amount_net": "418.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "419.00",
                                                        "amount_net": "418.90",
                                                        "amount_commission": "0.10",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                    "vat_data": {
                                        "included": False,
                                        "value": "0.00",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "84.00",
                                                "show_price": "84.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "84.00",
                                                        "amount_net": "84.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "84.00",
                                                        "amount_net": "84.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "84.00",
                                                "show_price": "84.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "84.00",
                                                        "amount_net": "84.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "84.00",
                                                        "amount_net": "84.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "419.00",
                                            "amount_net": "418.90",
                                            "amount_commission": "0.10",
                                        },
                                        "charge": {
                                            "amount_gross": "419.00",
                                            "amount_net": "418.90",
                                            "amount_commission": "0.10",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 6,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместные апартаменты (двуспальная кровать) (1 комната)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "bar_rate_price_data": None,
                        "book_hash": "h-6399c583-f3fb-5af6-b5ac-fc6aa9e2d07e",
                    },
                    {
                        "daily_prices": ["510.90"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "510.90",
                                    "show_amount": "510.90",
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
                                                "amount": "85.15",
                                                "currency_code": "PLN",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
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
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "510.90",
                                                "amount_show": "510.90",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "510.90",
                                                        "amount_net": "510.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "510.90",
                                                        "amount_net": "510.90",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                    "vat_data": {
                                        "included": True,
                                        "value": "21.82",
                                    },
                                    "perks": {
                                        "early_checkin": [
                                            {
                                                "charge_price": "103.00",
                                                "show_price": "103.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "103.00",
                                                        "amount_net": "103.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "103.00",
                                                        "amount_net": "103.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "10:00",
                                            }
                                        ],
                                        "late_checkout": [
                                            {
                                                "charge_price": "103.00",
                                                "show_price": "103.00",
                                                "commission_info": {
                                                    "show": {
                                                        "amount_gross": "103.00",
                                                        "amount_net": "103.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                    "charge": {
                                                        "amount_gross": "103.00",
                                                        "amount_net": "103.00",
                                                        "amount_commission": "0.00",
                                                    },
                                                },
                                                "time": "15:00",
                                            }
                                        ],
                                    },
                                    "commission_info": {
                                        "show": {
                                            "amount_gross": "510.90",
                                            "amount_net": "510.90",
                                            "amount_commission": "0.00",
                                        },
                                        "charge": {
                                            "amount_gross": "510.90",
                                            "amount_net": "510.90",
                                            "amount_commission": "0.00",
                                        },
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 5,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 0,
                            "club": 0,
                        },
                        "room_name": "Номер Superior",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 2,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "112.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "bar_rate_price_data": {
                            "amount": "438.59",
                            "currency_code": "PLN",
                        },
                        "book_hash": "h-d4a635ef-65f6-58c4-a7a6-557f7e77e464",
                    },
                ],
                "bar_price_data": {
                    "hotel": {"price": "123.96", "currency": "PLN"},
                    "room_groups": [
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 2,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 3,
                                "family": 0,
                                "capacity": 2,
                                "club": 0,
                            },
                            "price": "123.96",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 5,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 3,
                                "family": 0,
                                "capacity": 2,
                                "club": 0,
                            },
                            "price": "171.62",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 4,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 3,
                                "family": 0,
                                "capacity": 2,
                                "club": 0,
                            },
                            "price": "204.99",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 4,
                                "quality": 0,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 0,
                                "family": 0,
                                "capacity": 0,
                                "club": 0,
                            },
                            "price": "295.58",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 2,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 0,
                                "family": 0,
                                "capacity": 0,
                                "club": 0,
                            },
                            "price": "343.24",
                            "currency": "PLN",
                        },
                        {
                            "rg_ext": {
                                "rg_class": 3,
                                "quality": 5,
                                "sex": 0,
                                "bathroom": 2,
                                "bedding": 0,
                                "family": 0,
                                "capacity": 0,
                                "club": 0,
                            },
                            "price": "438.59",
                            "currency": "PLN",
                        },
                    ],
                },
            }
        ]
    },
}


affiliate_hotel_page_response = {
    "debug": {
        "b2b_request": {
            "checkin": "2020-08-05",
            "checkout": "2020-08-06",
            "currency": None,
            "residency": "ru",
            "timeout": None,
            "language": "ru",
            "guests": [{"adults": 1, "children": []}],
            "id": "test_hotel",
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
                        "daily_prices": ["2097.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "2097.00",
                                    "show_amount": "2097.00",
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
                                                "amount": "349.50",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "2097.00",
                                                "amount_show": "2097.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Standard (двуспальная кровать) (двуспальная кровать king size, тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-50a6d4ca-fe41-583d-9da3-eb243e44956e",
                    },
                    {
                        "daily_prices": ["2097.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "2097.00",
                                    "show_amount": "2097.00",
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
                                                "amount": "349.50",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "2097.00",
                                                "amount_show": "2097.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Standard (2 отдельные кровати) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-510d3f42-f0f7-5c0e-bc0e-bd8d67c48308",
                    },
                    {
                        "daily_prices": ["3468.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "3468.00",
                                    "show_amount": "3468.00",
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
                                                "amount": "578.00",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "3468.00",
                                                "amount_show": "3468.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 4,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Business (двуспальная кровать) (двуспальная кровать king size, тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-3a563874-dac9-5ee9-9f36-446811e43eff",
                    },
                    {
                        "daily_prices": ["3468.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "3468.00",
                                    "show_amount": "3468.00",
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
                                                "amount": "578.00",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "3468.00",
                                                "amount_show": "3468.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 4,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Business (2 отдельные кровати) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-4ed9053d-92e3-5895-95fd-57b3eab8c02e",
                    },
                    {
                        "daily_prices": ["53.23"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "3709.00",
                                    "show_amount": "3709.00",
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
                                                "amount": "618.17",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "3709.00",
                                                "amount_show": "3709.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 5,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный номер Superior (двуспальная кровать) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 312,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "43.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "book_hash": "h-ddcdbbd6-0d69-5b0c-9590-297546579ed9",
                    },
                    {
                        "daily_prices": ["5001.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "5001.00",
                                    "show_amount": "5001.00",
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
                                                "amount": "833.50",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "5001.00",
                                                "amount_show": "5001.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 4,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный полулюкс (двуспальная кровать) (двуспальная кровать king size, тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-45207eff-5ad3-5122-bff9-9c26b882b152",
                    },
                    {
                        "daily_prices": ["5001.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "5001.00",
                                    "show_amount": "5001.00",
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
                                                "amount": "833.50",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "5001.00",
                                                "amount_show": "5001.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 4,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 4,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный полулюкс (2 отдельные кровати) (тип кровати может измениться)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "twin",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-3fbe7ce0-19eb-5645-a1d4-da8121157c02",
                    },
                    {
                        "daily_prices": ["5808.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "5808.00",
                                    "show_amount": "5808.00",
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
                                                "amount": "968.00",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "5808.00",
                                                "amount_show": "5808.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 5,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный люкс (двуспальная кровать)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-eb6f8537-1b80-54d2-8a70-b8bfd8e8a9d1",
                    },
                    {
                        "daily_prices": ["91.68"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "6388.00",
                                    "show_amount": "6388.00",
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
                                                "amount": "1064.67",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "6388.00",
                                                "amount_show": "6388.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 4,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 1,
                            "club": 0,
                        },
                        "room_name": "Одноместный полулюкс",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 28,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "75.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "book_hash": "h-2fc30847-dd5c-50c6-9930-3eda4afcef74",
                    },
                    {
                        "daily_prices": ["106.47"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "7418.00",
                                    "show_amount": "7418.00",
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
                                                "amount": "1236.33",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "7418.00",
                                                "amount_show": "7418.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 2,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 1,
                            "club": 0,
                        },
                        "room_name": "Одноместный номер Standard",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 9,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "87.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "book_hash": "h-686c6d0c-ad5e-50be-966b-ed2713547a67",
                    },
                    {
                        "daily_prices": ["7421.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "7421.00",
                                    "show_amount": "7421.00",
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
                                                "amount": "1236.83",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "7421.00",
                                                "amount_show": "7421.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 5,
                            "quality": 5,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместный люкс Superior (двуспальная кровать)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-5fb299f5-8afd-5718-97cb-1e2f000352bb",
                    },
                    {
                        "daily_prices": ["9034.00"],
                        "meal": "breakfast-buffet",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "9034.00",
                                    "show_amount": "9034.00",
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
                                                "amount": "1505.67",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-04T20:59:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-04T20:59:00",
                                                "end_at": None,
                                                "amount_charge": "9034.00",
                                                "amount_show": "9034.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-04T20:59:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 6,
                            "quality": 0,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 3,
                            "family": 0,
                            "capacity": 2,
                            "club": 0,
                        },
                        "room_name": "Двухместные апартаменты (двуспальная кровать) (1 комната)",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": None,
                        "amenities_data": [
                            "double",
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": True,
                        "deposit": None,
                        "no_show": None,
                        "book_hash": "h-5bfa5429-4b87-5ffd-8a3c-57baec18f6fe",
                    },
                    {
                        "daily_prices": ["136.05"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "9479.00",
                                    "show_amount": "9479.00",
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
                                                "amount": "1579.83",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "9479.00",
                                                "amount_show": "9479.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
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
                        "room_name": "Одноместный люкс",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 2,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "112.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "book_hash": "h-1cbed9af-d3ab-5ed0-b6ad-dd397ed6d79f",
                    },
                    {
                        "daily_prices": ["150.85"],
                        "meal": "breakfast",
                        "payment_options": {
                            "payment_types": [
                                {
                                    "amount": "10510.00",
                                    "show_amount": "10510.00",
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
                                                "amount": "1751.67",
                                                "currency_code": "RUB",
                                            }
                                        ]
                                    },
                                    "cancellation_penalties": {
                                        "policies": [
                                            {
                                                "start_at": None,
                                                "end_at": "2020-08-03T21:00:00",
                                                "amount_charge": "0.00",
                                                "amount_show": "0.00",
                                            },
                                            {
                                                "start_at": "2020-08-03T21:00:00",
                                                "end_at": None,
                                                "amount_charge": "10510.00",
                                                "amount_show": "10510.00",
                                            },
                                        ],
                                        "free_cancellation_before": "2020-08-03T21:00:00",
                                    },
                                }
                            ]
                        },
                        "rg_ext": {
                            "rg_class": 3,
                            "quality": 5,
                            "sex": 0,
                            "bathroom": 2,
                            "bedding": 0,
                            "family": 0,
                            "capacity": 1,
                            "club": 0,
                        },
                        "room_name": "Одноместный номер Superior",
                        "serp_filters": ["has_bathroom"],
                        "sell_price_limits": None,
                        "allotment": 3,
                        "amenities_data": [
                            "non-smoking",
                            "private-bathroom",
                            "window",
                        ],
                        "any_residency": False,
                        "deposit": None,
                        "no_show": {
                            "amount": "124.00",
                            "currency_code": "USD",
                            "from_time": "12:00:00",
                        },
                        "book_hash": "h-81bfa660-c8c3-52f4-895a-a2ceafc9fa72",
                    },
                ],
            }
        ]
    },
}
