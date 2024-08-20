# WONG YEN WEI
# TP063782

from datetime import datetime, timedelta


def new_patient():
    patient = open("patient.txt", "a")
    vaccination = open("vaccination.txt", "a")
    rec = []
    vrec = []
    arec = [rec,vrec]
    name = str(input('Name: '))
    name = name.upper()
    while True:
        age = int(input('Age: '))
        if 120 > age >= 0:
            break
        else:
            print("Please Input a Valid Age")
    pid = get_new_id('PID')
    phone_no = str(input('Phone number: '))
    ic_no = str(input('IC number: '))
    email = str(input('Email: '))
    while True:
        vaccine_centre_choice = str(input("Vaccination Centre Choice(1/2): "))
        if vaccine_centre_choice == '1' or '2':
            vaccine_centre = "VC" + str(vaccine_centre_choice)
            break
        else:
            print("INVALID INPUT, PLEASE INSERT 1 OR 2! ")
    rec.append(str(name))
    rec.append(str(age))
    rec.append(str(phone_no))
    rec.append(str(pid))
    rec.append(str(ic_no))
    rec.append(str(email))
    rec.append(str(vaccine_centre))
    vrec.append(str(name))
    vrec.append(str(age))
    vrec.append(str(pid))
    vrec.append(str(vaccine_centre))
    if age < 12:
        print("Sorry, you cannot get vaccinated under the age of 12.")
        rec.append("No vaccine")
    elif 45 <= age <= 120:
        while True:
            print("AF vaccine(2 Dose)")
            print("BV vaccine(2 Dose)")
            print("DM vaccine(2 Dose)")
            print("EC vaccine(1 Dose)")
            vac_code = str(input("Please choose a vaccine type: "))
            vac_code = vac_code.upper()
            if vac_code == 'AF':
                print("You have chosen AF vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'BV':
                print("You have chosen BV vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'DM':
                print("You have chosen DM vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'EC':
                print("You have chosen EC vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            else:
                print('INVALID INPUT!')
    elif age >= 18:
        while True:
            print("BV vaccine(2 Dose)")
            print("CZ vaccine(2 Dose)")
            print("EC vaccine(1 Dose)")
            vac_code = str(input("Please choose a vaccine type: "))
            vac_code = vac_code.upper()
            if vac_code == 'BV':
                print("You have chosen BV vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'CZ':
                print("You have chosen CZ vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'EC':
                print("You have chosen EC vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            else:
                print('INVALID INPUT!')
    elif age >= 12:
        while True:
            print("AF vaccine(2 Dose)")
            print("CZ vaccine(2 Dose)")
            print("DM vaccine(2 Dose)")
            vac_code = str(input("Please choose a vaccine type: "))
            vac_code = vac_code.upper()
            if vac_code == 'AF':
                print("You have chosen AF vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'CZ':
                print("You have chosen CZ vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            elif vac_code == 'DM':
                print("You have chosen DM vaccine.")
                rec.append(vac_code)
                vrec.append(vac_code)
                break
            else:
                print('INVALID INPUT!')
    print("Your patient id is ", pid)
    now = datetime.now()
    reg_date = now.strftime("%d/%m/%y")
    dose1 = now + timedelta(days=5)
    d1 = dose1.strftime("%d/%m/%y")
    d2 = '-'
    stat = 'NEW'
    rec.append(str(reg_date))
    vrec.append(str(d1))
    vrec.append(d2)
    vrec.append(stat)
    print("Your first dose will be on: " + d1)
    print("=" * 100)
    patient.write(":".join(rec) + "\n")
    vaccination.write(":".join(vrec) + "\n")
    return arec


def v_admin(vallrec):
    search = str(input('Patient ID: '))
    flg = 0
    for i in range(len(vallrec)):
        if search.upper() in vallrec[i][2]:
            flg = 1
            print("Patient ID:", vallrec[i][2])
            print("Vaccination Centre:", vallrec[i][3])
            print("Selected Vaccine:", vallrec[i][4])
            print("D1 Date:", vallrec[i][5])
            print("D2 Date:", vallrec[i][6])
            print("Status:", vallrec[i][7])
            if vallrec[i][7] == 'Done' :
                print("You have done your vaccination! ")
            elif vallrec[i][7] == "NEW":
                d1done = input("Update Status To Dose 1 Done ? ")
                if d1done.lower() == 'yes':
                    vallrec[i][7] = 'DONE DOSE 1'
                    if vallrec[i][4] == "AF":
                        now = datetime.now()
                        dose1 = now.strftime("%d/%m/%y")
                        vallrec[i][5] = dose1
                        dose2 = now + timedelta(days=14)
                        vallrec[i][6] = dose2.strftime("%d/%m/%y")
                        print("Your second dose will be on: " + vallrec[i][6])
                        break
                    elif vallrec[i][4] == "CZ":
                        now = datetime.now()
                        dose1 = now.strftime("%d/%m/%y")
                        vallrec[i][5] = dose1
                        dose2 = now + timedelta(days=21)
                        vallrec[i][6] = dose2.strftime("%d/%m/%y")
                        print("Your second dose will be on: " + vallrec[i][6])
                        break
                    elif vallrec[i][4] == "BV":
                        now = datetime.now()
                        dose1 = now.strftime("%d/%m/%y")
                        vallrec[i][5] = dose1
                        dose2 = now + timedelta(days=21)
                        vallrec[i][6] = dose2.strftime("%d/%m/%y")
                        print("Your second dose will be on: " + vallrec[i][6])
                        break
                    elif vallrec[i][4] == "DM":
                        now = datetime.now()
                        dose1 = now.strftime("%d/%m/%y")
                        vallrec[i][5] = dose1
                        dose2 = now + timedelta(days=28)
                        vallrec[i][6] = dose2.strftime("%d/%m/%y")
                        print("Your second dose will be on: " + vallrec[i][6])
                        break
                    elif vallrec[i][4] == "EC":
                        print("You are completely vaccinated! ")
                        vallrec[i][6] = 'NOT NEEDED'
                        vallrec[i][7] = 'FULLY VACCINATED'
                        break
                elif d1done.lower() == 'no':
                    print('Please complete your vaccination before you update the vaccination status. ')
                    break
            elif vallrec[i][7] == 'DONE DOSE 1':
                d2done = input("Update Dose 2 Status To DONE ? ")
                if d2done.lower() == 'yes':
                    vallrec[i][7] = 'FULLY VACCINATED'
                    print('Congratulations! You are completely vaccinated!')
                    break
                elif d2done.lower() == 'no':
                    print('Please complete your vaccination before you update the vaccination status. ')
                    break
            elif vallrec[i][7] == 'FULLY VACCINATED':
                print("You are already Fully Vaccinated")
    if flg == 0:
        print("Patient ID not found")
    else:
        with open("vaccination.txt", "w") as fh:
            for line in vallrec:
                fh.write(":".join(line)+"\n")
    print('=' * 100)


def get_new_id(eid):
    with open("id.txt", "r") as user:
        rec = user.readline()
    if eid == "PID":
        ind = 0
    a = rec.split(":")
    nextid = a[ind]
    new_id = str(int(nextid[3:]) + 1)
    if len(new_id) == 1:
        nextid = nextid[:3] + "0000" + new_id
    elif len(new_id) == 2:
        nextid = nextid[:3] + "000" + new_id
    elif len(new_id) == 3:
        nextid = nextid[:3] + "00" + new_id
    elif len(new_id) == 4:
        nextid = nextid[:3] + "0" + new_id
    elif len(new_id) == 5:
        nextid = nextid[:3] + new_id
    a[ind] = nextid
    rec = ":".join(a)
    with open("id.txt", "w") as user:
        user.write(rec)
    return nextid


def mod_patient(allrecs, vallrec):
    no_of_rec = len(allrecs)
    search = str(input("Please enter your Patient ID (PID) to search : "))
    flg = 0
    for i in range(no_of_rec):
        if search.upper() in allrecs[i][3]:
            flg = 1
            print("1 - ", allrecs[i][0])
            print("2 - ", allrecs[i][2])
            print("3 - ", allrecs[i][5])
            idx = input("Enter the no of field to modify :")
            if idx == '1':
                indx = 0
                mod = input("Enter a new Value :")
                mod = mod.upper()
                allrecs[i][indx] = mod
                vallrec[i][0] = mod
                print("Your name has been changed to", mod)
            elif idx == '2':
                indx = 2
                mod = input("Enter a new Value :")
                allrecs[i][indx] = mod
                print("Your phone number has been changed to", mod)
            elif idx == '3':
                indx = 5
                mod = input("Enter a new Value :")
                allrecs[i][indx] = mod
                print("Your email account has been changed to", mod)
                break
    if flg == 0:
        print("Patient ID not found.")
    else:
        with open("patient.txt", "w") as fh:
            for line in allrecs:
                fh.write(":".join(line)+"\n")
        with open("vaccination.txt", "w") as fh1:
            for line in vallrec:
                fh1.write(":".join(line)+"\n")
    print('=' * 100)
    return search


def search_patient_record_status(vallrec,allrecs):
    search = input('Patient ID: ')
    flg = 0
    for i in range(len(vallrec)):
        if search.upper() in vallrec[i][2]:
            flg = 1
            print("=" * 120)
            print("NAME".center(10) + "|" + "AGE".center(5) + "|" + "PATIENT ID".center(10) +
                  "|" + "IC NUMBER".center(12) + "|" + "VACCINE CENTRE".center(14) +
                  "|" + "VACCINE".center(12) + "|" + "DOSE 1 DATE".center(12) +
                  "|" + "DOSE 2 DATE".center(12) + "|" + "STATUS".center(20))
            print("=" * 120)
            print(vallrec[i][0].center(10) + "|" + vallrec[i][1].center(5) + "|" + vallrec[i][2].center(10) + "|" +
                  allrecs[i][4].center(12) + "|" + vallrec[i][3].center(14) + "|" + vallrec[i][4].center(12) + "|" +
                  vallrec[i][5].center(12) + "|" + vallrec[i][6].center(12) + "|" + vallrec[i][7].center(20))
            print("=" * 120)
            break
    if flg == 0:
        print("Patient ID not found.")
        print("=" * 100)


def patient_vac_stat(vallrec):
    af = 0
    afd = 0
    afh = 0
    cz = 0
    czd = 0
    czh = 0
    bv = 0
    bvd = 0
    bvh = 0
    dm = 0
    dmd = 0
    dmh = 0
    ec = 0
    ecd = 0
    ech = 0
    afv2d = 0
    czv2d = 0
    bvv2d = 0
    dmv2d = 0
    ecv2d = 0
    status = len(vallrec)
    for i in range(status):
        if vallrec[i][4] == 'AF':
            af = af + 1
            if vallrec[i][7] == 'DONE DOSE 1':
                afd = afd + 1
            elif vallrec[i][7] == 'NEW':
                afh = afh + 1
            elif vallrec[i][7] == "FULLY VACCINATED":
                afv2d = afv2d + 1
        elif vallrec[i][4] == 'CZ':
            cz = cz + 1
            if vallrec[i][7] == 'DONE DOSE 1':
                czd = czd + 1
            elif vallrec[i][7] == 'NEW':
                czh = czh + 1
            elif vallrec[i][7] == "FULLY VACCINATED":
                czv2d = czv2d + 1
        elif vallrec[i][4] == 'BV':
            bv = bv + 1
            if vallrec[i][7] == 'DONE DOSE 1':
                bvd = bvd + 1
            elif vallrec[i][7] == 'NEW':
                bvh = bvh + 1
            elif vallrec[i][7] == "FULLY VACCINATED":
                bvv2d = bvv2d + 1
        elif vallrec[i][4] == 'DM':
            dm = dm + 1
            if vallrec[i][7] == 'DONE DOSE 1':
                dmd = dmd + 1
            elif vallrec[i][7] == 'NEW':
                dmh = dmh + 1
            elif vallrec[i][7] == "FULLY VACCINATED":
                dmv2d = dmv2d + 1
        elif vallrec[i][4] == 'EC':
            ec = ec + 1
            if vallrec[i][7] == 'DONE DOSE 1':
                ecd = ecd + 1
            elif vallrec[i][7] == 'NEW':
                ech = ech + 1
            elif vallrec[i][7] == "FULLY VACCINATED":
                ecv2d = ecv2d + 1
    print("Number of people who are waiting for dose 1:", afh+czh+bvh+dmh+ech)
    print("AF: ", afh)
    print("CZ: ", czh)
    print("BV: ", bvh)
    print("DM: ", dmh)
    print("EC: ", ech)
    print("Number of people who are waiting for dose 2:", afd+czd+bvd+dmd+ecd)
    print("AF: ", afd)
    print("CZ: ", czd)
    print("BV: ", bvd)
    print("DM: ", dmd)
    print("EC: ", ecd)
    print("Number of people who is completed vaccination:", afv2d+czv2d+bvv2d+dmv2d+ecd+ecv2d)
    print("AF: ", afv2d)
    print("CZ: ", czv2d)
    print("BV: ", bvv2d)
    print("DM: ", dmv2d)
    print("EC: ", ecv2d)
    print("Total number of patient:", status)
    print("AF: ", af)
    print("CZ: ", cz)
    print("BV: ", bv)
    print("DM: ", dm)
    print("EC: ", ec)
    print()


def show_all_rec(allrecs, vallrec):
    no_of_rec = len(allrecs)
    print("=" * 150)
    print("NAME".center(10) + "|" + "AGE".center(3) + "|" + "PHONE NUMBER".center(12) + "|" +
          "PATIENT ID".center(10) + "|" + "IC NUMBER".center(12) + "|" + "EMAIL".center(20) +
          "|" + "VACCINE CENTRE".center(14) + "|" + "VACCINE CODE".center(12) + "|" + "DOSE 1 DATE".center(12) + "|" +
          "DOSE 2 DATE".center(12) + "|" + "STATUS".center(20))
    print("=" * 150)
    for i in range(no_of_rec):
        print(allrecs[i][0].center(10) + "|" + allrecs[i][1].center(3) + "|" + allrecs[i][2].center(12) + "|" +
              allrecs[i][3].center(10) + "|" + allrecs[i][4].center(12) + "|" + allrecs[i][5].center(20) + "|" +
              allrecs[i][6].center(14) + "|" + vallrec[i][4].center(12) + "|" + vallrec[i][5].center(12) + "|" +
              vallrec[i][6].center(12) + "|" + vallrec[i][7].center(20))
    print("=" * 150)


def main_menu():
    allrecs = []
    fh = open("patient.txt", "r")
    for line in fh:
        my_list = line.strip().split(":")
        allrecs.append(my_list)
    vallrec = []
    fh2 = open("vaccination.txt", "r")
    for line in fh2:
        my_list = line.strip().split(":")
        vallrec.append(my_list)
    while True:
        print("Hi!")
        print("1-New Patient Registration. ")
        print("2-Modify Patient Personal Information. ")
        print("3-Vaccine Administration. ")
        print("4-Search Patient Record and Vaccination Status. ")
        print("5-Statistical Information on Patients Vaccinated. ")
        print("6-All Patient Information. ")
        print("7-Exit. ")
        choice = str(input("Enter your choice. "))
        if choice == '1':
            main_rec = new_patient()
            allrecs.append(main_rec)
        elif choice == '2':
            mod_patient(allrecs, vallrec)
        elif choice == '3':
            v_admin(vallrec)
        elif choice == '4':
            search_patient_record_status(vallrec,allrecs)
        elif choice == '5':
            patient_vac_stat(vallrec)
        elif choice == '6':
            show_all_rec(allrecs,vallrec)
        elif choice == '7':
            print("GoodBye~ Have a nice day! ")
            break
        else:
            print("INVALID INPUT. ")


main_menu()


