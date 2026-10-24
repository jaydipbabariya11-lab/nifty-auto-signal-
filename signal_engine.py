from dataclasses import dataclass
from math import floor
import math

@dataclass
class Signal:
    side: str
    reason: str

def evaluate_signal(spot, upper, lower, trend15, breakout5, retest5, oi_bias,
                    daily_loss, daily_limit, data_fresh=False):
    if not data_fresh:
        return Signal("WAIT", "Data freshness verified नहीं है")
    if daily_loss >= daily_limit:
        return Signal("STOP", "Daily loss limit reached")
    if spot > upper and trend15 == "bull" and breakout5 == "bull" and retest5 == "bull" and oi_bias != "bear":
        return Signal("BUY CALL SETUP", "15m bullish + 5m breakout/retest + OI विरोध नहीं")
    if spot < lower and trend15 == "bear" and breakout5 == "bear" and retest5 == "bear" and oi_bias != "bull":
        return Signal("BUY PUT SETUP", "15m bearish + 5m breakdown/retest + OI विरोध नहीं")
    return Signal("WAIT", "सभी confirmation शर्तें पूरी नहीं")

def position_size(capital, risk_pct, entry, stop, lot_size, daily_loss, daily_limit):
    if min(capital, risk_pct, entry, stop, lot_size) <= 0:
        return {"error": "Inputs positive होने चाहिए"}
    if stop >= entry:
        return {"error": "Long option के लिए stop premium entry से कम होना चाहिए"}
    if daily_loss >= daily_limit:
        return {"risk_budget": 0, "units": 0, "lots": 0, "quantity": 0}
    budget = min(capital * risk_pct / 100, daily_limit - daily_loss)
    units = floor(budget / (entry - stop))
    lots = floor(units / lot_size)
    return {"risk_budget": round(budget, 2), "per_unit_risk": round(entry-stop, 2),
            "one_lot_risk": round((entry-stop)*lot_size, 2), "lots": lots,
            "quantity": lots*lot_size, "planned_premium_risk": round(lots*lot_size*(entry-stop), 2)}

def square_of_9_reference(price):
    if price <= 0: raise ValueError("price must be positive")
    r = math.sqrt(price)
    return {"minus_90": round((r-.25)**2,2), "minus_45": round((r-.125)**2,2),
            "base": round(price,2), "plus_45": round((r+.125)**2,2),
            "plus_90": round((r+.25)**2,2)}
