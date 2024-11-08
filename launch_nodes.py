from multiprocessing import Process
from main_controller import MainController
from dual_servo_actuator import ServoControl
 
def launch_main_controller():
    controller = MainController(5,2) #v0,h
    controller.run()
 
def launch_servo_control():
    servo_control = ServoControl()
    servo_control.run()  # Optional if you want any continuous functionality here
 
if __name__ == "__main__":
    # Start only MainController and ServoControl
    processes = [
        Process(target=launch_main_controller),
        Process(target=launch_servo_control)
    ]
 
    # Start all processes
    for process in processes:
        process.start()
 
    # Join all processes
    for process in processes:
        process.join()
