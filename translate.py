import pandas as pd
from googletrans import Translator
import time

timestr = time.strftime("%Y.%m.%d-%H.%M.%S")

languages = {'af': 'afrikaans','sq': 'albanian', 
'am': 'amharic', 'ar': 'arabic', 
'hy': 'armenian', 'az': 'azerbaijani', 
'eu': 'basque', 'be': 'belarusian', 
'bn': 'bengali', 'bs': 'bosnian', 
'bg': 'bulgarian', 'ca': 'catalan', 
'ceb': 'cebuano','ny': 'chichewa',
'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 
'co': 'corsican','hr': 'croatian', 
'cs': 'czech', 'da': 'danish', 
'nl': 'dutch', 'en': 'english', 
'eo': 'esperanto', 'et': 'estonian', 
'tl': 'filipino', 'fi': 'finnish', 
'fr': 'french', 'fy': 'frisian', 
'gl': 'galician', 'ka': 'georgian', 
'de': 'german', 'el': 'greek', 
'gu': 'gujarati', 'ht': 'haitian creole', 
'ha': 'hausa', 'haw': 'hawaiian', 
'iw': 'hebrew', 'he': 'hebrew',
'hi': 'hindi', 'hmn': 'hmong', 
'hu': 'hungarian', 'is': 'icelandic', 
'ig': 'igbo', 'id': 'indonesian', 
'ga': 'irish', 'it': 'italian', 
'ja': 'japanese', 'jw': 'javanese',
'kn': 'kannada', 'kk': 'kazakh', 
'km': 'khmer', 'ko': 'korean', 
'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 
'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 
'lt': 'lithuanian', 'lb': 'luxembourgish', 
'mk': 'macedonian', 'mg': 'malagasy', 
'ms': 'malay', 'ml': 'malayalam', 
'mt': 'maltese', 'mi': 'maori', 
'mr': 'marathi', 'mn': 'mongolian', 
'my': 'myanmar (burmese)', 'ne': 'nepali', 
'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 
'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 
'sm': 'samoan', 'gd': 'scots gaelic', 
'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 
'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 
'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 
'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 
'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 
'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian',
'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 
'vi': 'vietnamese', 'cy': 'welsh', 
'xh': 'xhosa', 'yi': 'yiddish', 
'yo': 'yoruba', 'zu': 'zulu'}

if __name__ == '__main__':
    flag = 1
    choice = str(input(" Enter the language you want to translate your text into: " )).lower()
    
    t1=time.perf_counter()
    df = pd.read_excel('input_data.xlsx')

    for lang_code,lang in languages.items():
        if choice in lang:
            flag=1
            translator = Translator()
            df['Translated Text'] = df['Input Text'].map(lambda x: translator.translate(x, src="en", dest=lang_code).text)
        
            output_file = "Translated_Data_"+timestr+".xlsx"
            df.to_excel(output_file,index=False,sheet_name = 'Translated Data')
        
            t2=time.perf_counter()

            print('-'*40,'\n')
            print("Translation complete!")
            print('-'*40,'\n')  

            print('-'*45,'\n')
            print("Execution time:",t2-t1,"seconds.\n")
            print('-'*45,'\n')
            exit()

        else:
            flag=0
            continue

    if(flag==0):
        print('-'*55,'\n')
        print("Sorry :(   This language isn't supported for translation. \n")
        print('-'*55,'\n')