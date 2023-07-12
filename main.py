import pickle
import streamlit as st
from streamlit_option_menu import option_menu

Disease_Pred_Model = pickle.load(open('D:\Disease Prediction\disease_prediction_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu(' Disease Prediction System',
                          
                          ['Disease Prediction System'],
                          icons=['heart'],
                          default_index=0)
if (selected == "Disease Prediction"):


  



    
    # page title
    st.title(" Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  

    none = 0
    itching = 1
    skin_rash = 2
    nodal_skin_eruptions = 3
    continuous_sneezing = 4
    shivering = 5
    chills = 6
    joint_pain = 7
    stomach_pain = 8
    acidity_= 9
    ulcers_on_tongue = 10
    muscle_wasting = 11
    vomiting = 12
    burning_micturition = 13
    spotting_urination = 14
    fatigue = 15
    weight_gain = 16
    anxiety = 17
    cold_hands_feets = 18
    mood_swings = 19
    weight_loss = 20
    restlessness = 21
    lethargy = 22
    patches_in_throat = 23
    irregular_sugar_level = 24
    cough = 25
    high_fever = 26
    sunken_eyes = 27
    breathlessness = 28
    sweating = 29
    dehydration = 30
    indigestion = 31
    headache = 32
    yellowish_skin = 33
    dark_urine = 34
    nausea = 35
    loss_of_appetite = 36
    pain_behind_the_eyes = 37
    back_pain = 38
    constipation = 39
    abdominal_pain = 40
    diarrhoea = 41
    mild_fever = 42
    yellow_urine = 43
    yellowing_of_eyes = 44 
    acute_liver_failure = 44
    fluid_overload = 46
    swelling_of_stomach = 47
    swelled_lymph_nodes = 48 
    malaise = 49
    blurred_and_distorted_vision = 50
    phlegm = 51
    throat_irritation = 52
    redness_of_eyes = 53
    sinus_pressure = 54
    runny_nose = 55
    congestion = 56
    chest_pain = 57
    weakness_in_limbs = 58
    fast_heart_rate = 59
    pain_during_bowel_movements = 60
    pain_in_anal_region = 61
    bloody_stool = 62
    irritation_in_anus = 63
    neck_pain = 64
    dizziness = 65
    cramps = 66
    bruising = 67
    obesity = 68
    swollen_legs = 69
    swollen_blood_vessels = 70
    puffy_face_and_eyes = 71
    enlarged_thyroid = 72
    brittle_nails = 73
    swollen_extremeties = 74 
    excessive_hunger = 75
    extra_marital_contacts = 76
    drying_and_tingling_lips = 77
    slurred_speech = 78
    knee_pain = 79
    hip_joint_pain = 80 
    muscle_weakness = 81
    stiff_neck = 82
    swelling_joints = 83 
    movement_stiffness = 84
    spinning_movements = 85
    loss_of_balance = 86
    unsteadiness = 87
    weakness_of_one_body_side = 88
    loss_of_smell= 89
    bladder_discomfort = 90
    foul_smell_ofurine = 91
    continuous_feel_of_urine = 92
    passage_of_gases = 93
    internal_itching = 94
    toxic_look = 95
    depression = 96
    irritability = 97
    muscle_pain = 98
    altered_sensorium = 99
    red_spots_over_body = 100
    belly_pain = 101
    abnormal_menstruation = 102
    dischromic_patches = 103
    watering_from_eyes = 104
    increased_appetite =  105
    polyuria = 106
    family_history = 107
    mucoid_sputum = 108
    rusty_sputum = 109
    lack_of_concentration = 110
    visual_disturbances = 111
    receiving_blood_transfusion = 112
    receiving_unsterile_injections = 113
    coma = 114
    stomach_bleeding = 115
    distention_of_abdomen = 116
    history_of_alcohol_consumption = 117
    fluid_overload = 118
    blood_in_sputum = 119
    prominent_veins_on_calf = 120
    palpitations = 121
    painful_walking = 122
    pus_filled_pimples = 123
    blackheads = 124
    scurring = 125
    skin_peeling = 126
    silver_like_dusting = 127
    small_dents_in_nails = 128
    inflammatory_nails = 129
    blister = 130
    red_sore_around_nose = 131
    yellow_crust_ooze = 132
    prognosis = 133
    foul_smell_of_urine = 134
    dischromic__patches = 135
    spotting__urination = 136
    
    with col1:
        Symptom1 = st.text_input('Enter Symptom 1')
        
    with col2:
        Symptom2 = st.text_input('Enter Symptom 2')
        
    with col3:
        Symptom3 = st.text_input('Enter Symptom 3')
        
    with col4:
        Symptom4 = st.text_input('Enter Symptom 4')
        
    with col5:
        Symptom5  = st.text_input('Enter Symptom 5')
        
    with col1:
        Symptom6 = st.text_input('Enter Symptom 6')
        
    with col2:
        Symptom7 = st.text_input('Enter Symptom 7')
        
    with col3:
        Symptom8 = st.text_input('Enter Symptom 8')
        
    with col4:
        Symptom9 = st.text_input('Enter Symptom 9')
        
    with col5:
        Symptom10 = st.text_input('Enter Symptom 10')
        
    with col1:
        Symptom11 = st.text_input('Enter Symptom 11')
        
    with col2:
        Symptom12 = st.text_input('Enter Symptom 12')
        
    with col3:
        Symptom13 = st.text_input('Enter Symptom 13')
        
    with col4:
        Symptom14 = st.text_input('Enter Symptom 14')
        
    with col5:
        Symptom15 = st.text_input('Enter Symptom 15')
        
    with col1:
        Symptom16 = st.text_input('Enter Symptom 16')
        
    with col2:
        Symptom17 = st.text_input('Enter Symptom 17')
        
    Disease_Prediction = ''

        
        # creating a button for Prediction
        
    if st.button('Test Result'):
            Disease_Symptomps_prediction = Disease_Pred_Model.predict([[eval(Symptom1), eval(Symptom2), eval(Symptom3), eval(Symptom4), eval(Symptom5),eval(Symptom6), eval(Symptom7), eval(Symptom8), eval(Symptom9), eval(Symptom10),eval(Symptom11),eval(Symptom12),eval(Symptom13),eval(Symptom14),eval(Symptom15),eval(Symptom16),eval(Symptom17)]])
            Disease_Prediction = Disease_Symptomps_prediction[0]
            
            
    st.success(Disease_Prediction)
