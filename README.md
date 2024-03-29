## VISION AI 
While sighted individuals can directly experience the world’s beauty, those with visual impairments often depend on others to narrate their environment. But what if their loved ones aren’t present? To tackle this, we’re creating a solution that acts as a perpetual companion for the visually impaired. Similar to a friend, our solution will verbally describe everything to them, and they can inquire about any aspect of the image. This ensures they never feel isolated or unsupported. This is the core of our project for the GDSC Solution Challenge, where we aim to profoundly impact the lives of visually impaired individuals.

This project demonstrates a multimodal AI system that integrates speech recognition, facial recognition, and text-to-speech functionalities.

## Architecture
![Screenshot (89)](https://github.com/Thejas775/Vision-AI-Google-Solution-Challenge-2024/assets/114435001/085e3e68-5409-4d5c-8700-3cb0654f1029)

**Setup:**
* Install any OS in Raspberry Pi.
* Attach USB microphone and Raspberry Pi camera
* Make a virtual environment for better package handling
* Install all the requirements
* Run the python file in the virtual environment.

**Requirements:**

* deepface
* Pillow
* opencv-python
* google-generativeai
* SpeechRecognition
* gtts

**Features:**

* **Record audio:** Captures audio input and converts it to text using Google Speech Recognition.
* **Facial recognition:** Identifies people in images using DeepFace and compares them to known faces in a database.
* **Text-to-speech:** Converts text to audio using gTTS.
* **Image compression:** Reduces the size of images while maintaining quality.
* **API call with Gemini:** Generates text and images using Google's GenerativeAI model.

**Code Structure:**

* `record_audio`: Records audio and converts it to text.
* `find_match`: Performs facial recognition using DeepFace.
* `text_to_speech`: Converts text to audio using gTTS.
* `call_api_with_gemini`: Calls Google's GenerativeAI model to generate text and images.
* `capture_image`: Captures image from the camera.
* `compress_image`: Compresses images to reduce size.
* `main`: Runs the main program loop and interacts with other modules.

**Usage:**

1. Install required libraries using `pip install -r requirements.txt`.
2. Substitute `Your Gemini api key` with your actual Gemini API key. 
3. Run `python main.py`.
4. To use Facial recognition ,put your image database in the `images` folder.

