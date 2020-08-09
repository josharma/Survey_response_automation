import csv

with open('C:\\Users\\AW0204TU\\Desktop\\cl_stuff\\survey_response_automation\\Sample_Contact_Survey_Scholar.csv', newline='', mode='r') as csvfile1, open('C:\\Users\\AW0204TU\\Desktop\\cl_stuff\\survey_response_automation\\sample_mentor_database.csv', newline='', mode='r') as in_file, open('C:\\Users\\AW0204TU\\Desktop\\cl_stuff\\survey_response_automation\\sample_mentor_database_output.csv', newline='', mode='w+') as out_file :
    reader_1 = csv.reader(csvfile1, delimiter=",")#, quotechar='|')
    reader_2 = csv.reader(in_file, delimiter=",")
    writer = csv.writer(out_file)
    #reading the column having scholar's name, column number should be adjusted accordingly
#    print('reached_1')
    response_scholar = {}
    scholar_email = {}
    for column in reader_1:
        response_scholar[column[1].replace("-", " ").strip().lower()] = column[3]
        scholar_email[column[2].replace("-", " ").lower().strip()] = column[3]
    #print(response_scholar)
    #print(scholar_email)
    count = 0
    for row in reader_2:
        match_found = False
        for key in response_scholar:
            #print(row[2].strip(), key)
            if row[2].replace("-", " ").lower().strip() == key:
                row[29] = response_scholar[key]
                match_found = True
                #print("Match")
                count += 1
                writer.writerow(row)
                break
            elif row[2] == "" or row[2] == "Potential scholar to match to (Bold means scholar has been interviewed)":
                writer.writerow(row)
                match_found = True
                break
            else:
                match_found = False
                pass
        #print("reached_for_loop_1_end")
        for email in scholar_email:
            #print("email_reached")
            if row[29] == "":
                #print(row[3].replace("-", " ").lower().strip(), email)
                if row[3].replace("-", " ").lower().strip() == email:
                    row[29] = scholar_email[email]
                    match_found = True
                    #print("Match")
                    count += 1
                    writer.writerow(row)
                    break
        if match_found == False:
            writer.writerow(row)
    in_file.close()
    out_file.close()
    print("The total number of matches are ", count)
