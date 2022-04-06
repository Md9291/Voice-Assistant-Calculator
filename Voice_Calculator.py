"""
Project:  Voice Assistant Calculator
@author: MOHAMMAD YUNUS.
"""
#pip install pyttsx3
import pyttsx3
#pip install speech_recognition
import speech_recognition as sr
#pip install DateTime
import datetime 
from datetime import date
#pip install calendra
import calendar
#pip install times
import time
import math
#pip install wikipedia
import wikipedia

global query
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am voice assistant yunus. Please tell me how may I help you.")
    
def takeCommand():
    global query
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)     
        print("Say that again please...")  
        speak('Say that again please...')
        return "None"    
    return query

def calculator():
    global query
    try:
        if 'addition'  in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to add')
            b = float(input("Enter another number to add:"))
            c = a+b
            print(f"{a} + {b} = {c}")
            speak(f'The addition of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'subtraction' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to subtract')
            b = float(input("Enter another number to subtract:"))
            c = a-b
            print(f"{a} - {b} = {c}")
            speak(f'The subtraction of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'reminder' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number')
            b = float(input("Enter another number:"))
            c = a%b
            print(f"{a} % {b} = {c}")
            speak(f'The modular division of {a} and {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                    
        elif 'division' in query:
            speak('Enter a number as dividend')
            a = float(input("Enter a number:"))
            speak('Enter another number as divisor')
            b = float(input("Enter another number as divisor:"))
            c = a/b
            print(f"{a} / {b} = {c}")
            speak(f'{a} divided by {b} is equal to {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'multiplication' in query:
            speak('Enter a number')
            a = float(input("Enter a number:"))
            speak('Enter another number to multiply')
            b = float(input("Enter another number to multiply:"))
            c = a*b
            print(f"{a} x {b} = {c}")
            speak(f'The multiplication of {a} and {b} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square root' in query:
            speak('Enter a number to find its sqare root')
            a = float(input("Enter a number:"))
            c = a**(1/2)
            print(f"Square root of {a} = {c}")
            speak(f'Square root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'square' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**2
            print(f"{a} x {a} = {c}")
            speak(f'Square of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube root' in query:
            speak('Enter a number to find its cube root')
            a = float(input("Enter a number:"))
            c = a**(1/3)
            print(f"Cube root of {a} = {c}")
            speak(f'Cube root of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cube' in query:
            speak('Enter a number to find its sqare')
            a = float(input("Enter a number:"))
            c = a**3
            print(f"{a} x {a} x {a} = {c}")
            speak(f'Cube of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'factorial' in query:
            try:
                n = int(input('Enter the number whose factorial you want to find:'))
                fact = 1
                for i in range(1,n+1):
                    fact = fact*i
                print(f"{n}! = {fact}")
                speak(f'{n} factorial is equal to {fact}. Your answer is {fact}.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                #print(e)
                speak('I unable to calculate its factorial.')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'power' in query or 'raise' in query:
            speak('Enter a number whose power you want to raised')
            a = float(input("Enter a number whose power to be raised :"))
            speak(f'Enter a raised power to {a}')
            b = float(input(f"Enter a raised power to {a}:"))
            c = a**b
            print(f"{a} ^ {b} = {c}")
            speak(f'{a} raise to the power {b} = {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'percentage' in query:
            speak('Enter a number whose percentage you want to calculate')
            a = float(input("Enter a number whose percentage you want to calculate :"))
            speak(f'How many percent of {a} you want to calculate?')
            b = float(input(f"Enter how many percentage of {a} you want to calculate:"))
            c = (a*b)/100
            print(f"{b} % of {a} is {c}")
            speak(f'{b} percent of {a} is {c}. Your answer is {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
            
        elif 'interest' in query:
            speak('Enter the principal value or amount')
            p = float(input("Enter the principal value (P):"))
            speak('Enter the rate of interest per year')
            r = float(input("Enter the rate of interest per year (%):"))
            speak('Enter the time in months')
            t = int(input("Enter the time (in months):"))            
            interest = (p*r*t)/1200
            sint = round(interest)
            fv = round(p + interest) 
            print(f"Interest = {interest}")
            print(f"The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {p + interest}.")
            speak(f'interest is {sint}. The total amount accured, principal plus interest, from simple interest on a principal of {p} at a rate of {r}% per year for {t} months is {fv}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        
    
        elif 'sine' in query:
            speak('Enter the angle in degree to find its sine value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.sin(b)
            speak('Here is your answer.')
            print(f"sin({a}) = {c}")
            speak(f'sin({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        elif 'cos' in query:
            speak('Enter the angle in degree to find its cosine value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.cos(b)
            speak('Here is your answer.')
            print(f"cos({a}) = {c}")
            speak(f'cos({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
                
        elif 'cot' in query or 'court' in query:
            try:
                speak('Enter the angle in degree to find its cotangent value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c = 1/math.tan(b)
                speak('Here is your answer.')
                print(f"cot({a}) = {c}")
                speak(f'cot({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print("infinity")
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                
            
                
        elif 'tan' in query or '10' in query:
            speak('Enter the angle in degree to find its tangent value')
            a = float(input("Enter the angle:"))
            b = a * 3.14/180
            c = math.tan(b)
            speak('Here is your answer.')
            print(f"tan({a}) = {c}")
            speak(f'tan({a}) = {c}')
            
            speak('Do you want to do another calculation?')
            query = takeCommand().lower()
            if 'yes' in query:
                speak('ok which calculation you want to do?')
                query = takeCommand().lower()
                calculator()
            else:
                speak('ok')
        
                
        elif 'cosec' in query:
            try:
                speak('Enter the angle in degree to find its cosecant value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c =1/ math.sin(b)
                speak('Here is your answer.')
                print(f"cosec({a}) = {c}")
                speak(f'cosec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                    
        elif 'cosecant' in query:
            try:
                speak('Enter the angle in degree to find its cosecant value')
                a = float(input("Enter the angle:"))
                b = a * 3.14/180
                c =1/ math.sin(b)
                speak('Here is your answer.')
                print(f"cosec({a}) = {c}")
                speak(f'cosec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
                
        elif 'secant' in query:
            try:
                speak('Enter the angle in degree to find its secant value')
                a = int(input("Enter the angle:"))
                b = a * 3.14/180
                c = 1/math.cos(b)
                speak('Here is your answer.')
                print(f"sec({a}) = {c}")
                speak(f'sec({a}) = {c}')
                
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            except Exception as e:
                print('Infinity')
                speak('Answer is infinity')
                speak('Do you want to do another calculation?')
                query = takeCommand().lower()
                if 'yes' in query:
                    speak('ok which calculation you want to do?')
                    query = takeCommand().lower()
                    calculator()
                else:
                    speak('ok')
            
                
    except Exception as e:
        speak('I unable to do this calculation.')
        speak('Do you want to do another calculation?')
        query = takeCommand().lower()
        if 'yes' in query:
            speak('ok which calculation you want to do?')
            query = takeCommand().lower()
            calculator()
        else:
            speak('ok')
        
        
if __name__ == "__main__":
    wishMe()
    said = True
    while said:

        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
   
       
        elif 'calculat' in query:
            speak('Yes. Which kind of calculation you want to do? addition, substract, divide, multiply or anything else.')
            query = takeCommand().lower()
            calculator()
            
        elif 'add' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif '+' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'plus' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')      
        elif 'subtrac' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'minus' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'multipl' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif ' x ' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'slash' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif '/' in query:
            speak('If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'divi' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'trigonometr' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'percent' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')          
        elif '%' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'raise to ' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')

        elif 'simple interest' in query:
            speak('If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'change' in query and 'your' in query and 'voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak("Here's an example of one of my voices. Would you like to use this one?")
            query = takeCommand().lower()
            if 'yes' in query or 'sure' in query or 'of course' in query:
                speak('Great. I will keep using this voice.')
            elif 'no' in query:
                speak('Ok. I am back to my other voice.')
                engine.setProperty('voice', voices[0].id)
            else:
                speak('Sorry, I am having trouble understanding. I am back to my other voice.')
                engine.setProperty('voice', voices[0].id)
       
        elif ('repeat' in query and ('word' in query or 'sentence' in query or 'line' in query) and ('say' in query or 'tell' in query)) or ('repeat' in query and 'after' in query and ('me' in query or 'my' in query)):
            speak('yes sir, I will repeat your words starting from now')
            query = takeCommand().lower()
            speak(query)
            time.sleep(1)
            speak("If you again want me to repeat something else, try saying, 'repeat after me' ")        
        elif 'where do you live' in query:
            speak('I am from India, I live in laptop of Mr. Yunus')
        
        elif 'you are great' in query:
            speak('Thank you sir. It is because of artificial intelligence which had learnt by humans.')
            
        elif 'excellent' in query:
            speak('Thank you Dr Maheswari mam')
        elif len(query) >= 200:
            speak('Your voice is pretty good!')  
        elif 'exit' in query:
            speak('Ok, Thank you Sir.')
            said = False
            speak('see you later.')
        elif ' ' in query:
            try:
                #query = query.replace("what is ","")
                results = wikipedia.summary(query, sentences=3)
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')       
                
        else:
            speak('I unable to give answer of your question')
       
      
