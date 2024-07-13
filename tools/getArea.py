from pynput import mouse

listener = None
start_position = None
end_position = None


def on_click(x, y, button, pressed):
    global start_position, end_position
    if pressed:
        start_position = (x, y)
    else:
        end_position = (x, y)
        return False


def get_area():
    global start_position, end_position, listener
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return start_position + end_position
