import time 
def timer():
    current_time = 0    #creates timer variable to count in seconds
    for i in range(0, 5):
        for i in range(0,10):
         time.sleep(0.1)
        current_time += 100
        print("Output to GUI:", current_time)
    def convert():
        if current_time >= 60:
         print("yes")
        else:
            print("no")
    convert()

       


timer()
