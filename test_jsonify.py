import unittest
from moneylover import *

testjson = {
  "1": {"amount": -7, "category": "Food & Beverage", "date": "2016-06-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "2": {"amount": -30, "category": "Food & Beverage", "date": "2016-06-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "3": {"amount": -4, "category": "Groceries", "date": "2016-06-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "4": {"amount": -0.8, "category": "Coffee & Snacks", "date": "2016-06-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "5": {"amount": -49.95, "category": "Entertainment", "date": "2016-06-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "6": {"amount": -10, "category": "Transportation", "date": "2016-06-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "7": {"amount": -4, "category": "Coffee & Snacks", "date": "2016-06-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "8": {"amount": -30, "category": "Groceries", "date": "2016-06-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "9": {"amount": -300, "category": "Bills & Utilities", "date": "2016-06-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "10": {"amount": 2871.93, "category": "Salary", "date": "2016-06-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "11": {"amount": -5.9, "category": "Coffee & Snacks", "date": "2016-06-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "12": {"amount": -70.2, "category": "Clothes & Shoes", "date": "2016-06-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "13": {"amount": -10, "category": "Transportation", "date": "2016-06-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "14": {"amount": -69.95, "category": "Phone", "date": "2016-06-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "15": {"amount": 637.5, "category": "Salary", "date": "2016-06-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "16": {"amount": -35.5, "category": "Accessories & Make Up", "date": "2016-06-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "17": {"amount": -100, "category": "Travel", "date": "2016-06-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "18": {"amount": -4, "category": "Coffee & Snacks", "date": "2016-06-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "19": {"amount": -5, "category": "Transportation", "date": "2016-06-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "20": {"amount": -3.75, "category": "Coffee & Snacks", "date": "2016-06-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "21": {"amount": -11.65, "category": "Food & Beverage", "date": "2016-06-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "22": {"amount": -52, "category": "Business", "date": "2016-06-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "23": {"amount": -12, "category": "Groceries", "date": "2016-06-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "24": {"amount": -7.8, "category": "Coffee & Snacks", "date": "2016-06-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "25": {"amount": -487.88, "category": "Travel", "date": "2016-06-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "26": {"amount": -55.69, "category": "Groceries", "date": "2016-06-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "27": {"amount": -20, "category": "Transportation", "date": "2016-06-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "28": {"amount": -4, "category": "Coffee & Snacks", "date": "2016-06-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "29": {"amount": -18.4, "category": "Lunch & Dinners", "date": "2016-06-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "30": {"amount": -20, "category": "Transportation", "date": "2016-06-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "31": {"amount": -18.14, "category": "Groceries", "date": "2016-06-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "32": {"amount": -3, "category": "Shopping", "date": "2016-06-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "33": {"amount": -3.75, "category": "Coffee & Snacks", "date": "2016-06-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "34": {"amount": -4, "category": "Coffee & Snacks", "date": "2016-06-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "35": {"amount": -150, "category": "Water", "date": "2016-06-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "36": {"amount": -20.35, "category": "Groceries", "date": "2016-06-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "37": {"amount": 465, "category": "Salary", "date": "2016-06-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "38": {"amount": -12.2, "category": "Coffee & Snacks", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "39": {"amount": -6, "category": "Transportation", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "40": {"amount": -10.05, "category": "Coffee & Snacks", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "41": {"amount": -3, "category": "Coffee & Snacks", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "42": {"amount": -5.75, "category": "Food & Beverage", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "43": {"amount": -225, "category": "Others", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "44": {"amount": -1215, "category": "Bills & Utilities", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "45": {"amount": -59.99, "category": "Internet", "date": "2016-06-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "46": {"amount": -15.65, "category": "Food & Beverage", "date": "2016-06-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "47": {"amount": -4.6, "category": "Coffee & Snacks", "date": "2016-06-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "48": {"amount": -5.9, "category": "Bills & Utilities", "date": "2016-06-27 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "49": {"amount": -150, "category": "Bills & Utilities", "date": "2016-06-27 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "50": {"amount": -2.3, "category": "Transportation", "date": "2016-06-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "51": {"amount": -18.95, "category": "Accessories & Make Up", "date": "2016-06-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "52": {"amount": -36, "category": "Accessories & Make Up", "date": "2016-06-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "53": {"amount": -7, "category": "Coffee & Snacks", "date": "2016-06-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "54": {"amount": -6, "category": "Transportation", "date": "2016-06-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "55": {"amount": -79.05, "category": "Groceries", "date": "2016-06-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "56": {"amount": -10, "category": "Transportation", "date": "2016-06-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "57": {"amount": -7.5, "category": "Coffee & Snacks", "date": "2016-06-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "58": {"amount": -7.2, "category": "Groceries", "date": "2016-06-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "59": {"amount": 1, "category": "Salary", "date": "2016-06-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "60": {"amount": 168, "category": "Salary", "date": "2016-06-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "61": {"amount": -10, "category": "Transportation", "date": "2016-07-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "62": {"amount": -6.4, "category": "Food & Beverage", "date": "2016-07-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "63": {"amount": -10, "category": "Food & Beverage", "date": "2016-07-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "64": {"amount": -16.6, "category": "Coffee & Snacks", "date": "2016-07-02 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "65": {"amount": -11.4, "category": "Food & Beverage", "date": "2016-07-02 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "66": {"amount": 100, "category": "Gifts", "date": "2016-07-03 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "67": {"amount": -12.5, "category": "Food & Beverage", "date": "2016-07-03 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "68": {"amount": -1, "category": "Transportation", "date": "2016-07-04 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "69": {"amount": -20, "category": "Transportation", "date": "2016-07-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "70": {"amount": -15.37, "category": "Groceries", "date": "2016-07-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "71": {"amount": -19, "category": "Phone", "date": "2016-07-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "72": {"amount": -8.1, "category": "Food & Beverage", "date": "2016-07-06 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "73": {"amount": -14.99, "category": "Games", "date": "2016-07-06 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "74": {"amount": -5, "category": "Transportation", "date": "2016-07-06 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "75": {"amount": -3.79, "category": "Food & Beverage", "date": "2016-07-06 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "76": {"amount": 713, "category": "Salary", "date": "2016-07-07 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "77": {"amount": -12, "category": "Coffee & Snacks", "date": "2016-07-07 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "78": {"amount": -4, "category": "Coffee & Snacks", "date": "2016-07-07 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "79": {"amount": -10.35, "category": "Food & Beverage", "date": "2016-07-08 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "80": {"amount": -34.49, "category": "Groceries", "date": "2016-07-08 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "81": {"amount": -2.5, "category": "Groceries", "date": "2016-07-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "82": {"amount": -22, "category": "Lunch & Dinners", "date": "2016-07-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "83": {"amount": -8.65, "category": "Groceries", "date": "2016-07-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "84": {"amount": -7, "category": "Coffee & Snacks", "date": "2016-07-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "85": {"amount": -3, "category": "Groceries", "date": "2016-07-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "86": {"amount": -6, "category": "Groceries", "date": "2016-07-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "87": {"amount": -27.8, "category": "Lunch & Dinners", "date": "2016-07-11 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "88": {"amount": -20, "category": "Movies", "date": "2016-07-11 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "89": {"amount": -8, "category": "Lunch & Dinners", "date": "2016-07-11 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "90": {"amount": -33.5, "category": "Coffee & Snacks", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "91": {"amount": -8.82, "category": "Coffee & Snacks", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "92": {"amount": -33.5, "category": "Lunch & Dinners", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "93": {"amount": -10, "category": "Transportation", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "94": {"amount": -24, "category": "Clothes & Shoes", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "95": {"amount": 200, "category": "Salary", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "96": {"amount": -20, "category": "Lunch & Dinners", "date": "2016-07-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "97": {"amount": -11, "category": "Coffee & Snacks", "date": "2016-07-13 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "98": {"amount": -11.1, "category": "Food & Beverage", "date": "2016-07-13 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "99": {"amount": -9.5, "category": "Lunch & Dinners", "date": "2016-07-13 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "100": {"amount": -5.5, "category": "Coffee & Snacks", "date": "2016-07-13 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "101": {"amount": -131.99, "category": "Electricity", "date": "2016-07-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "102": {"amount": -16.4, "category": "Coffee & Snacks", "date": "2016-07-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "103": {"amount": -8, "category": "Food & Beverage", "date": "2016-07-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "104": {"amount": -11.21, "category": "Groceries", "date": "2016-07-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "105": {"amount": 465, "category": "Salary", "date": "2016-07-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "106": {"amount": 3376.49, "category": "Salary", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "107": {"amount": -13, "category": "Coffee & Snacks", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "108": {"amount": -5, "category": "Lunch & Dinners", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "109": {"amount": -7.5, "category": "Travel", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "110": {"amount": -27, "category": "Lunch & Dinners", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "111": {"amount": -100, "category": "Activities & Outings", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "112": {"amount": -300, "category": "To Savings", "date": "2016-07-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "113": {"amount": -10, "category": "Personal Care", "date": "2016-07-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "114": {"amount": -6.99, "category": "Phone", "date": "2016-07-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "115": {"amount": -75.5, "category": "Groceries", "date": "2016-07-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "116": {"amount": -5, "category": "Games", "date": "2016-07-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "117": {"amount": -41.8, "category": "Movies", "date": "2016-07-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "118": {"amount": -6, "category": "Parking Fees", "date": "2016-07-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "119": {"amount": -15.5, "category": "Lunch & Dinners", "date": "2016-07-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "120": {"amount": -3, "category": "Coffee & Snacks", "date": "2016-07-17 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "121": {"amount": -215.05, "category": "Gas", "date": "2016-07-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "122": {"amount": -150, "category": "To Savings", "date": "2016-07-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "123": {"amount": -30, "category": "Myki", "date": "2016-07-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "124": {"amount": -14.25, "category": "Coffee & Snacks", "date": "2016-07-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "125": {"amount": -26.15, "category": "Lunch & Dinners", "date": "2016-07-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "126": {"amount": -155, "category": "Sports", "date": "2016-07-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "127": {"amount": -6.15, "category": "Groceries", "date": "2016-07-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "128": {"amount": -254, "category": "To Savings", "date": "2016-07-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "129": {"amount": -13.5, "category": "Lunch & Dinners", "date": "2016-07-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "130": {"amount": -9.5, "category": "Groceries", "date": "2016-07-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "131": {"amount": -50, "category": "Entertainment", "date": "2016-07-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "132": {"amount": -14, "category": "Lunch & Dinners", "date": "2016-07-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "133": {"amount": -40, "category": "Groceries", "date": "2016-07-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "134": {"amount": 713, "category": "Salary", "date": "2016-07-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "135": {"amount": -500, "category": "To Savings", "date": "2016-07-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "136": {"amount": -11.5, "category": "Lunch & Dinners", "date": "2016-07-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "137": {"amount": -25, "category": "Lunch & Dinners", "date": "2016-07-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "138": {"amount": -18, "category": "Clothes & Shoes", "date": "2016-07-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "139": {"amount": -8.5, "category": "Food & Beverage", "date": "2016-07-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "140": {"amount": -26.6, "category": "Clothes & Shoes", "date": "2016-07-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "141": {"amount": -34.9, "category": "Groceries", "date": "2016-07-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "142": {"amount": -32.5, "category": "Presents & Donations", "date": "2016-07-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "143": {"amount": -10.5, "category": "Groceries", "date": "2016-07-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "144": {"amount": -20, "category": "Myki", "date": "2016-07-23 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "145": {"amount": -125, "category": "Credit Card", "date": "2016-07-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "146": {"amount": -30, "category": "Myki", "date": "2016-07-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "147": {"amount": -59.99, "category": "Internet", "date": "2016-07-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "148": {"amount": -1216, "category": "Rent", "date": "2016-07-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "149": {"amount": -35, "category": "Groceries", "date": "2016-07-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "150": {"amount": -30, "category": "Lunch & Dinners", "date": "2016-07-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "151": {"amount": -24, "category": "Lunch & Dinners", "date": "2016-07-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "152": {"amount": -12.5, "category": "Lunch & Dinners", "date": "2016-07-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "153": {"amount": -29.71, "category": "Presents & Donations", "date": "2016-07-27 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "154": {"amount": -14, "category": "Lunch & Dinners", "date": "2016-07-27 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "155": {"amount": -5, "category": "Clothes & Shoes", "date": "2016-07-27 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "156": {"amount": -20, "category": "Lunch & Dinners", "date": "2016-07-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "157": {"amount": -0.65, "category": "Groceries", "date": "2016-07-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "158": {"amount": -2.95, "category": "Coffee & Snacks", "date": "2016-07-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "159": {"amount": -38, "category": "Groceries", "date": "2016-07-28 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "160": {"amount": -52.8, "category": "Presents & Donations", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "161": {"amount": -70.7, "category": "Phone", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "162": {"amount": -106.04, "category": "Credit Card", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "163": {"amount": -7.45, "category": "Fees & Charges", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "164": {"amount": 24.95, "category": "Selling", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "165": {"amount": 16, "category": "Others", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "166": {"amount": -5.6, "category": "Coffee & Snacks", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "167": {"amount": -26.5, "category": "Activities & Outings", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "168": {"amount": -11, "category": "Activities & Outings", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "169": {"amount": -16.8, "category": "Lunch & Dinners", "date": "2016-07-29 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "170": {"amount": -110.53, "category": "Groceries", "date": "2016-07-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "171": {"amount": -20, "category": "Presents & Donations", "date": "2016-07-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "172": {"amount": -64.97, "category": "Groceries", "date": "2016-07-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "173": {"amount": -300, "category": "To Savings", "date": "2016-07-30 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "174": {"amount": -906, "category": "Others", "date": "2016-08-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "175": {"amount": -87, "category": "Travel", "date": "2016-08-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "176": {"amount": -20, "category": "Myki", "date": "2016-08-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "177": {"amount": -11.8, "category": "Groceries", "date": "2016-08-01 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "178": {"amount": -19, "category": "Phone", "date": "2016-08-03 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "179": {"amount": -150, "category": "Clothes & Shoes", "date": "2016-08-03 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "180": {"amount": -1.5, "category": "Books", "date": "2016-08-04 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "181": {"amount": -4.2, "category": "Business & Education", "date": "2016-08-04 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "182": {"amount": -2.85, "category": "Groceries", "date": "2016-08-04 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "183": {"amount": -10, "category": "Lunch & Dinners", "date": "2016-08-04 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "184": {"amount": -18.63, "category": "Groceries", "date": "2016-08-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "185": {"amount": -10.5, "category": "Food & Beverage", "date": "2016-08-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "186": {"amount": -288, "category": "Business & Education", "date": "2016-08-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "187": {"amount": -31, "category": "Electronics", "date": "2016-08-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "188": {"amount": -27.95, "category": "Games", "date": "2016-08-05 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "189": {"amount": -10.5, "category": "Lunch & Dinners", "date": "2016-08-06 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "190": {"amount": -9.5, "category": "Lunch & Dinners", "date": "2016-08-06 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "191": {"amount": -10.5, "category": "Entertainment", "date": "2016-08-08 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "192": {"amount": -32, "category": "Activities & Outings", "date": "2016-08-08 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "193": {"amount": -8.5, "category": "Lunch & Dinners", "date": "2016-08-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "194": {"amount": -0.75, "category": "Groceries", "date": "2016-08-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "195": {"amount": -15, "category": "Clothes & Shoes", "date": "2016-08-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "196": {"amount": -40, "category": "Groceries", "date": "2016-08-10 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "197": {"amount": -10, "category": "Myki", "date": "2016-08-11 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "198": {"amount": 120, "category": "Salary", "date": "2016-08-11 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "199": {"amount": -10.8, "category": "Lunch & Dinners", "date": "2016-08-12 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "200": {"amount": -41, "category": "Personal Care", "date": "2016-08-13 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "201": {"amount": 2863, "category": "Salary", "date": "2016-08-13 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "202": {"amount": -20, "category": "Myki", "date": "2016-08-14 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "203": {"amount": -101, "category": "Groceries", "date": "2016-08-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "204": {"amount": -200, "category": "To Savings", "date": "2016-08-15 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "205": {"amount": -70, "category": "Phone", "date": "2016-08-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "206": {"amount": -254, "category": "To Savings", "date": "2016-08-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "207": {"amount": -14.14, "category": "Business & Education", "date": "2016-08-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "208": {"amount": -15, "category": "Clothes & Shoes", "date": "2016-08-16 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "209": {"amount": -10, "category": "Myki", "date": "2016-08-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "210": {"amount": -137.6, "category": "Accessories & Make Up", "date": "2016-08-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "211": {"amount": -25.71, "category": "Personal Care", "date": "2016-08-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "212": {"amount": -18, "category": "Clothes & Shoes", "date": "2016-08-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "213": {"amount": 370.1, "category": "Salary", "date": "2016-08-18 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "214": {"amount": -24, "category": "Lunch & Dinners", "date": "2016-08-19 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "215": {"amount": -12, "category": "Lunch & Dinners", "date": "2016-08-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "216": {"amount": -14, "category": "Food & Beverage", "date": "2016-08-20 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "217": {"amount": -50, "category": "Lunch & Dinners", "date": "2016-08-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "218": {"amount": -6.1, "category": "Groceries", "date": "2016-08-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "219": {"amount": -10, "category": "Myki", "date": "2016-08-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "220": {"amount": -34, "category": "Lunch & Dinners", "date": "2016-08-21 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "221": {"amount": -94, "category": "Credit Card", "date": "2016-08-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "222": {"amount": -8.2, "category": "Coffee & Snacks", "date": "2016-08-22 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "223": {"amount": -13, "category": "Lunch & Dinners", "date": "2016-08-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "224": {"amount": -5.6, "category": "Groceries", "date": "2016-08-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "225": {"amount": -155, "category": "Sports", "date": "2016-08-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "226": {"amount": -18, "category": "Lunch & Dinners", "date": "2016-08-24 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "227": {"amount": -150, "category": "Credit Card", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "228": {"amount": -1216, "category": "Rent", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "229": {"amount": -59.99, "category": "Internet", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "230": {"amount": -79, "category": "Lunch & Dinners", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "231": {"amount": -10, "category": "Myki", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "232": {"amount": -10, "category": "Presents & Donations", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "233": {"amount": -55, "category": "Presents & Donations", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "234": {"amount": -5, "category": "Entertainment", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "235": {"amount": 187.05, "category": "Salary", "date": "2016-08-25 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "236": {"amount": -4, "category": "Coffee & Snacks", "date": "2016-08-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "237": {"amount": -10, "category": "Myki", "date": "2016-08-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"},
  "238": {"amount": -27.98, "category": "Presents & Donations", "date": "2016-08-26 00:00:00", "wallet": "Cash", "note": null, "currency": "AUD"}
}


class jsontest(unittest.TestCase):
    def test(self):
        test, hdr = loadMLWorkbook("../sample.xlsx")
        js = ls_to_json(test)
        assert js == testjson