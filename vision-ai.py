import os
import subprocess
import speech_recognition as sr
from gtts import gTTS
from time import sleep
from pathlib import Path
import google.generativeai as genai
from PIL import Image
from deepface import DeepFace
import cv2

def record_audio():
    #for recording audio
    r = sr.Recognizer()
    print("Before Recording")
    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5)
    print("After Recording")


    try:
        print("reached here")
        text = r.recognize_google(audio)
        print(text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def find_match(image_path):
    # Load the image 
    images_folder="images"
    test_image = cv2.imread(image_path)

    image_files = os.listdir(images_folder)

    for image_file in image_files:
        # Make path
        full_image_path = os.path.join(images_folder, image_file)
        image = cv2.imread(full_image_path)
        result = DeepFace.verify(test_image, image)
        if result["verified"]:
            text_to_speech(f"Match found The person is: {full_image_path}")
            print(f"Match found: {full_image_path}")
           
    else:
        text_to_speech("No match found")
        print("No match found.")

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    sleep(2)
    subprocess.run(["xdg-open","output.mp3"])

def call_api_with_gemini(prompt):

    genai.configure(api_key="Gemini-API-Key")

    # Set up the model
    generation_config = {
      "temperature": 0.4,
      "top_p": 1,
      "top_k": 32,
      "max_output_tokens": 4096,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    

    image_parts = [
      {
        "mime_type": "image/png",
        "data": Path("compressed_image.png").read_bytes()
      },
    ]

    prompt_parts = [
      prompt,
      image_parts[0],
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)
    text_to_speech(response.text)


def compress_image(input_path, output_path, scale_factor=0.5):
    # Image Compression as Gemini doesn't take images above 4mb
    try:
        with Image.open(input_path) as img:
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)
        print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_image(file_path='captured_image.png'):
    #For capturing image
    try:
        subprocess.run(['libcamera-still', '-e', 'png', '-o', file_path], check=True)
        print(f"Image captured and saved to {file_path}")
        compressed_file_path = 'compressed_image.png'
        compress_image(file_path, compressed_file_path)
        return compressed_file_path

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        command = record_audio()
        if command and ("hey vision" in command.lower() or "hello vision" in command.lower() or "vision" in command.lower()):
            print("Capturing image...")
            subprocess.run(["xdg-open","CapturingImage.mp3"])
            compressed_image_path = capture_image()
            print("Recording prompt...")
            subprocess.run(["xdg-open","RecordingPrompt.mp3"])
            sleep(1)
            prompt_text = record_audio()
            if ("who is this person" in prompt_text.lower() or "describe the person" in prompt_text.lower() or "person" in prompt_text.lower()):
                #face-recognition
                image_path="captured_image.png"
                print("Identifying person")
                find_match(image_path)
                continue
            call_api_with_gemini(prompt_text)
            os.remove(compressed_image_path)
            os.remove("captured_image.png")
            print("Converting API output to speech...")
            sleep(2)
