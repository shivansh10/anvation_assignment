## Program for leveraging Cognitive service APIs mentioned below to accept audio file or mic based speech as input, to identify user intent and/or sentiment of texts. 

### 1. main.py 
Run **main.py** for output.

### 2. predictLUIS.py
The model is been build on [www.luis.ai](www.luis.ai) using few amount of intents added to it along with two entities 

a. name of smartphone  
b. cost of smartphone.

### 3. sentiment_analysis.py
Contains the Azure cognitive service API which classify texts into three classes thus, giving the sentiment of the text. 

### 4. speech_to_text.py
Converts the speech to text by using Azure Speech API. It takes input in two of the following ways:

a. speech_recognize_continuous_from_file : Takes input as a file.

b. speech_recognize_continuous_from_microphone : Takes input directly from microphone. 
