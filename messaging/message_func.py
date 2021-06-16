import threading
import time

def listenForMessages():
    while True:
        print("waiting...\n");
        time.sleep(2);
    
def app():
    while True:
        print("running...");
        time.sleep(0.02);
        
        
message_listener = threading.Thread(target=listenForMessages);
app_thread = threading.Thread(target=app);


app_thread.start();
message_listener.start();
