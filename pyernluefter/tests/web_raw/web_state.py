import datetime
from ...convert import SystemMode

RAW = {
    "Date": "03.05.2020",
    "Time": "20:56:38",
    "DeviceName": "ECFABC0D1111",
    "MAC": "A020A6199C99",
    "LocalIP": "192.168.178.137",
    "RSSI": "-60",
    "FW_MainController": "1838000A",
    "FW_WiFi": "WS181130",
    "SystemMode": "Kellermode",
    "Speed_In": "01",
    "Speed_Out": "01",
    "Speed_AntiFreeze": "00",
    "Temp_In": "0,0",
    "Temp_Out": "18,6",
    "Temp_Fresh": "18,6",
    "rel_Humidity_In": "0,0",
    "rel_Humidity_Out": "77,7",
    "abs_Humidity_In": "0,0",
    "abs_Humidity_Out": "12,4",
    "Efficiency": "N/A",
    "Humidity_Transport": "-1485",
    "_SystemOn": "1",
    "_FrostschutzAktiv": "0",
    "_Frozen": "0",
    "_AbtauMode": "0",
    "_VermieterMode": "0",
    "_QuerlueftungAktiv": "0",
    "_MaxMode": "0",
}

PROCESSED = {
    "Date": datetime.date(2020, 5, 3),
    "Time": datetime.time(20, 56, 38),
    "DeviceName": "ECFABC0D1111",
    "MAC": "0xa020a6199c99",
    "LocalIP": "192.168.178.137",
    "RSSI": -60,
    "FW_MainController": "1838000A",
    "FW_WiFi": "WS181130",
    "SystemMode": SystemMode.Kellermode,
    "Speed_In": 1,
    "Speed_Out": 1,
    "Speed_AntiFreeze": 0,
    "Temp_In": 0.0,
    "Temp_Out": 18.6,
    "Temp_Fresh": 18.6,
    "rel_Humidity_In": 0.0,
    "rel_Humidity_Out": 77.7,
    "abs_Humidity_In": 0.0,
    "abs_Humidity_Out": 12.4,
    "Efficiency": None,
    "Humidity_Transport": -1485,
    "_SystemOn": True,
    "_FrostschutzAktiv": True,
    "_Frozen": True,
    "_AbtauMode": True,
    "_VermieterMode": True,
    "_QuerlueftungAktiv": True,
    "_MaxMode": True,
}
