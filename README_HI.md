# NIFTY Angel One Auto Signal — Starter Project

स्थिति: सुरक्षित starter/scaffold; production-ready नहीं। डिफ़ॉल्ट PAPER_MODE=true है और यह अपने-आप कोई ऑर्डर नहीं भेजता।

## चलाने का तरीका
1. Python 3.10+ इंस्टॉल करें।
2. ZIP extract करें और project folder में जाएँ।
3. `pip install -r requirements.txt`
4. `.env.example` की copy `.env` नाम से बनाकर credentials अपने कंप्यूटर पर भरें।
5. `streamlit run app.py`

किसी को API key, PIN, TOTP secret, JWT/feed token न भेजें और इन्हें GitHub पर upload न करें।

## अभी क्या काम करता है
- Hindi Streamlit dashboard
- 15m trend + 5m breakout/retest rule checks
- Gann Square-of-9 के approximate reference levels
- Premium stop-loss से risk/lot sizing
- Daily loss cutoff और order confirmation gate
- Paper-mode order review

## अभी क्या अधूरा है
Live WebSocket tick-to-candle aggregation, current instrument-master से option expiry/strike/token selection, option-chain OI feed, reconnect/recovery, broker order-state reconciliation और production order placement को वास्तविक खाते पर जाँचना बाकी है। Dashboard manual inputs पर आधारित है; यह अभी live-connected signal नहीं है।

Risk budget = capital × risk %. Quantity = risk budget / (entry premium − stop premium), फिर actual lot size पर नीचे round होता है। Brokerage, taxes, spread, slippage, rejected/partial orders और gaps के कारण वास्तविक नुकसान अधिक हो सकता है। Daily loss cutoff तभी विश्वसनीय है जब P&L सही update हो; इसे broker-side kill switch न समझें।

Official docs: https://smartapi.angelone.in/docs
Official SDK: https://github.com/angel-one/smartapi-python

पहले paper trade/backtest करें; live order integration को सुरक्षित backend, current broker requirements और explicit per-order confirmation के बाद ही enable करें।
