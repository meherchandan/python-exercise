import datetime

def agecalculator():
    name = input("What's your name:")
    age = input('hey {}, how old are you:'.format(name))
    finalage = 100 - age
    now = datetime.datetime.now()
    finalyear = int(now.year + finalage)
    msg = ""
    if(finalage>0):
        msg = 'Hi {} you will turn 100 on {}'.format(name.title(),finalyear)
    else:
        msg  = 'You are already 100 years old. Stay Alive!!'
    print(msg)
    copier = input("Enter a number: ")
    print((msg+'\n')*int(copier))

if __name__ == "__main__":
    agecalculator()
