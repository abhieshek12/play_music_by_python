music = {
    1 : "https://youtu.be/-FP2Cmc7zj4?feature=shared" , 
    2 : "https://youtu.be/KUN5Uf9mObQ?feature=shared" , 
    3 : "https://youtu.be/Ja168gMpb3o?feature=shared" , 
    4 : "https://youtu.be/hxMNYkLN7tI?feature=shared" , 
    5 : "https://youtu.be/S-z6vyR89Ig?feature=shared"
    
}

def library (text) :
    if text.lower() in "labon ko" :
        return music[1]
    elif text.lower() in "arabic kuthu" :
        return music[2]
    elif text.lower() in "Why This Kolaveri Di".lower() :
        return music[3]
    elif text.lower() in "Aaj Ki Raat".lower() :
        return music[4]
    elif text.lower() in "Kaho Na Kaho ".lower() :
        return music[5]
    
     