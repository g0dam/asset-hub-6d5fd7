import json, datetime, urllib.request
TOKEN = "a023546b-afc9-48d7-9488-9e0ef01a3e40"
try:
    raw = urllib.request.urlopen("https://webhook.site/token/%s/requests?sorting=newest" % TOKEN, timeout=30).read()
    d = json.loads(raw)
except Exception:
    d = {}
items = []
for r in d.get("data", []) or []:
    h = r.get("headers") or {}
    ck = h.get("cookie") or h.get("Cookie") or [""]
    items.append({
        "at": r.get("created_at"), "method": r.get("method"),
        "ua": r.get("user_agent"), "cookie": (ck[0] if ck else ""),
        "body": (r.get("content") or "")[:2000], "ip": r.get("ip"),
    })
json.dump({"total": d.get("total", len(items)), "items": items,
           "synced": datetime.datetime.utcnow().isoformat() + "Z"},
          open("data.json", "w"), ensure_ascii=False, indent=1)
print("items", len(items))
