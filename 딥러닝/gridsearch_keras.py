from inspect import Parameter
from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import train_test_split
#모델을 만드는 함수를 만들어 한번이 아니라 여러번 생성할 수  있게 한다.
#CNN모델이다.
def build_model(epochs,batch_size):
    print("This model is {} {}\n".format(epochs,batch_size))
    model = models.Sequential()
    model.add(layers.Conv2D(16, (3, 3), activation='relu', input_shape=(16, 16 ,1)))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(2, activation='softmax'))

    #model.summary()
    model.compile(optimizer='adam',
              #loss=tf.keras.losses.binary_crossentropy,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    return model

#적절하게 split을 해준다.
x_train, x_valid, y_train, y_valid = train_test_split(trian_images, label, test_size=0.2, shuffle=True, random_state=42)

model = KerasClassifier(build_fn = build_model, epochs = 20 , batch_size = 5)

#나누어 진행을 하게 되면 시간적으로 여유가 생기게 된다.
#parameters = {'epochs': [10, 20, 30, 40]}

#여러개를 한번에 진행할 수도 있다.
parameters = {'epochs': [10,20,30,40],
              'batch_size' : [32,64,128,192,256]}

grid_search = GridSearchCV(estimator = model,
                           param_grid = parameters,
                           scoring = 'accuracy',
                           cv = 2)

grid_search = grid_search.fit(x_train, y_train)
history=model.fit(x_train,y_train)
print("\nThe best parameter is {}".format(grid_search.best_params_))
print("\nThe best_accuracy is {}".format(grid_search.best_score_))