from main import window

@window.event
def on_draw():
    window.clear()

@window.event
def on_key_press(symbol, modifiers):
    print(f"{symbol}")

