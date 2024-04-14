from flask import Blueprint,render_template,request
import cattle_disease_prediction as cp
view=Blueprint(__name__,"view")

@view.route('/')
def home():
    return render_template('index.html')

@view.route('/predict',methods=['POST','GET'])
def predict():
    disease={'anorexia':0, 'abortions':0, 'aggression':0, 'arthrogyposis':0, 'ankylosis':0,
       'anxiety':0, 'bellowing':0, 'blood_loss':0, 'blisters':0, 'conjunctivae':0,
       'coughing':0, 'depression':0, 'discomfort':0, 'dyspnea':0, 'dysentery':0,
       'diarrhoea':0, 'dehydration':0, 'drooling':0, 'dull':0, 'decreased_fertility':0,
       'difficulty_breathing':0, 'emaciation':0, 'fever':0, 'facial_paralysis':0,
       'frothing_of_mouth':0, 'frothing':0, 'highly_diarrhoea':0, 'high_pulse_rate':0,
       'high_temp':0, 'isolation_from_herd':0, 'infertility':0, 'loss_of_appetite':0,
       'lameness':0, 'lack_of_coordination':0, 'lethargy':0, 'lacrimation':0,
       'milk_watery':0, 'milk_clots':0, 'mild_diarrhoea':0, 'moaning':0,
       'reduction_in_milk_yield':0, 'rapid_breathing':0, 'reduced_fat':0,
       'reduced_feed_intake':0, 'salivation':0, 'stillbirths':0, 'swollen_tongue':0,
       'unwillingness_to_move':0, 'ulcer':0, 'vomiting':0, 'weight_loss':0,
       'weakness':0}
    data=request.form.values()
    for i in data:
        disease[i.lower().replace(" ","_")]=1
    ans=cp.model.predict([list(disease.values())])
    return render_template("disease.html",pred="The predicted disease is " + cp.label.classes_[ans][0])