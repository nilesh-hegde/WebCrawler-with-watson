import database
from watson_developer_cloud import ToneAnalyzerV3
import json

dtoi={'anger':0,'fear':0,'joy':0,'sadness':0,'analytical':0,'confident':0,'tentative':0}
dndtv={'anger':0,'fear':0,'joy':0,'sadness':0,'analytical':0,'confident':0,'tentative':0}
d={'anger':0,'fear':0,'joy':0,'sadness':0,'analytical':0,'confident':0,'tentative':0}

def analysis(text,file):
    tone_analyzer = ToneAnalyzerV3(
        version='*********',
        username='**********',
        password='**********',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()
    i=0
    a1=tone_analysis['document_tone']
    a2=a1['tones']
    while i<len(a2):
        a3=a2[i]
        #print(a3['tone_id'])
        if file=='0':
            dtoi[a3['tone_id']]=1
        if file=='1':
            dndtv[a3['tone_id']]=1
        i=i+1
    for x in d:
        d[x]=dtoi[x]+dndtv[x]
    database.ins(d)
    database.instoi(dtoi)
    database.insndtv(dndtv)
