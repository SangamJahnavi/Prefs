import speech_recognition as sr
import websocket
import time

r = sr.Recognizer()

def send_command_to_esp32(command):
    websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
    ws = websocket.create_connection(websocket_url)
    ws.send(command)
    ws.close()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # Use PocketSphinx for speech recognition
        text = r.recognize_sphinx(audio)
        print("You said: " + text)

        if "on" in text:
            send_command_to_esp32("on")
            print('Sent 1')
        elif "off" in text:
            send_command_to_esp32("off")
            print('Sent 0')

    except sr.UnknownValueError:
        print("PocketSphinx could not understand audio")
    except sr.RequestError as e:
        print("PocketSphinx error; {0}".format(e))

# Continuously listen for speech
while True:
    recognize_speech()