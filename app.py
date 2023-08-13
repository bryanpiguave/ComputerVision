import streamlit  as st
from PIL import Image
import numpy as np 
import tensorflow as tf
import tensorflow_hub as hub
# Load your trained model
model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/tensorflow/efficientnet/b0/classification/1")
])
model.build([None, 224, 224, 3])  # Batch input shape.

model = model.load_weights('/home/bryan/Documents/GITHUB/PlantCV/weights/cp.ckpt')

def preprocess_image(image):
    image = image.resize((224, 224))  # Adjust the dimensions according to your model
    image = np.array(image)
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)
    return image



def main():
    st.markdown("# Produce classifier 🍌")
    st.sidebar.markdown("# Produce classifier 🍌")
    uploaded_image = st.file_uploader("Choose a produce image")
    
    class_labels = ['Class1', 'Class2', 'Class3', ...]


    image = Image.open('data/mini_dataset/banana/banana992.jpg')

    st.image(image, caption='You can use this image as test')

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        preprocessed_image = preprocess_image(image)

        # Make predictions using your model
        predictions = model.predict(preprocessed_image)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_labels[predicted_class_index]

        st.write(f"Predicted Class: {predicted_class_label}")
        st.write("Class Probabilities:")
        for i, class_prob in enumerate(predictions[0]):
            st.write(f"{class_labels[i]}: {class_prob:.4f}")

if __name__=="__main__":
    main()

