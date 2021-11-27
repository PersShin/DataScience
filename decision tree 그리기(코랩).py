from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
(pred == y_test).mean()

from sklearn.tree import export_graphviz

# .dot 파일로 export 해줍니다
export_graphviz(model, out_file='tree.dot', 
                feature_names = X_train.columns,
                max_depth = 4, # 표현하고 싶은 최대 depth
                precision = 3, # 소수점 표기 자릿수
                filled = True, # class별 color 채우기
                rounded=True, # 박스의 모양을 둥글게
               )
# 생성된 .dot 파일을 .png로 변환
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'decistion-tree.png', '-Gdpi=600'])
# jupyter notebook에서 .png 직접 출력
from IPython.display import Image
Image(filename = 'decistion-tree.png')