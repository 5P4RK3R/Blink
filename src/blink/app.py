"""
An app to remind user to blink their eyes and relax
"""
import cv2
import toga
from toga import App, Window, Image
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Blink(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

# class CameraApp(App):
#     def startup(self):
#         self.window = Window(title="Camera Feed", size=(800, 600))
#         # self.image_view = Image()
#         # self.window.content = self.image_view

#         # Open the camera
#         self.cap = cv2.VideoCapture(0)

#         # Start the camera capture loop
#         self.capture_loop()

#     def capture_loop(self):
#         # Read a frame from the camera
#         ret, frame = self.cap.read()

#         # if ret:
#             # Convert the frame from BGR to RGB
#             # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             # Convert the frame to a format suitable for Toga's Image widget
#             # image_bytes = cv2.imencode('.png', frame_rgb)[1].tobytes()

#             # Set the image data to the Image widget
#             # self.image_view.value = image_bytes

#         # Schedule the next frame capture
#         self.window.app.set_timeout(1/30, self.capture_loop)

#     def shutdown(self):
#         # Release the camera
#         self.cap.release()


def main():
    return Blink()

