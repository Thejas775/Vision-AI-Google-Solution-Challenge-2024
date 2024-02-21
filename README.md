## VISION AI 
While sighted individuals can directly experience the world’s beauty, those with visual impairments often depend on others to narrate their environment. But what if their loved ones aren’t present? To tackle this, we’re creating a solution that acts as a perpetual companion for the visually impaired. Similar to a friend, our solution will verbally describe everything to them, and they can inquire about any aspect of the image. This ensures they never feel isolated or unsupported. This is the core of our project for the upcoming hackathon, where we aim to profoundly impact the lives of visually impaired individuals.

This project demonstrates a multimodal AI system that integrates speech recognition, facial recognition, image compression, and text-to-speech functionalities.

**Requirements:**

* Python 3.x
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

* `record_audio.py`: Records audio and converts it to text.
* `find_match.py`: Performs facial recognition using DeepFace.
* `text_to_speech.py`: Converts text to audio using gTTS.
* `call_api_with_gemini.py`: Calls Google's GenerativeAI model to generate text and images.
* `compress_image.py`: Compresses images to reduce size.
* `capture_image.py`: Captures image from the camera and compresses it.
* `main.py`: Runs the main program loop and interacts with other modules.

**Usage:**

1. Install required libraries using `pip install -r requirements.txt`.
2. Place your image database in the `images` folder.
3. Run `python main.py`.
4. The program will guide you through recording audio, facial recognition, and interacting with the API.

**Additional Notes:**

* This is a basic implementation and can be further customized and extended.
* Consider ethical implications and responsible use of facial recognition technology.
* Ensure proper API key and authentication for the GenerativeAI model.

**I hope this README provides a clear overview of the project. Feel free to reach out if you have any questions!**
