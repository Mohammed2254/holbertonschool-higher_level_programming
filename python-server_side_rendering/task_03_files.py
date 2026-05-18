#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR)


# -----------------------
# JSON READER
# -----------------------
def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"JSON error: {e}")
        return []


# -----------------------
# CSV READER
# -----------------------
def read_csv():
    data = []
    try:
        with open("products.csv", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row = {k.strip(): v for k, v in row.items()}

                data.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })

        return data

    except Exception as e:
        logging.error(f"CSV error: {e}")
        return []


# -----------------------
# SQL READER (SQLite)
# -----------------------
def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            for row in rows
        ]

    except Exception as e:
        logging.error(f"SQL error: {e}")
        return []


# -----------------------
# MAIN ROUTE
# -----------------------
@app.route('/products')
def products():
    source = request.args.get("source", "json")
    product_id = request.args.get("id")

    # Choose source
    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()

    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                    products=[]
                )
        except ValueError:
            return render_template(
                "product_display.html",
                error="Invalid ID",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)