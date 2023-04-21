import time

entry = input('Hello Dan! Insert Password: ')

if entry == 'Dan':
    print('Access Granted')
else:
    print('Access Denied')
    print('Hint: Name')
    if entry == 'Ethan':
        print('This Is Dedicated To Ethan My Best Friend')
        print('P.S Your Amazing!')
        time.sleep(1)
    entry2 = input(' ')
    if entry2 == 'Dan':
        print('Access Granted')
    else:
        print('i already gave you a hint')
        print('im sorry')
        time.sleep(1)
        exit()
print('Welcome, Dan!')
time.sleep (0.5)
print('Loading...')
time.sleep (1)
print('Apps:')
print(' ')
print('The Internet')
print('Bank')
print('MeTube')
print('Terminal')
print('Python 3.11')
print('Reminders')

entry = input(' ')

if entry == 'The Internet':
    print('Loading The Internet...')
    time.sleep(1)
    print('You Can Search:')
    print('FREEVBUCKS.bon')
    print('HackerSim.bon')
    print('Amongus.bon')
    InternetPart = input(' ')
    if InternetPart == 'FREEVBUCKS.bon':
        print('DOWNLOADING Trog.zib...')
        time.sleep(1)
        print('YOU HAVE BEEN VIRUSED')
        time.sleep(1)
        count = 0
        while (count < 50):
            count = count + 1
            print("Virus Has Been Detected")
        else:
            time.sleep
            exit()
    else:
        if InternetPart == 'HackerSim.bon':
            print('Downloading Hacker Simulator...')
            time.sleep(1)
            print('Your already playing it.')
            exit()
        else:
            if InternetPart == 'Amongus.bon':
                time.sleep(1)
                spams = 0
                while (spams < 50):
                    spams = spams + 1
                    print('AMONGUS')
                else:
                    exit()

else:
    if entry == 'MeTube':
        print('What Do You Expect?')
        exit()
    else:
        if entry == 'Terminal':
            SettingsPart = input('Enter Command')
            print('Credits')
            if SettingsPart == 'Credits':
                print("Thanks For Playing My Game!")
                print('You Are A Amazing Person!')
                time.sleep(1)
                print('People Like You Make My Day <3')
                time.sleep(1)
                print('Have A Great One!')
                time.sleep(1)
            exit()
        else:
            if entry == 'Python 3.11':
                print('Your Already In It')
                exit()
            else:
                if entry == 'Reminders':
                    print('One Reminder')
                    time.sleep(1)
                    print('remind Ethan to finish the video')
                else:
                    if entry == 'Bank':
                        print('[#         ]')
                        time.sleep(1.5)
                        print('[###       ]')
                        time.sleep(2)
                        print('[######    ]')
                        time.sleep(1)
                        print('[######### ]')
                        time.sleep(0.5)
                        print('Done!')
                        time.sleep(1)
                        print('Bank Of Arkansas')
                        print('Hello, DAN JERRET')
                        print('Funds:')
                        print('2,435,124.53')
                        time.sleep(1)
                        bankpart = input('Do You Wish To Withdraw? (Y/N)')
                        if bankpart == 'y':
                            print('Withdrew 100,000 Dollars To Jhon Pastel')
                            exit()
                        else:
                            print('Invalid Input')
                            exit()