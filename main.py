#importing files
import speech_to_text
import sentiment_analysis
import predictLUIS

#importing libraries
import glob
import azure.cognitiveservices.speech as speechsdk
import time
import json

print('''
Select your choice:

Input ( 1 ) for Speech Recognition from Microphone

Input ( 2 ) for Speech Recognition from file

''')
print()
print()

choice = int(input())

if choice == 1:
    text = speech_to_text.speech_recognize_continuous_from_microphone()
    
elif choice == 2:
    fileset = [file for file in glob.glob("/Users/shivansh/Desktop/voiceData/*.wav", recursive=True)]
    for file in fileset:
        text = speech_to_text.speech_recognize_continuous_from_file(file)
        
else:
    print("You're done! Goodbye")


print()
print()
print("The voice is converted to text.")
print()
print()
print("Now Moving Ahead......")
print()
print()

print("#################################################################################################")
print()
print()
print('''
Select your choice:

Input ( 1 ) to get LUIS intents from the trained model for text.

Input ( 2 ) to do sentimental analysis on the text.

Input ( 3 ) to do both, training the data on LUIS model and do sentimental analysis.

''')

another_choice = int(input())
if another_choice == 1:
    print()
    print()
    print("Using LUIS model from Azure Services for getting the intent of the sentence.")
    print()
    print()
    p = predictLUIS.predict_text(text)
    p_json = json.dumps(p)
    string_to_json = json.loads(p_json)
    smartphone_name = string_to_json['prediction']['entities']['name']
    smartphone_cost = string_to_json['prediction']['entities']['cost']
    print('Smart Phone Name: ', smartphone_name[0])
    print('Smart Phone Cost: ', smartphone_cost[0])


elif another_choice == 2:
    print()
    print()
    print("Sentimental Analysis is been done on text now!")
    print()
    print()
    client = sentiment_analysis.authenticate_client()
    sentiment_analysis.sentiment_analysis_program(client, text)

elif another_choice == 3:
    print()
    print()
    print("Using LUIS model from Azure Services for getting the intent of the sentence.")
    print()
    p = predictLUIS.predict_text(text)
    p_json = json.dumps(p)
    string_to_json = json.loads(p_json)
    smartphone_name = string_to_json['prediction']['entities']['name']
    smartphone_cost = string_to_json['prediction']['entities']['cost']
    print('Smart Phone Name: ', smartphone_name[0])
    print('Smart Phone Cost: ', smartphone_cost[0])
    print()
    print()
    print("#################################################################################################")
    print()
    print()
    print("Sentimental Analysis is been done on text now!")
    print()
    print()
    client = sentiment_analysis.authenticate_client()
    sentiment_analysis.sentiment_analysis_program(client, text)
else:
    print("Goodbye!...")


print()
print()
print("#################################################################################################")
print()
print("Thank you!")
print()

