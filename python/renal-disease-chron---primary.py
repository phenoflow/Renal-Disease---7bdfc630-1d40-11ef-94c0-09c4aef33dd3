# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"K02yz00","system":"readv2"},{"code":"K023.00","system":"readv2"},{"code":"K02..12","system":"readv2"},{"code":"K02z.00","system":"readv2"},{"code":"K100100","system":"readv2"},{"code":"1Z13.00","system":"readv2"},{"code":"1Z11.00","system":"readv2"},{"code":"K02..00","system":"readv2"},{"code":"K0A3700","system":"readv2"},{"code":"K02..11","system":"readv2"},{"code":"K0A3300","system":"readv2"},{"code":"K02y000","system":"readv2"},{"code":"K05..00","system":"readv2"},{"code":"K100000","system":"readv2"},{"code":"Kyu2100","system":"readv2"},{"code":"1Z14.00","system":"readv2"},{"code":"1Z10.00","system":"readv2"},{"code":"1Z12.00","system":"readv2"},{"code":"K02y300","system":"readv2"},{"code":"K0A3500","system":"readv2"},{"code":"N03","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('renal-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["renal-disease-chron---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["renal-disease-chron---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["renal-disease-chron---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
