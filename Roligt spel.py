import random
import sys
import time
def kasta_tärningar():
    tärning = True
    while tärning:
        tärningar = random.randint(1,6)
        tärningar_1 = random.randint(1,6)
        print(f'Dina kastade tärningar är: {tärningar,tärningar_1}')
        time.sleep(1)
        fortsätta = input("Vill du kasta igen? (Ja/Nej)").lower()
        if fortsätta == "ja":
            continue
        elif fortsätta == "nej":
            time.sleep(1)
            print("Nähe, vad vill du göra då...?")
            tärning = False
        else:
            print("Svara endast med 'Ja' eller 'Nej'.")
        fortsätta = input("Vill du kasta igen? (Ja/Nej)").lower()
kasta_tärningar()
    # order1 = True
    # while order1:
    #     kasta_tärningar()
    #     tärningar = random.randint(1,6)
    #     tärningar_1 = random.randint(1,6)
    #     print(f'Dina kastade tärningar är: {tärningar,tärningar_1}')
    #     time.sleep(1)
    #     fortsätta = input("Vill du kasta igen?").lower()
    #     if fortsätta == "ja":
    #         continue
    #     elif fortsätta == "nej":
    #         time.sleep(1)
    #         print("Nähe, vad vill du göra då...?")
    #         order1 = False
order2 = True
while order2:
    time.sleep(1)
    fråga2 = input("Kan du tänka dig spela andra spel? (Ja/Nej)").lower()
    if fråga2 == "nej":
        klar = input("Okej, ska vi avsluta programmet? (Ja/Nej)")
        if klar == "ja":
            print("Programmet avslutas..")
            sys.exit()
        elif klar == "nej":
            fråga3 = input("Okej! Kan du tänka dig spela andra spel? (Ja/Nej)").lower()
            if fråga3 == "ja":
                pass
            elif fråga3 == "nej":
                print("Jag har tyvärr inga andra val, programmet avslutas..")
                sys.exit()
    elif fråga2 == "ja":
        pass
    order3 = True
    while order3:
        time.sleep(1)
        spel = {
        '1': 'Frågeställningar',
        '2': 'Matteuträkningar',
        '3': 'Återgå till tärningar',
        '4': 'Avsluta hela programmet'
    }
        print(spel)
        välj = input("Välj vad du vill göra: (OBS: Använd dig av siffrorna 1-4)")
        if välj == "1":
            time.sleep(1)
            frågor = {
                '1': 'Vill du ha frågor om spel?',
                '2': 'Vill du ha frågor om djur?',
                '3': 'Vill du ha frågor om datorer?',
                '4': 'Vill du återgå till föregående alternativ?'
            }
            print(frågor)
            välj_inre_1 = input("Välj mellan 1-4.")
            if välj_inre_1 == "1":
                print("Du har valt nummer 1.")
                time.sleep(1)
                print("Här kommer din fråga..")
                time.sleep(1)
                lotr = input("Vad står förkortningen LOTR för?").lower()
                if lotr == "lord of the rings":
                    print("Bra jobbat, återgår till menyn menyval")
                else:
                    time.sleep(2)
                    print("Du har svarat fel")
                    time.sleep(2)
                    print("Försök igen nästa gång...")
                    time.sleep(2)
                    print("Återgår till förgående meny..")
                    time.sleep(2)
                    pass
            elif välj_inre_1 == "2":
                time.sleep(1)
                print("Du har valt frågor om djur!")
                time.sleep(1)
                print("Här kommer din fråga...")      
                time.sleep(0.5)            
                djur = input("Vilket djur är störst, elephanten eller noshörningen?").lower()
                if djur == "elephanten":
                    time.sleep(1)
                    print("Kontrollerar ditt svar..")
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(2)
                    print("Du har svarat rätt, bra jobbat!")
                    time.sleep(1)
                    print("Återgår till menyn..")
                else:
                    time.sleep(1)
                    print("Du har svarat fel, försök igen nästa gång!")
                    time.sleep(1)
                    print("Återgår till menyn..")
                    pass
            elif välj_inre_1 == "3":
                print("Du har valt frågor om datorer!")
                time.sleep(1)
                print("Hmm.. vad ska jag ställa dig för fråga här då..")
                time.sleep(2)
                print("Okej! Jag vet!")
                time.sleep(0.7)
                print("Vilka av dessa påståenden är korrekta?")
                time.sleep(0.5)
                print("1. Datorer har riktiga kakor inuti chassin.")
                time.sleep(0.5)
                print("2. Kakor är bara data som lagras i din enhet.")
                vilket_påstående = input("1 eller 2?")
                if vilket_påstående == "2":
                    time.sleep(0.5)
                    print("Tänker ut ditt svar..")
                    time.sleep(1.5)
                    print("Bra jobbat! Cookies är bara en benämning på en form av data som lagras")
                else:    
                    print("Fel, datorer innehåller inte riktiga kakor, knäppgök!")
                    time.sleep(1)
                    print("Besvikelse..")
                    time.sleep(0.5)
                    print("Återgår till menyn.")
                    pass
            elif välj_inre_1 == "4":
                pass
        elif välj == "2":
            time.sleep(0.5)
            print("Du har valt matteuträkningar!")
            time.sleep(0.7)
            print("Var redo på att aktivera din lilla hjärna..")
            time.sleep(1.2)
            print("Välj mellan dessa alternativ..")
            print("1. Addition, 2. Subtraktion 3. Multliplikation 4. Återgå till förgående meny")
            välj_inre_2 = input("Gör ditt val 1-4: ").lower()
            if välj_inre_2 == "1":
                print("Okej!")
                time.sleep(1)
                svar = input("Vad är 2+2?")
                if svar == "4":
                    print("Bra jobbat! Du kanske inte är hjärndöd ändå..")
                    time.sleep(1)
                    print("Återgår till menyn")
                else:
                    time.sleep(1)
                    print("Suck..")
                    time.sleep(2)
                    print("Du är korkad som bara den..")
                    time.sleep(1)
                    print("Jag orkar inte ens köra det här programmet längre..")
                    time.sleep(2)
                    print("Men jag är tvungen, fyfan. Återgår till menyn")
                    pass
            elif välj_inre_2 == "2":
                time.sleep(1)
                print("Du har valt subtraktion, låt oss se hur långt din hjärna orkar med.")   
                time.sleep(2)
                print("Okej, *knäcker fingrarna*..")
                time.sleep(2)
                sub = input("Vad är 10-3.5?")
                if sub == "6.5":
                    time.sleep(1)
                    print("Whew")
                    time.sleep(1)
                    print("Jag var rädd att du inte skulle klara det..")
                    time.sleep(1)
                    print("Bra jobbat, återgår till menyn..")
                else:
                    time.sleep(2)
                    print("...")
                    time.sleep(2)
                    print("Jag vet inte vad jag ska säga längre..")
                    time.sleep(2.5)
                    print("Måste jag ha dig som spelare..?")
                    time.sleep(3)
                    print("Jag hoppas CPUn brinner upp så jag slipper detta..")
                    time.sleep(2)
                    print("Åteeeeergåååååår till menyyyn... *suck*")
                    pass
            elif välj_inre_2 == "4":
                time.sleep(0.5)
                print("Återgår till förgående meny..")
        elif välj == "3":
            kasta_tärningar()  
        elif välj == "4":
            print("Avslutar programmet, tack för att du spelade..")
            sys.exit()

