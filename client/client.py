from classes import MainController

mc = MainController()

running = True
while running:
    running = mc.handle_event()

