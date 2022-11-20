import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cv2


from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.layers import Input, Activation, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import load_model

from imblearn.over_sampling import RandomOverSampler

CURRENT_ROOT_FOLDER = './data'

FER_DATASET_PATH = os.path.join(CURRENT_ROOT_FOLDER, 'fer2013.csv')
# original source: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data?select=fer2013.tar.gz

FERPLUS_DATASET_PATH = os.path.join(CURRENT_ROOT_FOLDER, 'fer2013new.csv')
# original source: https://github.com/microsoft/FERPlus

MODEL_CKPT_DIR = os.path.join(CURRENT_ROOT_FOLDER, './output/')

IMG_WIDTH, IMG_HEIGHT = 48, 48

emotion_mapping = {
    0: 'angry',
    1: 'disgusted',
    2: 'fearful',
    3: 'happy',
    4: 'sad',
    5: 'surprised',
    6: 'neutral'
}


# def get_dataset_splits():
#     df_fer = pd.read_csv(FER_DATASET_PATH)
#     df_ferplus = pd.read_csv(FERPLUS_DATASET_PATH)
#     df_ferplus.drop(columns=['Usage', 'Image name'], inplace=True)
#     df = pd.concat([df_fer, df_ferplus], axis=1)
#     return df[df['Usage'] == 'Training'], df[df['Usage'] == 'PrivateTest'], df[df['Usage'] == 'PublicTest']


# def get_image(pixels_str):
#     img = np.fromstring(pixels_str, np.float32, sep=' ')
#     img = np.stack((img,) * 3, axis=-1)
#     img /= 255  # important for deep learning
#     img = img.reshape(IMG_WIDTH, IMG_HEIGHT, 3)
#     return img


# def get_ml_data(df, oversample=False):
#     num_classes = df['emotion'].unique().shape[0]

#     X_raw, y_raw = [], []
#     for idx, row in df.iterrows():
#         X_raw.append([row['pixels']])
#         y_raw.append(row['emotion'])

#     if oversample:
#         ros = RandomOverSampler(random_state=0)
#         X_raw, y_raw = ros.fit_resample(X_raw, y_raw)

#     X, y = [], []
#     for i in range(0, len(X_raw)):
#         X.append(get_image(X_raw[i][0]))
#         y.append(to_categorical(y_raw[i], num_classes=num_classes))

#     del (X_raw)
#     del (y_raw)

#     return np.array(X), np.array(y), num_classes


# df_train, df_val, df_test = get_dataset_splits()

# X_train, y_train, num_classes = get_ml_data(df_train, oversample=True)
# X_val, y_val, _ = get_ml_data(df_val)
# X_test, y_test, _ = get_ml_data(df_test)

# print(f'Number of training samples: {X_train.shape[0]}')
# print(f'Number of validation samples: {X_val.shape[0]}')
# print(f'Number of test samples: {X_test.shape[0]}')

# print(y_train[0])
# plt.imshow(X_train[0])

# BATCH_SIZE = 64

# gen_train = ImageDataGenerator(
#     rotation_range=40,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     fill_mode='nearest'
# ).flow(X_train, y_train, batch_size=BATCH_SIZE)

# gen_val = ImageDataGenerator().flow(X_val, y_val, batch_size=BATCH_SIZE)

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
          input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.3))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.3))

model.add(Conv2D(128, (3, 3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.3))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(256))
model.add(Dropout(0.5))
model.add(Dense(7))
model.add(Activation('softmax'))

model.summary()

# Skipping training

# NUM_EPOCHS = 80

# steps_train = int(np.math.ceil(X_train.shape[0] / BATCH_SIZE))
# steps_val = int(np.math.ceil(X_val.shape[0] / BATCH_SIZE))

# training_callbacks = [
#     EarlyStopping(patience=5, monitor='val_accuracy', restore_best_weights=True),
#     ModelCheckpoint(filepath=os.path.join(MODEL_CKPT_DIR, 'model_basic.h5'), monitor='val_accuracy', save_best_only=True),
#     ModelCheckpoint(filepath=os.path.join(MODEL_CKPT_DIR, 'model.{epoch:02d}-{val_accuracy:.2f}.h5'), monitor='val_accuracy', save_best_only=True),
# ]

# model.compile(
#   loss='categorical_crossentropy',
#   optimizer=Adam(learning_rate=0.001),
#   metrics=['accuracy']
# )

# model.fit(
#   gen_train,
#   steps_per_epoch=steps_train,
#   epochs=NUM_EPOCHS,
#   validation_data=gen_val,
#   validation_steps=steps_val,
#   callbacks=training_callbacks
# )

# Loading pre-trained model

model = load_model('model.22-0.53.h5')

# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful",
                3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# start the webcam feed
cap = cv2.VideoCapture(0)
while True:
    # Find haar cascade to draw bounding box around face
    ret, frame = cap.read()
    if not ret:
        break
    facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Grab webcam image and convert colorspace to RGB
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face
    faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
      # Crop face, resize to 48x48
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        crop = cv2.resize(roi_gray, (48, 48))
        
        # Expand dims to add blank dimension at beginning of array to match input expected by model
        X = np.expand_dims(crop, axis=0)

        print(X)

        prediction = model.predict(X)
        print(prediction)
        maxindex = int(np.argmax(prediction))
        cv2.putText(frame, emotion_dict[maxindex] + " " + str(prediction[0][maxindex]),
                    (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Video', cv2.resize(
        frame, (1600, 960), interpolation=cv2.INTER_CUBIC))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
