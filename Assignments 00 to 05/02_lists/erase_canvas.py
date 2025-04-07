# Erase the canvas by calling the erase() method of the Canvas class.:
import time

class Canvas:
    def set_canvas_title(self, title):
        print(f"Canvas title set to: {title}")
    
    def set_canvas_size(self, width, height):
        print(f"Canvas size set to: {width}x{height}")
    
    def set_canvas_background(self, color):
        print(f"Canvas background set to: {color}")
    
    def create_rectangle(self, x1, y1, x2, y2, fill_color):
        print(f"Rectangle created with fill color: {fill_color}")
    
    def update(self):
        print("Canvas updated.")
    
    def erase(self):
        print("Canvas erased.")
    
    def wait(self):
        print("Waiting for user action...")

def main():
    canvas = Canvas()
    canvas.set_canvas_title("Erase Canvas")
    canvas.set_canvas_size(400, 400)
    canvas.set_canvas_background("white")

    canvas.create_rectangle(50, 50, 350, 350, fill_color="red")
    canvas.update()

    time.sleep(2)
    canvas.erase()

    canvas.update()
    canvas.wait()
main()
