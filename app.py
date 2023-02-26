import streamlit as st
from keras.models import load_model
from PIL import Image,ImageOps
import numpy as np


st.set_page_config(page_title="KANUMURI.HARSHITH'S TOMATO LEAF DETECTION ", page_icon = 'screenshot (2).png', layout = 'wide', initial_sidebar_state = 'auto')

st.set_option('deprecation.showfileUploaderEncoding',False)
st.title("TOMATO LEAF DISEASE DETECTION")

def loadmodel():
    model=load_model("tomato.h5")
    return model
model=loadmodel()
img=st.file_uploader("UPLOAD YOUR IMAGE",type=["jpg","png","JPG","PNG"])
def prediction(image,model):
    img=ImageOps.fit(image,(128,128),Image.LANCZOS)
    img=np.array(img)/255
    h=img[np.newaxis,...]
    r=model.predict(h)
    return r

if img is None:
    st.text("PLEASE UPLOAD A APPROPRIATE IMAGE")
else:
    image=Image.open(img)
    st.image(image,use_column_width=True)
    predict=prediction(image,model)
    classnames=["Tomato___Bacterial_spot","Tomato___Early_blight","Tomato___Late_blight","Tomato___Leaf_Mold"
                ,"Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite",
                "Tomato___Target_Spot","Tomato___Tomato_Yellow_Leaf_Curl_Virus","Tomato___Tomato_mosaic_virus",
                "Tomato___healthy"]
    print(np.argmax(predict))
    st.subheader(classnames[np.argmax(predict)])


