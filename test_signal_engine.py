from signal_engine import evaluate_signal, position_size

def test_call_setup():
    assert evaluate_signal(23000,22850,22450,"bull","bull","bull","neutral",0,1000,True).side == "BUY CALL SETUP"

def test_stale_data_blocks():
    assert evaluate_signal(23000,22850,22450,"bull","bull","bull","neutral",0,1000,False).side == "WAIT"

def test_daily_limit_stops():
    assert evaluate_signal(23000,22850,22450,"bull","bull","bull","neutral",1000,1000,True).side == "STOP"

def test_sizing():
    r=position_size(50000,1,120,110,65,0,1000)
    assert r["risk_budget"] == 500 and r["lots"] == 0
