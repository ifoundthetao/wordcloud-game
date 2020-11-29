from flask import Flask, request, session, redirect, render_template, url_for
import base64
import datetime
import hashlib
import os
import random


app = Flask(__name__)
app.secret_key = "foo"

@app.route('/ajax/getname', methods=['GET'])
def get_name():
    currentHash = request.args.get('currentHash')
    return getNameFromHash(currentHash)

@app.route('/make-user', methods=['POST', 'GET'])
def make_user():
    if request.method == 'POST':
        session.permanent = True
        session['username'] = request.form['username']

        return redirect(url_for("main"))
        return "foo"
    else:
        #return """<!doctype html><html><head></head><body><form method=post>Enter a username: <input type=text name=username><input type=submit></form></body></html>"""
        return render_template('make-user.html')

@app.route('/')
def main():
    #if 'username' not in session:
    #    return redirect(url_for('make_user'))
    
    random.seed(getClosestSeed())
    image=random.choice(os.listdir('word-clouds'))
    image_base64 = ""
    with open('word-clouds/' + image, 'rb') as image_file:
        image_base64 = base64.b64encode(image_file.read())

    hashed_book_name =hashlib.md5(getBookNameFromFileName(image).encode('utf-8')).hexdigest()

    return render_template('index.html', image_base64=image_base64.decode('utf-8'), hashed_book_name=hashed_book_name)


def getBookNameFromFileName(filename):

    files = {
         "1chronicles_wordcloud.png" : "I Chronicles"
        ,"1corinthians_wordcloud.png" : "I Corinthians"
        ,"1john_wordcloud.png" : "I John"
        ,"1kings_wordcloud.png" : "I Kings"
        ,"1peter_wordcloud.png" : "I Peter"
        ,"1samuel_wordcloud.png" : "I Samuel"
        ,"1thessalonians_wordcloud.png" : "I Thessalonians"
        ,"1timothy_wordcloud.png" : "I Timothy"
        ,"2chronicles_wordcloud.png" : "II Chronicles"
        ,"2corinthians_wordcloud.png" : "II Corinthians"
        ,"2john_wordcloud.png" : "II John"
        ,"2kings_wordcloud.png" : "II Kings"
        ,"2peter_wordcloud.png" : "II Peter"
        ,"2samuel_wordcloud.png" : "II Samuel"
        ,"2thesalonians_wordcloud.png" : "II Thesalonians"
        ,"2timothy_wordcloud.png" : "II Timothy"
        ,"3john_wordcloud.png" : "III John"
        ,"amos_wordcloud.png" : "Amos"
        ,"colossians_wordcloud.png" : "Colossians"
        ,"daniel_wordcloud.png" : "Daniel"
        ,"deuteronomy_wordcloud.png" : "Deuteronomy"
        ,"ecclesiastes_wordcloud.png" : "Ecclesiastes"
        ,"ephesians_wordcloud.png" : "Ephesians"
        ,"esther_wordcloud.png" : "Esther"
        ,"exodus_wordcloud.png" : "Exodus"
        ,"ezekiel_wordcloud.png" : "Ezekiel"
        ,"ezra_wordcloud.png" : "Ezra"
        ,"full-summaries_wordcloud.png" : "Full Bible"
        ,"galatians_wordcloud.png" : "Galatians"
        ,"genesis_wordcloud.png" : "Genesis"
        ,"habakkuk_wordcloud.png" : "Habakkuk"
        ,"haggai_wordcloud.png" : "Haggai"
        ,"hebrews_wordcloud.png" : "Hebrews"
        ,"hosea_wordcloud.png" : "Hosea"
        ,"isaiah_wordcloud.png" : "Isaiah"
        ,"james_wordcloud.png" : "James"
        ,"jeremiah_wordcloud.png" : "Jeremiah"
        ,"job_wordcloud.png" : "Job"
        ,"joel_wordcloud.png" : "Joel"
        ,"john_wordcloud.png" : "John"
        ,"jonah_wordcloud.png" : "Jonah"
        ,"joshua_wordcloud.png" : "Joshua"
        ,"jude_wordcloud.png" : "Jude"
        ,"judges_wordcloud.png" : "Judges"
        ,"lamentations_wordcloud.png" : "Lamentations"
        ,"leviticus_wordcloud.png" : "Leviticus"
        ,"luke_wordcloud.png" : "Luke"
        ,"malachi_wordcloud.png" : "Malachi"
        ,"mark_wordcloud.png" : "Mark"
        ,"matthew_wordcloud.png" : "Matthew"
        ,"micah_wordcloud.png" : "Micah"
        ,"nahum_wordcloud.png" : "Nahum"
        ,"names_wordcloud.png" : "Names"
        ,"nasb_wordcloud.png" : "NASB"
        ,"nehemiah_wordcloud.png" : "Nehemiah"
        ,"numbers_wordcloud.png" : "Numbers"
        ,"obadiah_wordcloud.png" : "Obadiah"
        ,"philemon_wordcloud.png" : "Philemon"
        ,"philppians_wordcloud.png" : "Philppians"
        ,"proverbs_wordcloud.png" : "Proverbs"
        ,"psalms_wordcloud.png" : "Psalms"
        ,"revelation_wordcloud.png" : "Revelation"
        ,"romans_wordcloud.png" : "Romans"
        ,"ruth_wordcloud.png" : "Ruth"
        ,"song-of-solomon_wordcloud.png" : "Song of Solomon"
        ,"titus_wordcloud.png" : "Titus"
        ,"zechariah_wordcloud.png" : "Zechariah"
    }
    print(files[filename])
    return files[filename]

def getNameFromHash(currentHash):
    hashList = {
           "433954d85eb30629a97505247f7321dc" : "I Chronicles"
         , "2fe49ec78c684e8e34a5da67db550f2c" : "I Corinthians"
         , "056fd4a5d89be879b47b02296bc3a2b5" : "I John"
         , "9eae202e6ea972fa142aacb77c8f5270" : "I Kings"
         , "e4acd4ceffa7a7b69b2e49751d91263d" : "I Peter"
         , "a35c9f3edfce0ee07564701a2ba50983" : "I Samuel"
         , "5d211adc6fe5af930441cfc887d5af9f" : "I Thessalonians"
         , "ddac0275ac26a1c79b0e52e34c0c7804" : "I Timothy"
         , "280a60b79aae6b7bff92c741a8b6e6f9" : "II Chronicles"
         , "3bd3c56e48ba5b48b1fb3ba8d73d572b" : "II Corinthians"
         , "27ed83d583e457b0a6ca17e9e3cc1e44" : "II John"
         , "4cb5af220706732327289acd6b3af4a5" : "II Kings"
         , "cd328e11062892f488c82450b342a96a" : "II Peter"
         , "2edba8b7af675ea0f43279d2670d9558" : "II Samuel"
         , "2f39d3dc950e5a781ca881b4d2d3c4a5" : "II Thesalonians"
         , "4b9fdec03e70d6cbaa0a7066c1b13f02" : "II Timothy"
         , "16649369b551ffe3463f9c9963c6e5cc" : "III John"
         , "c00d602fe381288855f6b400ab6c77e7" : "Amos"
         , "e16897400dd1fa4a8f699d2b2e17cc2c" : "Colossians"
         , "262031397020fd8df478ec13b4b096c5" : "Daniel"
         , "fc40272ee60011e0b27911c6a9b82e9a" : "Deuteronomy"
         , "90d3f2a652fad0d56aa3076d0f2f62be" : "Ecclesiastes"
         , "964add4a8b79b57348cee7ad9f125a18" : "Ephesians"
         , "2b1d226f59ef0b094ccb49ba1b095394" : "Esther"
         , "0cdf051c93865faa15cbc5cd3d2b69fb" : "Exodus"
         , "9c21900bc9b7ccaa68c9166ddc0d3014" : "Ezekiel"
         , "dc53785d25a3e11fb45aa5dbc946e293" : "Ezra"
         , "4c65685a0a1647c2abdf10d8023d7a42" : "Full Bible"
         , "265eba480c067b1ced4f25b4d0815e87" : "Galatians"
         , "411f3239ffbefd44ebd08ac9eaec6489" : "Genesis"
         , "88f7ae40918a94a708df713bcaf26626" : "Habakkuk"
         , "b7daf17893fe6e8ed6d32b307175758a" : "Haggai"
         , "28e03b6e834efd8e8cce67baecb17500" : "Hebrews"
         , "027f557078da31b70bdceb26d54e9ee0" : "Hosea"
         , "76c269a0dfa33fba379e29eed2ee0521" : "Isaiah"
         , "d52e32f3a96a64786814ae9b5279fbe5" : "James"
         , "e0d1bfde0c2da91753f73c54bb4b74c5" : "Jeremiah"
         , "cf51066f49e517f274b8173cc265c60b" : "Job"
         , "da64a1bc2c9a53dd1cdb6846103cd2de" : "Joel"
         , "61409aa1fd47d4a5332de23cbf59a36f" : "John"
         , "ae8989a8f472814e65123b137ab29d1f" : "Jonah"
         , "85b103482a20682da703aa388933a6d8" : "Joshua"
         , "229331fbe50e5f7296e88fc548d4534f" : "Jude"
         , "d3f20c9854b085e4d004e75c61ec26d8" : "Judges"
         , "47526f0d96d4d615944da9028f707dcc" : "Lamentations"
         , "bfe2abcd3abf7db1766799c6d5971272" : "Leviticus"
         , "b21dfb148d20b1febdd8d86417f925c1" : "Luke"
         , "12071ae292a0192ca5149099089bcbcc" : "Malachi"
         , "b82a9a13f4651e9abcbde90cd24ce2cb" : "Mark"
         , "64730ca35ed9274ff6aa8a719407fe53" : "Matthew"
         , "f0c014f660edfba75f68145fe0670dcb" : "Micah"
         , "a978a4a109624bbd5e552c597494acee" : "Nahum"
         , "cafd6a9e554bce844b3fb415747a3abe" : "Names"
         , "6cab395d2a36b8a0d404292f21ee2d75" : "NASB"
         , "222194e9c4a4f9f42b44c72d7cc0c680" : "Nehemiah"
         , "cbebfa21dbe8e87e788d94a76f073807" : "Numbers"
         , "f048451b8fe68c0b70bc4a006fbecd4a" : "Obadiah"
         , "06f9e4db9076632e0c7294d6fda8ff1b" : "Philemon"
         , "38c91ae1de0efd650c7e1dc0c464f8b5" : "Philppians"
         , "8733dd8dee25126cf5ba8ed07290d863" : "Proverbs"
         , "0b6d443b27df3bf9855361724e9d0fe6" : "Psalms"
         , "2e77f901673403a0a2adaa9318093179" : "Revelation"
         , "29a673ce0a8e68c6cd6b13553bb61539" : "Romans"
         , "8e06843ec162b74a7902867dd4bca8c8" : "Ruth"
         , "156f81c27d05d15751c80ff770edf45f" : "Song of Solomon"
         , "f71185951db8a1c8c166c45b001afd9a" : "Titus"
         , "6da724e30f3be7fd21f0a555d3ae01ac" : "Zechariah"
    }
    return hashList[currentHash]

def getClosestSeed(dt=None, round_to=20):
    if dt == None:
        dt=datetime.datetime.now()
    seconds = (dt - dt.min).seconds
    rounding = (seconds + round_to/2) // round_to * round_to
    return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)

