from flask import Flask, render_template 
import json
import os

# 自動切換到 app.py 所在資料夾
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("目前工作目錄:", os.getcwd())

app = Flask(__name__)

# 載入產品資料
def load_products():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("錯誤：找不到 products.json！")
        return []
    except json.JSONDecodeError as e:
        print("JSON 解析錯誤：", e)
        return []

# 根據 category 分類商品
def categorize_products(products):
    categorized = {}
    for product in products:
        category = product.get("category", "其他")
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(product)
    return categorized

@app.route('/')
def index():
    products = load_products()
    categorized = categorize_products(products)
    return render_template('index.html', categorized=categorized)

if __name__ == '__main__':
    app.run(debug=True)
