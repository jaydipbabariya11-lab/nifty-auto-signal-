"""Angel One SmartAPI login/helper scaffold. Verify current official SDK signatures."""
import os
from dotenv import load_dotenv
load_dotenv()

def create_session():
    required = ["ANGEL_API_KEY", "ANGEL_CLIENT_CODE", "ANGEL_PIN", "ANGEL_TOTP_SECRET"]
    missing = [k for k in required if not os.getenv(k)]
    if missing: raise RuntimeError("Missing local .env settings: " + ", ".join(missing))
    import pyotp
    from SmartApi import SmartConnect
    api = SmartConnect(api_key=os.environ["ANGEL_API_KEY"])
    otp = pyotp.TOTP(os.environ["ANGEL_TOTP_SECRET"]).now()
    result = api.generateSession(os.environ["ANGEL_CLIENT_CODE"], os.environ["ANGEL_PIN"], otp)
    if not result or not result.get("status"): raise RuntimeError(f"Angel One login failed: {result}")
    return api, result

def get_historical_candles(api, exchange, symbol_token, interval, from_date, to_date):
    params = {"exchange": exchange, "symboltoken": str(symbol_token), "interval": interval,
              "fromdate": from_date, "todate": to_date}
    return api.getCandleData(params)

def place_order_after_confirmation(api, order_params, confirmed=False, paper_mode=True):
    if not confirmed: raise PermissionError("Order नहीं भेजा: explicit confirmation नहीं मिली")
    if paper_mode: return {"paper": True, "message": "Simulated; broker को order नहीं भेजा"}
    return api.placeOrder(order_params)
