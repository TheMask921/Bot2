from dhooks import Webhook, Embed
hook = Webhook("https://discord.com/api/webhooks/1026793125483659284/hLbMuKTQ963su39WVK0TGHPRBPAPaElkjM_t8O914lT-N5504ycwsB7oCh8Q4P-_WXyD") 

data = input ("Enter something: ")
hook.send(data)