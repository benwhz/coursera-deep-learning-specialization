import pandas as pd
import re

def mergeIntervals(intervals):
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher[0] <= lower[1]:
                if lower[2] is higher[2]:
                    upper_bound = max(lower[1], higher[1])
                    merged[-1] = (lower[0], upper_bound, lower[2])
                else:
                    if lower[1] > higher[1]:
                        merged[-1] = lower
                    else:
                        merged[-1] = (lower[0], higher[1], higher[2])
            else:
                merged.append(higher)
    return merged

def get_entities(df):
    
    entities = []
    
    for i in range(len(df)):
        entity = []
    
        for annot in df['annotation'][i]:
            print(type(annot))
            try:
                ent = annot['label'][0]
                start = annot['points'][0]['start']
                end = annot['points'][0]['end'] + 1
                entity.append((start, end, ent))
            except:
                pass
    
        entity = mergeIntervals(entity)
        entities.append(entity)
    
    return entities

def pd_test():
    df_data = pd.read_json("./C5 - Sequence Models/Week 4/Named Entity Recognition/ner.json", lines=True)
    s1 = df_data.count(0)
    s2 = df_data.count(1)
    print(df_data.head(), type(s1), s1.shape, s2.shape)
    print(s1['content'], s2[1])

    df_data = df_data.drop(['extras'], axis=1)
    df_data['content'] = df_data['content'].str.replace("\n", " ")

    a = df_data['annotation'][0][0]
    print(a, type(a))
    get_entities(df_data)


    text = 'a   thit is a test string  '
    invalid_span_tokens = re.compile(r'\s')
    m = invalid_span_tokens.match(text[0])

    print(m)

    t = 'Afreen Jamadar Active member of IIIT Committee in Third year  Sangli, Maharashtra - Email me on Indeed: indeed.com/r/Afreen-Jamadar/8baf379b705e37c6  I wish to use my knowledge, skills and conceptual understanding to create excellent team environments and work consistently achieving organization objectives believes in taking initiative and work to excellence in my work.  WORK EXPERIENCE  Active member of IIIT Committee in Third year  Cisco Networking -  Kanpur, Uttar Pradesh  organized by Techkriti IIT Kanpur and Azure Skynet. PERSONALLITY TRAITS: • Quick learning ability • hard working  EDUCATION  PG-DAC  CDAC ACTS  2017  Bachelor of Engg in Information Technology  Shivaji University Kolhapur -  Kolhapur, Maharashtra  2016  SKILLS  Database (Less than 1 year), HTML (Less than 1 year), Linux. (Less than 1 year), MICROSOFT ACCESS (Less than 1 year), MICROSOFT WINDOWS (Less than 1 year)  ADDITIONAL INFORMATION  TECHNICAL SKILLS:  • Programming Languages: C, C++, Java, .net, php. • Web Designing: HTML, XML • Operating Systems: Windows […] Windows Server 2003, Linux. • Database: MS Access, MS SQL Server 2008, Oracle 10g, MySql.  https://www.indeed.com/r/Afreen-Jamadar/8baf379b705e37c6?isid=rex-download&ikw=download-top&co=IN'

    print(len(t.split()))

from transformers import DistilBertTokenizerFast, AutoTokenizer #, TFDistilBertModel

def tokenizer_chinese():
    """
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-cased')
    examples = ['今天天气不错','今天天气非常糟糕','今天阳光明媚，舒适清爽']
    tokenized_inputs = tokenizer(examples, truncation=True, is_split_into_words=False, padding='max_length', max_length=512)
    """
    sentences = ["今天 天气 不错",'今天 天气 非常 糟糕',"今天 天气 很好",'今天 天气 很差']
    tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese', use_fast = False, tokenize_chinese_chars = False)
    out = tokenizer(sentences)

    pass

from transformers import pipeline

def tf_test():
    nlp = pipeline('sentiment-analysis')
    result = nlp('We are very happy to include pipline into the transformers repository.')
    print(result)

if __name__ == '__main__':
    tf_test()