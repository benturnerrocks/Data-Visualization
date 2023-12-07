import csv



def cleanFile(infilename):
    outfilename = infilename[:-4] + "_clean.csv"
    with open(infilename, 'r', newline='') as csvfileR:
        with open("Cleaned Files/" + outfilename, 'w') as csvfileW:
            reader = csv.reader(csvfileR, quotechar = '\"')
            writer = csv.writer(csvfileW)
            fields = ['Start Date', 'End Date', 'Program Title', 'Faculty Director', 'Term', 'Number of Participants', 'Country', 'Countries Visited', 'Photos']
            writer.writerow(fields)
            next(reader)
            for row in reader:
                array = []
                startYear = int(row[0][:4])
                endYear = startYear
                startMonth = "00"
                endMonth = "00"
                if ("spring" in row[3]) or ("Spring" in row[3]):
                    startYear += 1
                    endYear += 1
                    startMonth = "03"
                    endMonth = "06"
                elif ("break" in row[3]) or ("Break" in row[3]):
                    endYear += 1
                    startMonth = "11"
                    endMonth = "12"
                elif ("winter" in row[3]) or ("Winter" in row[3]):
                    startYear += 1
                    endYear += 1
                    startMonth = "01"
                    endMonth = "03"
                elif ("fall" in row[3]) or ("Fall" in row[3]):
                    startMonth = "08"
                    endMonth = "11"
                elif ("summer" in row[3]) or ("Summer" in row[3]):
                    startMonth = "06"
                    endMonth = "08"

                if row[4] == "NDA":
                    row[4] = 0
                elif "projected" in row[5]:
                    row[4] = row[4].split(" ")[0]
                array.append(str(startYear) + "/" + startMonth) #start date
                array.append(str(endYear) + "/" + endMonth) #end date
                array.append(row[1]) #Name of program
                array.append(row[2]) #faculty director
                array.append(row[3]) #term
                array.append(row[4]) #number of participants
                array.append(row[5]) #country
                array.append(row[6]) #countries visited
                writer.writerow(array)

    csvfileW.close()
    csvfileR.close()


cleanFile('OCS_master.csv')

