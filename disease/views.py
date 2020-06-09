from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Diseases, symptoms, alert, question, answer
from .forms import Diseaseform, Symptomform, QuestionForm



def home(request):
    context={}
    alerts=alert.objects.all().order_by('people_affected')
    context['alerts']=alerts
    return render(request, 'disease/home.html',context)

def contact(request):
    return render(request, 'disease/contact.html')

def aboutus(request):
    return render(request, "disease/aboutus.html")

def privacy(request):
    return render(request, 'disease/privacy.html')
    
def thanks(request):
    return render(request, 'disease/thanks.html')

def Hhome(request):
    return render(request, 'disease/HospitalDash.html')
    
def diseaseview(request):
    if request.method == "POST":
        form = Diseaseform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'disease/thanks.html')
    else:
        form = Diseaseform()
    
    return render(request, 'disease/form.html', {'form' : form})

def usercheckview(request):
    symptoms={"Heberden's node": 0, "Murphy's sign": 0, "Stahli's line": 0, 'abdomen acute': 0, 'abdominal bloating': 0, 'abdominal tenderness': 0, 'abnormal sensation': 0, 'abnormally hard consistency': 0, 'abortion': 0, 'abscess bacterial': 0, 'absences finding': 0, 'achalasia': 0, 'ache': 0, 'adverse effect': 0, 'adverse reaction': 0, 'agitation': 0, 'air fluid level': 0, 'alcohol binge episode': 0, 'alcoholic withdrawal symptoms': 0, 'ambidexterity': 0, 'angina pectoris': 0, 'anorexia': 0, 'anosmia': 0, 'aphagia': 0, 'apyrexial': 0, 'arthralgia': 0, 'ascites': 0, 'asterixis': 0, 'asthenia': 0, 'asymptomatic': 0, 'ataxia': 0, 'atypia': 0, 'aura': 0, 'awakening early': 0, 'barking cough': 0, 'bedridden': 0, 'behavior hyperactive': 0, 'behavior showing increased motor activity': 0, 'blackout': 0, 'blanch': 0, 'bleeding of vagina': 0, 'bowel sounds decreased': 0, 'bradycardia': 0, 'bradykinesia': 0, 'breakthrough pain': 0, 'breath sounds decreased': 0, 'breath-holding spell': 0, 'breech presentation': 0, 'bruit': 0, 'burning sensation': 0, 'cachexia': 0, 'cardiomegaly': 0, 'cardiovascular event': 0, 'cardiovascular finding': 0, 'catatonia': 0, 'catching breath': 0, 'charleyhorse': 0, 'chest discomfort': 0, 'chest tightness': 0, 'chill': 0, 'choke': 0, 'cicatrisation': 0, 'clammy skin': 0, 'claudication': 0, 'clonus': 0, 'clumsiness': 0, 'colic abdominal': 0, 'consciousness clear': 0, 'constipation': 0, 'coordination abnormal': 0, 'cough': 0, 'cushingoid facies': 0, 'cushingoid\xa0habitus': 0, 'cyanosis': 0, 'cystic lesion': 0, 'debilitation': 0, 'decompensation': 0, 'decreased body weight': 0, 'decreased stool caliber': 0, 'decreased translucency': 0, 'diarrhea': 0, 'difficulty': 0, 'difficulty passing urine': 0, 'disequilibrium': 0, 'distended abdomen': 0, 'distress respiratory': 0, 'disturbed family': 0, 'dizziness': 0, 'dizzy spells': 0, 'drool': 0, 'drowsiness': 0, 'dullness': 0, 'dysarthria': 0, 'dysdiadochokinesia': 0, 'dysesthesia': 0, 'dyspareunia': 0, 'dyspnea': 0, 'dyspnea on exertion': 0, 'dysuria': 0, 'ecchymosis': 0, 'egophony': 0, 'elation': 0, 'emphysematous change': 0, 'energy increased': 0, 'enuresis': 0, 'erythema': 0, 'estrogen use': 0, 'excruciating pain': 0, 'exhaustion': 0, 'extrapyramidal sign': 0, 'extreme exhaustion': 0, 'facial paresis': 0, 'fall': 0, 'fatigability': 0, 'fatigue': 0, 'fear of falling': 0, 'fecaluria': 0, 'feces in rectum': 0, 'feeling hopeless': 0, 'feeling strange': 0, 'feeling suicidal': 0, 'feels hot/feverish': 0, 'fever': 0, 'flare': 0, 'flatulence': 0, 'floppy': 0, 'flushing': 0, 'focal seizures': 0, 'food intolerance': 0, 'formication': 0, 'frail': 0, 'fremitus': 0, 'frothy sputum': 0, 'gag': 0, 'gasping for breath': 0, 'general discomfort': 0, 'general unsteadiness': 0, 'giddy mood': 0, 'gravida 0': 0, 'gravida 10': 0, 'green sputum': 0, 'groggy': 0, 'guaiac positive': 0, 'gurgle': 0, 'hacking cough': 0, 'haemoptysis': 0, 'haemorrhage': 0, 'hallucinations auditory': 0, 'hallucinations visual': 0, 'has religious belief': 0, 'headache': 0, 'heartburn': 0, 'heavy feeling': 0, 'heavy legs': 0, 'hematochezia': 0, 'hematocrit decreased': 0, 'hematuria': 0, 'heme positive': 0, 'hemianopsia homonymous': 0, 'hemiplegia': 0, 'hemodynamically stable': 0, 'hepatomegaly': 0, 'hepatosplenomegaly': 0, 'hirsutism': 0, 'history of - blackout': 0, 'hoard': 0, 'hoarseness': 0, 'homelessness': 0, 'homicidal thoughts': 0, 'hot flush': 0, 'hunger': 0, 'hydropneumothorax': 0, 'hyperacusis': 0, 'hypercapnia': 0, 'hyperemesis': 0, 'hyperhidrosis disorder': 0, 'hyperkalemia': 0, 'hypersomnia': 0, 'hypersomnolence': 0, 'hypertonicity': 0, 'hyperventilation': 0, 'hypesthesia': 0, 'hypoalbuminemia': 0, 'hypocalcemia result': 0, 'hypokalemia': 0, 'hypokinesia': 0, 'hypometabolism': 0, 'hyponatremia': 0, 'hypoproteinemia': 0, 'hypotension': 0, 'hypothermia, natural': 0, 'hypotonic': 0, 'hypoxemia': 0, 'immobile': 0, 'impaired cognition': 0, 'inappropriate affect': 0, 'incoherent': 0, 'indifferent mood': 0, 'intermenstrual heavy bleeding': 0, 'intoxication': 0, 'irritable mood': 0, 'jugular venous distention': 0, 'labored breathing': 0, 'lameness': 0, 'large-for-dates fetus': 0, 'left\xa0atrial\xa0hypertrophy': 0, 'lesion': 0, 'lethargy': 0, 'lightheadedness': 0, 'lip smacking': 0, 'loose associations': 0, 'low back pain': 0, 'lung nodule': 0, 'macerated skin': 0, 'macule': 0, 'malaise': 0, 'mass in breast': 0, 'mass of body structure': 0, 'mediastinal shift': 0, 'mental status changes': 0, 'metastatic lesion': 0, 'milky': 0, 'moan': 0, 'monoclonal': 0, 'monocytosis': 0, 'mood depressed': 0, 'moody': 0, 'motor retardation': 0, 'muscle hypotonia': 0, 'muscle twitch': 0, 'myalgia': 0, 'mydriasis': 0, 'myoclonus': 0, 'nasal discharge present': 0, 'nasal flaring': 0, 'nausea': 0, 'nausea and vomiting': 0, 'neck stiffness': 0, 'neologism': 0, 'nervousness': 0, 'night sweat': 0, 'nightmare': 0, 'no known drug allergies': 0, 'no status change': 0, 'noisy respiration': 0, 'non-productive cough': 0, 'nonsmoker': 0, 'numbness': 0, 'numbness of hand': 0, 'oliguria': 0, 'orthopnea': 0, 'orthostasis': 0, 'out of breath': 0, 'overweight': 0, 'pain': 0, 'pain abdominal': 0, 'pain back': 0, 'pain chest': 0, 'pain foot': 0, 'pain in lower limb': 0, 'pain neck': 0, 'painful swallowing': 0, 'pallor': 0, 'palpitation': 0, 'panic': 0, 'pansystolic murmur': 0, 'para 1': 0, 'para 2': 0, 'paralyse': 0, 'paraparesis': 0, 'paresis': 0, 'paresthesia': 0, 'passed stones': 0, 'patient non compliance': 0, 'pericardial friction rub': 0, 'phonophobia': 0, 'photophobia': 0, 'photopsia': 0, 'pin-point pupils': 0, 'pleuritic pain': 0, 'pneumatouria': 0, 'polydypsia': 0, 'polymyalgia': 0, 'polyuria': 0, 'poor dentition': 0, 'poor feeding': 0, 'posterior\xa0rhinorrhea': 0, 'posturing': 0, 'presence of q wave': 0, 'pressure chest': 0, 'previous pregnancies 2': 0, 'primigravida': 0, 'prodrome': 0, 'productive cough': 0, 'projectile vomiting': 0, 'prostate tender': 0, 'prostatism': 0, 'proteinemia': 0, 'pruritus': 0, 'pulse absent': 0, 'pulsus\xa0paradoxus': 0, 'pustule': 0, 'qt interval prolonged': 0, 'r wave feature': 0, 'rale': 0, 'rambling speech': 0, 'rapid shallow breathing': 0, 'red blotches': 0, 'redness': 0, 'regurgitates after swallowing': 0, 'renal angle tenderness': 0, 'rest pain': 0, 'retch': 0, 'retropulsion': 0, 'rhd positive': 0, 'rhonchus': 0, 'rigor - temperature-associated observation': 0, 'rolling of eyes': 0, 'room spinning': 0, 'satiety early': 0, 'scar tissue': 0, 'sciatica': 0, 'scleral\xa0icterus': 0, 'scratch marks': 0, 'sedentary': 0, 'seizure': 0, 'sensory discomfort': 0, 'shooting pain': 0, 'shortness of breath': 0, 'side pain': 0, 'sinus rhythm': 0, 'sleeplessness': 0, 'sleepy': 0, 'slowing of urinary stream': 0, 'sneeze': 0, 'sniffle': 0, 'snore': 0, 'snuffle': 0, 'soft tissue swelling': 0, 'sore to touch': 0, 'spasm': 0, 'speech slurred': 0, 'splenomegaly': 0, 'spontaneous rupture of membranes': 0, 'sputum purulent': 0, 'st segment depression': 0, 'st segment elevation': 0, 'stiffness': 0, 'stinging sensation': 0, 'stool color yellow': 0, 'stridor': 0, 'stuffy nose': 0, 'stupor': 0, 'suicidal': 0, 'superimposition': 0, 'sweat': 0, 'sweating increased': 0, 'swelling': 0, 'symptom aggravating factors': 0, 'syncope': 0, 'systolic ejection murmur': 0, 'systolic murmur': 0, 't wave inverted': 0, 'tachypnea': 0, 'tenesmus': 0, 'terrify': 0, 'thicken': 0, 'throat sore': 0, 'throbbing sensation quality': 0, 'tinnitus': 0, 'tired': 0, 'titubation': 0, 'todd paralysis': 0, 'tonic seizures': 0, 'transaminitis': 0, 'transsexual': 0, 'tremor': 0, 'tremor resting': 0, 'tumor cell invasion': 0, 'unable to concentrate': 0, 'unconscious state': 0, 'uncoordination': 0, 'underweight': 0, 'unhappy': 0, 'unresponsiveness': 0, 'unsteady gait': 0, 'unwell': 0, 'urge incontinence': 0, 'urgency of\xa0micturition': 0, 'urinary hesitation': 0, 'urinoma': 0, 'verbal auditory hallucinations': 0, 'verbally abusive behavior': 0, 'vertigo': 0, 'vision blurred': 0, 'vomiting': 0, 'weepiness': 0, 'weight gain': 0, 'welt': 0, 'wheelchair bound': 0, 'wheezing': 0, 'withdraw': 0, 'worry': 0, 'yellow sputum': 0}
    symp = []

    for key, value in symptoms.items():
        symp.append(key) 
    if request.method == "POST":
        form = Symptomform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'disease/analysis.html')
    else:
        form = Symptomform()

          

    return render(request, 'disease/usercheck.html', {'form' : form, 'symp': symp})

def analysis(request):
    symp = symptoms.objects.all()
    field = symptoms._meta.fields
    
    data_symp = str(getattr(symp, str(field), "null"))
    #print(field)
    #print(symp)
    
    if("," in data_symp):
        data_symp = data_symp.split(",")
    else:
        data_symp = data_symp.strip(" ")

    #data_symp is available for analysis
    symptoms.objects.all().delete()       

    return render(request, 'disease/analysis.html')

def qanalysis(request):
    ans = answer.objects.all()
    field = answer._meta.fields

    data_ans = str(getattr(ans, str(field), 'null'))

    if("," in data_ans):
        data_ans = data_ans.split(",")
    else:
        data_ans = data_ans.strip(" ")

    answer.objects.all().delete()

    return render(request, 'disease/analysis.html')


def userquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'disease/analysis.html')
    else:
        form = QuestionForm()
    return render(request, 'disease/userquestion.html', {'form' : form})