from . import app

@app.handle(intent='greet')
def welcome(request, responder):
    responder.reply('Hello')