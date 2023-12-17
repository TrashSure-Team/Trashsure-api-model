from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import tensorflow as tf

app = FastAPI()
model = tf.keras.models.load_model('model.h5')


def process_image(file) -> str:
    image = Image.open(io.BytesIO(file))
    image = image.resize((128, 128))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)
    image = image / 255.0  
    return image

@app.get('/')
async def root():
    return {'example':"thisis"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Process the image
        # contents = file.file.read()
        processed_image = process_image(await file.read())
        
        # Make prediction
        prediction = model.predict(processed_image)
        predicted_class_index = tf.argmax(prediction, axis=1).numpy()[0]
        class_labels = ['Glass', 'Medical', 'Metal', 'Paper', 'Plastic', 'Textiles', 'e-Waste']
        predicted_class_label = class_labels[predicted_class_index]
    
        

        return JSONResponse(content={"label":str(predicted_class_label),"prediction":str(prediction) }, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)