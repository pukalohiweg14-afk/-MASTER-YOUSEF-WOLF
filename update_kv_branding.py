#!/usr/bin/env python3
"""Update wolf_state (announcement banner with support IDs) and panel_settings
(telegram field pointing to support) via KV. Safe — no code edits."""
import json
import subprocess
import time
import sys

CF_TOKEN = "cfut_UY0gGYg0kaVUbd2DqTcP2ztgMGz0dZ2pXCrp0Gbhb3e9233c"
ACCOUNT_ID = "90b167a62cd32cbadc577515649e328d"
KV_NS = "2201c97b22f246af9863c188eac94658"

BASE = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/storage/kv/namespaces/{KV_NS}"

def api(method, path, data=None):
    cmd = ["curl", "-s", "-X", method, f"{BASE}{path}",
           "-H", f"Authorization: Bearer {CF_TOKEN}",
           "-H", "Content-Type: application/json"]
    if data is not None:
        cmd += ["--data", data]
    return subprocess.check_output(cmd).decode("utf-8")

# --- 1) Update wolf_state: set a prominent announcement with support IDs ---
raw = api("GET", "/values/wolf_state")
state = json.loads(raw)
print("BEFORE wolf_state.announce:", state.get("announce"))

state["announce"] = {
    "on": True,
    "text": "🐺 MASTER YOUSEF WOLF EMPIRE — پشتیبانی: @Kmnbvczx0090 | @vpnstan2 👑",
    "at": int(time.time() * 1000)
}
state["_updatedAt"] = int(time.time() * 1000)
body = json.dumps(state, ensure_ascii=False)
resp = api("PUT", "/values/wolf_state", body)
print("wolf_state write:", json.loads(resp).get("success"))

# --- 2) Update panel_settings: telegram field + tgBotUrl ---
raw2 = api("GET", "/values/panel_settings")
settings = json.loads(raw2)
print("BEFORE panel_settings.telegram:", settings.get("telegram"))
print("BEFORE panel_settings.tgBotUrl:", settings.get("tgBotUrl"))

# Keep the telegram channel link, but the panel reads this for the "telegram" display.
# We'll set it to a combined string with both support IDs.
settings["telegram"] = "https://t.me/Kmnbvczx0090 | https://t.me/vpnstan2"
settings["tgBotUrl"] = "https://panel-silence3.panel-silence.workers.dev" + settings.get("tgBotUrl","").split("workers.dev",1)[-1]
settings["updatedAt"] = int(time.time() * 1000)
body2 = json.dumps(settings, ensure_ascii=False)
resp2 = api("PUT", "/values/panel_settings", body2)
print("panel_settings write:", json.loads(resp2).get("success"))

# --- 3) Verify ---
time.sleep(3)
chk = json.loads(api("GET", "/values/wolf_state"))
print("AFTER wolf_state.announce:", chk.get("announce"))
chk2 = json.loads(api("GET", "/values/panel_settings"))
print("AFTER panel_settings.telegram:", chk2.get("telegram"))
print("AFTER panel_settings.panelPass:", chk2.get("panelPass"))
print("AFTER panel_settings.tgBotUrl:", chk2.get("tgBotUrl"))
