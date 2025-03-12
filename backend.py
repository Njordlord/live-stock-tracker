import yfinance as yf
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app) 

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_data(ticker):
    
    try:
        
        stock = yf.Ticker(ticker)
        
        data = stock.history(period="1d")
        if data.empty:
            return jsonify({"error": f"No data found for ticker: {ticker}"}), 404
        last_price = data["Close"].iloc[-1]
       
        timestamp = pd.Timestamp.now().isoformat()
        return jsonify({
            "ticker": ticker,
            "price": float(last_price),
            "timestamp": timestamp
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    
    app.run(debug=True)








