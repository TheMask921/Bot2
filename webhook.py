import json
from dhooks import Webhook, Embed

with open("webhook.json") as webhook:
    webhook = json.load(webhook)

hook = Webhook(webhook)
data = input ("Enter something: ")
hook.send(data)