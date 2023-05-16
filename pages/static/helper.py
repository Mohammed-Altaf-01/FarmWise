# third party imports 
import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
from googletrans import Translator


# built in imports 
import requests
import os
from PIL import ImageOps, Image
import h5py


def prediction(image):
    """
    Input is a image which is PIL's Image object and converts it into array before classifing it into a prediction 

    """
    classifier = load_model("pages/ml_models/imageclassifier.h5")
    shape = ((226, 226, 3))
    test_image = image.resize((256, 256))
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image/255.0
    test_image = np.expand_dims(test_image, axis=0)
    prediction = classifier.predict(test_image)
    labels = ['Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Potato___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight', 'Tomato___Septoria_leaf_spot', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Strawberry___Leaf_scorch', 'Peach___healthy', 'Apple___Apple_scab', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 'Apple___Black_rot', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
              'Peach___Bacterial_spot', 'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Pepper,_bell___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy', 'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles)', 'Raspberry___healthy', 'Tomato___Leaf_Mold', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Pepper,_bell___Bacterial_spot', 'Corn_(maize)___healthy']
    return np.argmax(prediction[0])  # labels[np.argmax(prediction[0])]


@st.cache_data
def tips():
    """
    This function just works for non diseased images, reducing the api call load 
    """
    return """1.Use quality seeds: Make sure to use high-quality seeds to start your crops. Healthy seeds have better resistance to pests and diseases and will help ensure a strong start for your crops.

2.Soil health: Good soil health is essential for healthy crops. Make sure the soil has adequate nutrients, pH level, and organic matter. You can also add compost or fertilizer to enrich the soil.

3.Watering: Water the crops regularly, but don't overwater. Most crops need around an inch of water per week. Make sure the water is evenly distributed, and avoid watering during the hottest part of the day.

4.Mulching: Mulching helps to retain moisture in the soil, suppress weed growth, and keep the soil temperature even. Use organic materials like straw or leaves for best results.

5.Crop rotation: Rotating crops helps to prevent the build-up of pests and diseases in the soil. Rotate your crops every year, alternating between different plant families.

6.Pest control: Use natural methods to control pests, such as companion planting, insect-repelling herbs, and natural insecticides. Avoid using harmful chemicals that can harm the environment and the crops.

7.Weed control: Weeds can compete with crops for nutrients, water, and sunlight. Remove weeds regularly using hand weeding, hoeing or mulching.

8.Pruning: Prune your crops regularly to remove dead or diseased parts. This will help prevent the spread of diseases and improve air circulation around the plants.

9.Sunlight: Ensure that your crops receive adequate sunlight. Most crops require at least six hours of sunlight per day. Choose a spot that receives the most sunlight for planting.

10.Observation: Observe your crops regularly for signs of pests, diseases, or nutrient deficiencies. This will help you catch any problems early and take corrective action before they get worse."""



#translation using google translation api 
def translation(text,language):
    """Takes input a text and the language to convert into and return the given text converted into that specific language"""
    lang_dict = {'हिंदी':'hindi','ਪੰਜਾਬੀ':'punjabi',"తెలుగు":'telugu',"தமிழ்":"tamil","اردو":'urdu','English':'english'}
    language = lang_dict[language]
    translator = Translator()
    match language:
        case 'english':
            output = translator.translate(text,dest='en')
            return  output.text
        case 'hindi':
            # translating english to hindi  
            output = translator.translate(text, dest="hi")
            return output.text 
        case 'urdu':
            # translating english to hindi  
            output = translator.translate(text, dest="ur")
            return output.text    
        case 'punjabi':
            # translating english to hindi  
            output = translator.translate(text, dest="pa")
            return output.text  
        case 'telugu':
            # translating english to hindi  
            output = translator.translate(text, dest="te")
            return output.text  
        case 'tamil':
            # translating english to hindi  
            output = translator.translate(text, dest="ta")
            return output.text  
        case 'odia':
            # translating english to hindi  
            output = translator.translate(text, dest="or")
            return output.text  


def PromptChecker(prompt):
    """
    takes in a prompt or a statement and checeks weather it include agriculture and farm related statements or not 
    
    """
    str = prompt.split(" ")
    verification_list = ['describe','buisness','want','agriculture','agricultural','tips','tricks','leaf','grow','plant','flower','crop','disease','unhealthy','spots','color','green','colour','healthy','feartelizer','farming','agriculture','agribussiness','potato','tomato','ladyfinger','garlic','root','Vegetable',"Ash gourd"	,'Broccoli','Cucumber','Celery','Bitter gourd','Greens',"Carrot",'Spring onions','Potato','Capsicum','Turnip','Brinjal''Tomato',	'Green peas',	'Ginger'	,'Apple gourd',
                'Onion',	'Cauliflower'	,'Beetroot'	,'Ridged gourd','Garlic',	'Cabbage' ,'Mushroom',"Lady's finger"	,'Snake gourd	','Ivy gourd', 'Scarlet gourd',	'Spinach',
                'Beans','Lab labGreen papaya','Corn','Pumpkin'	,'Bottle gourd	','Snake beans' ,'Yard long beans',	'Okra','White pumpkin','Apple','Banana','Apricot',   'Atemoya ', ' Avocados',   'Blueberry ', ' Blackcurrant ',  'Ackee',   'Cranberry'  , 'Cantaloupe',   'Cherry'  , 'Black', 'sapote/Chocolate', 'pudding', 'fruit',   'Dragonrfruit'  , 'Dates'   ,'Cherimoya'  , "Buddha's hand", 'fruit ',  'Finger', 'Lime ',  'Fig'  , 'Coconut' ,
               'Cape', 'gooseberry','Inca', 'berry','Physalis ',  'Grapefruit'  , 'Gooseberries'  ,' Custard', 'apple/Sugar',  'Hazelnut'  , 'Honeyberries' ,  'Dragon', 'fruit ',  'Durian'   ,'Horned', 'Melon ' , 'Hog', 'Plum ',' Egg', 'fruit   Feijoa/Pineapple', 
               'guava/Guavasteen','Indian', 'Fig   Ice', 'Apple  ', 'Guava   Fuyu', 'Persimmon '  ,'Jackfruit ','  Jujube ','  Honeydew', 'melon',   'Jenipapo' ,  'Kiwi'  , 'Kabosu' ,  'Kiwano'  ,' Kaffir', 'lime/Makrut', 'Lime',   'Lime'  , 'Lychee' ,  'Longan'   ,'Langsat' ,  'Mango' ,  'Mulberry'  , 'Pear'  , 'Lucuma' ,  'Muskmelon'  , 'Naranjilla' ,   'Olive' ,  'Oranges' ,     'Pomegranate' ,  'Pineapple' ,   'Raspberries' ,  'Strawberries' ,  'Starfruit' , 'Watermelon' ,  'Sapota'  , 'Star', 'apple']
    extended = [i.lower().strip() for i in verification_list]  #extended was not working 
    for i in str:
        if i.lower() in extended:
            return True
    else:
        return False


# if __name__ == "__main__":
#     while True:
#         value = input("enter your prompt    ")
#         if value =='exit':
#             break
#         else:
#             print(PromptChecker(value))

