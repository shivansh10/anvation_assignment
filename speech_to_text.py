
#importing libraries
import glob
import azure.cognitiveservices.speech as speechsdk
import time

speech_config = speechsdk.SpeechConfig(subscription="9a91a17646c447888d8b0d2bbfe3402e", region="eastus")

#from an audio file
def speech_recognize_continuous_from_file(file):

    audio_config = speechsdk.audio.AudioConfig(filename=file)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
    
    #input the converted text into list
    all_results = []
    def handle_final_result(evt):
        all_results.append(evt.result.text)

    speech_recognizer.recognized.connect(handle_final_result)

    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)
    
    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    #return ouput
    return all_results


#from Microphone

def speech_recognize_continuous_from_microphone():
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print()
    print()
    print("Speak into your microphone.")

    result = speech_recognizer.recognize_once_async().get()
    output = result.text
    
    print()
    print(output)

    results = []
    results.append(output)
    return results


