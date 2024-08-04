from app import app
from flask import render_template, request, jsonify
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
from io import BytesIO
from PIL import Image
import pandas as pd
from bs4 import BeautifulSoup
import os, sys
from concurrent.futures import ThreadPoolExecutor


def load_image_from_url(url):
  try:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img
  except:
    return Image.open("Carte_Set_de_Base_1.png")

base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

def preprocess_and_extract(image_path, model):
    if "http" in image_path or "https" in image_path:
      img = load_image_from_url(image_path)
      img = img.resize((224, 224))
      img_data = np.array(img)
      ig = Image.fromarray(img_data)
      image_rgb = ig.convert('RGB')
      img_data = np.expand_dims(np.array(image_rgb), axis=0)
      img_data = preprocess_input(img_data)
    else:
      img = image.load_img(image_path, target_size=(224, 224))
      img_data = image.img_to_array(img)
      img_data = np.expand_dims(img_data, axis=0)
      img_data = preprocess_input(img_data)
    features = model.predict(img_data)
    return features

def compute_similarity(feature1, feature2):
    similarity = cosine_similarity(feature1, feature2)
    return similarity[0][0]*100

def get_img_url(url):
  req=requests.get(url)
  bs=BeautifulSoup(req.content,"html.parser")
  img_url=f'https://www.pokepedia.fr{bs.find("div",id="file").find("a").get("href")}'
  return (url,img_url,preprocess_and_extract(img_url, model))

df=pd.read_csv("pokemon_base_set_complete.csv")
features2=[]
with ThreadPoolExecutor(max_workers=os.cpu_count()) as exe:
    result=exe.map(get_img_url,df["Image URL"])
    for i in result:
        features2.append(i)

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/get_card_details",methods=["POST"])
def get_card_details():
    if request.method=="POST":
        try:
            file=request.files["file"]
            if file.filename.split(".")[-1] not in ("jpeg","png","jpg"):
                return jsonify(message="Invalid File"),400
            file_path=os.path.join(os.path.join(os.getcwd(),"temp"),file.filename)
            file.save(file_path)
            features1 = preprocess_and_extract(file_path, model)
            os.remove(file_path)
            similarity = [(i[0],i[1],score) for i in features2 if (score:=compute_similarity(features1, i[-1]))>=85]
            card_url=(max(similarity,key=lambda x:x[-1]) if similarity else [""]*3)
            card_detail=df[df["Image URL"]==card_url[0]].to_dict(orient="records")
            if card_detail:
              card_detail=card_detail[0]
              card_detail["Image URL"]=card_url[1]
              return jsonify(card_detail),200
            return jsonify(message="Unable to Detect the Card"), 400
        except Exception as e:
           print(e, sys.exc_info()[-1].tb_lineno)
           return jsonify(message="Something Went Wrong"),500
