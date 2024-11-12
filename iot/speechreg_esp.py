# text input only code



# import speech_recognition as sr
# import serial
# import websocket
# import time
# import os

# r = sr.Recognizer()

# def send_command_to_esp32(command):
#     websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
#     ws = websocket.create_connection(websocket_url)
#     ws.send(command)
#     ws.close()

# def recognize_speech():
#     # with sr.Microphone() as source:
#     #     print("Say something!")
#     #     audio = r.listen(source)

#     try:
#         # text = r.recognize_google(audio)
#         # text = r.recognize_sphinx(audio)
#         text=input()

#         print("You said: " + text)
#         if "on" in text:
#             # ser.write(b'1')  # Sending '1' to turn on the LED
#             send_command_to_esp32("on")
#             print('Sent 1')
#         elif "off" in text:
#             # ser.write(b'0')  # Sending '0' to turn off the LED
#             send_command_to_esp32("off")
#             print('Sent 0')
# #
#     except:
#         print(10)
#     # except sr.UnknownValueError:
#     #     print("Google Speech Recognition could not understand audio")
#     # except sr.RequestError as e:
#     #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Continuously listen for speech
# send_command_to_esp32("off")
# while True:
#     recognize_speech()


# with dgx server and speech

# import speech_recognition as sr
# import serial
# import websocket
# import time
# import os
# import requests

# url = "http://dgx.kmitonline.in:4000"


# r = sr.Recognizer()

# def send_command_to_esp32(command):
#     websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
#     ws = websocket.create_connection(websocket_url)
#     ws.send(command)
#     ws.close()

# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         # text = r.recognize_sphinx(audio)
#         print("You said: " + text)

#         payload = {"input": text}
#         response = requests.post(url, json=payload)

#         if response.status_code == 200:
#             data = response.json()
#             output = data.get("output")
#             if output is not None:
#                 if output == "1":
#                     send_command_to_esp32("on")
#                     print('Sent 1')
#                 else:
#                     send_command_to_esp32("off")
#                     print('Sent 0')
#             else:
#                 print("Invalid response format")
#         else:
#             print("Failed to send request. Status code:", response.status_code)

        


#         # if "on" in text:
#         #     # ser.write(b'1')  # Sending '1' to turn on the LED
#         #     send_command_to_esp32("on")
#         #     print('Sent 1')
#         # elif "off" in text:
#         #     # ser.write(b'0')  # Sending '0' to turn off the LED
#         #     send_command_to_esp32("off")
#         #     print('Sent 0')


#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Continuously listen for speech
# # send_command_to_esp32("off")
# while True:
#     recognize_speech()                     

# only on and off with speech recognition

# import speech_recognition as sr
# import serial
# import websocket
# import time
# import os

# r = sr.Recognizer()

# def send_command_to_esp32(command):
#     websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
#     ws = websocket.create_connection(websocket_url)
#     ws.send(command)
#     ws.close()

# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         # text = r.recognize_sphinx(audio)
        

#         print("You said: " + text)
#         if "on" in text:
#             # ser.write(b'1')  # Sending '1' to turn on the LED
#             send_command_to_esp32("on")
#             print('Sent 1')
#         elif "off" in text:
#             # ser.write(b'0')  # Sending '0' to turn off the LED
#             send_command_to_esp32("off")
#             print('Sent 0')


#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Continuously listen for speech
# send_command_to_esp32("off")
# while True:
#     recognize_speech()










# dgx server without speech working

import speech_recognition as sr
import serial
import websocket
import time
import os
import requests

url = "http://dgx.kmitonline.in:4000"


r = sr.Recognizer()

def send_command_to_esp32(command):
    websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
    ws = websocket.create_connection(websocket_url)
    ws.send(command)
    ws.close()

def recognize_speech():
    # with sr.Microphone() as source:
    #     print("Say something!")
    #     audio = r.listen(source)

    try:
        # text = r.recognize_google(audio)
        text=input()
        # text = r.recognize_sphinx(audio)
        print("You said: " + text)


        payload = {"input": text}
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            output = data.get("output")
            if output is not None:
                if output == "1":
                    send_command_to_esp32("on")
                    print('Sent 1')
                else:
                    send_command_to_esp32("off")
                    print('Sent 0')
            else:
                print("Invalid response format")
        else:
            print("Failed to send request. Status code:", response.status_code)

        


        # if "on" in text:
        #     # ser.write(b'1')  # Sending '1' to turn on the LED
        #     send_command_to_esp32("on")
        #     print('Sent 1')
        # elif "off" in text:
        #     # ser.write(b'0')  # Sending '0' to turn off the LED
        #     send_command_to_esp32("off")
        #     print('Sent 0')

    except:
        print(10)
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Continuously listen for speech
# send_command_to_esp32("off")
while True:
    recognize_speech()     


# dgx server with speech recognition working

# import speech_recognition as sr
# import serial
# import websocket
# import time
# import os
# import requests

# url = "http://dgx.kmitonline.in:4000"


# r = sr.Recognizer()

# def send_command_to_esp32(command):
#     websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
#     ws = websocket.create_connection(websocket_url)
#     ws.send(command)
#     ws.close()

# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         # text=input()
#         # text = r.recognize_sphinx(audio)
#         print("You said: " + text)

#         payload = {"input": text}
#         response = requests.post(url, json=payload)

#         if response.status_code == 200:
#             data = response.json()
#             output = data.get("output")
#             if output is not None:
#                 if output == "1":
#                     send_command_to_esp32("on")
#                     print('Sent 1')
#                 else:
#                     send_command_to_esp32("off")
#                     print('Sent 0')
#             else:
#                 print("Invalid response format")
#         else:
#             print("Failed to send request. Status code:", response.status_code)

        


#         # if "on" in text:
#         #     # ser.write(b'1')  # Sending '1' to turn on the LED
#         #     send_command_to_esp32("on")
#         #     print('Sent 1')
#         # elif "off" in text:
#         #     # ser.write(b'0')  # Sending '0' to turn off the LED
#         #     send_command_to_esp32("off")
#         #     print('Sent 0')

#     # except:
#     #     print(10)
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Continuously listen for speech
# # send_command_to_esp32("off")
# while True:
#     recognize_speech()     