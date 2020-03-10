from django import forms
import nltk
import binascii
def xor(x, y):
    return '{0:b}'.format(int(x, 2) ^ int(y, 2))
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'




class DetectionForm(forms.Form):
    songName = forms.CharField(label="Name")
    songAuthor = forms.CharField(label="Author")
    songLyric = forms.CharField(label="Lyric" )
    def result(self):
        result=""
        sentence=self.cleaned_data['songLyric']
        nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        nltk_sentiment = SentimentIntensityAnalyzer()
        score = nltk_sentiment.polarity_scores(sentence)
        if score['neg'] > score['pos']: 
            result= 'sad'
        else:
            result= 'happy'
        return result

class thachthucForm(forms.Form):
    Ma = forms.CharField(label="Ma")
    Key= forms.CharField(label="Key")
    
            
    def result(self):
        result=""
        a=self.cleaned_data['Ma']
        k=self.cleaned_data['Key']
        kk=int(k)
        k1=bin(kk)
        D=""
        for i in range(0, len(a)):
            a1=text_to_bits(a[i])
            a2=xor(a1,k1)
            D=D+a2
        Ans=[]
        for i in range(0, len(D), 5):
            Ans.append(D[i:i+5])
        for i in range(len(Ans)):
            d="1"+Ans[i]
            Ans[i]=d
        str1 = ''.join(Ans)
        Last=[]
        for i in range(0, len(str1), 6):
            Last.append(str1[i:i+6])
        for i in range(len(Last)):
            result+=text_from_bits(Last[i])
            result+="    "
        return result
        