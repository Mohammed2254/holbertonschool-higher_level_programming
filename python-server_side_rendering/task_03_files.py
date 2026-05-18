#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# ---------------- JSON ----------------
def read_json():
    with open("products.json", "r") as f:
        return json.load(f)


# ---------------- CSV ----------------
def read_csv():
    products = []

    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if "id" not in row:
                continue

            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

    return products


# ---------------- ROUTE ----------------
@app.route("/products")
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []
    error = None

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

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if int(p["id"]) == product_id]

            if not data:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                    products=[]
                )

        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=data,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)