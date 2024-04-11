from flask import Flask, request
from pathlib import Path
from datetime import date
from decimal import Decimal
from calculadora_do_cidadao import Ipca

ipca_data = Path("IPCA.csv")

ipca = Ipca()
ipca.to_csv(ipca_data)

app = Flask(__name__)

@app.route("/ipca", methods=['POST'])
def ipca():
    data = request.get_json()
    start_date = date.fromisoformat(data['start_date'])
    value = Decimal(data['value'])
    end_date = date.fromisoformat(data['end_date'])
  
    ipca = Ipca(ipca_data)
    new_value = ipca.adjust(start_date, value, end_date)
    percent = (new_value - value) / value * 100

    return { 'new_value': new_value, 'percentage': percent }

if __name__ == '__main__':
    app.run(debug=True)