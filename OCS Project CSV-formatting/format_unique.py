import csv



def cleanFile(infilename):
    outfilename = infilename[:-4] + "_unique.csv"
    with open(infilename, 'r', newline='') as csvfileR:
        with open("Cleaned Files/" + outfilename, 'w') as csvfileW:
            reader = csv.reader(csvfileR, quotechar = '\"')
            writer = csv.writer(csvfileW)
            fields = ['Start Date', 'End Date', 'Program Title', 'Faculty Director', 'Term', 'Number of Participants', 'Country', 'Countries Visited', 'Photos', 'Description']
            writer.writerow(fields)
            next(reader)
            previousRows = dict()
            for row in reader:
                if row[5] == "NDA":
                    row[5] = 0
                elif "projected" in row[5]:
                    row[5] = row[5].split(" ")[0]
                row[5] = int(row[5])
                if row[2] in previousRows.keys():
                    startDate = previousRows[row[2]][0]
                    row[0] = startDate
                    row[5] += previousRows[row[2]][5]
                    if row[3] not in previousRows[row[2]][3]:
                        row[3] += ", " + previousRows[row[2]][3]
                photos = ""
                description = "This OCS ran from " + row[0] + " to " + row[1] + ", and visited " + row[7] + ".\n\n" + "Lead by " + row[3] + " with " + str(row[5]) + " total students in partipation across the years."
                row.append(photos)
                row.append(description)
                previousRows[row[2]] = row
            for unique_rows in previousRows.values():
                writer.writerow(unique_rows)

    csvfileW.close()
    csvfileR.close()


cleanFile('OCS_master_clean.csv')

