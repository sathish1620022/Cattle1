import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df=df=pd.read_csv("Training.csv")

col_removed=["abdominal_pain","anaemia","acetone","blood_poisoning","colic","Condemnation_of_livers","encephalitis","gaseous_stomach","high_proportion","hyperaemia","hydrocephalus",
             "intermittent_fever","jaundice","ketosis","milk_flakes","mucosal_lesions","milk_fever","nausea","nasel_discharges","oedema","pain", "painful_tongue","pneumonia",
             "photo_sensitization","reduced_rumination","reduced_fertility","stomach_pain","quivering_lips","shallow_breathing","swollen_pharyngeal", "swelling",
             "tachycardia","torticollis","udder_swelling","udder_heat","udder_hardeness","udder_redness","udder_pain","saliva","rumenstasis","raised_breathing"]

df.drop(columns=col_removed,inplace=True)
df.rename(columns={"lack_of-coordination":"lack_of_coordination","reduction_milk_vields":"reduction_milk_yields"},inplace=True)

X=df.drop(columns="prognosis")
y=df["prognosis"]

label=LabelEncoder()
y_label=label.fit_transform(y)
     
scale=StandardScaler()
X_scaled=scale.fit_transform(X)
     
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y_label,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()
model.fit(X_train,y_train)


