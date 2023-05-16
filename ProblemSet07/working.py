import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    format1= re.search(r"^(\d{1,2}):(\d{2}) ([AP]M) to (\d{1,2}):(\d{2}) ([AP]M)$", s)
    format2= re.search(r"^(\d{1,2}) ([AP]M) to (\d{1,2}) ([AP]M)", s)

    if format1:
        start_hour= int(format1.group(1))
        start_minute= int(format1.group(2))
        start_meridian= format1.group(3)
        end_hour= int(format1.group(4))
        end_mintue= int(format1.group(5))
        end_meridian= format1.group(6)
    else:
        if format2:
            start_hour= int(format2.group(1))
            start_minute= 0
            start_meridian= format2.group(2)
            end_hour= int(format2.group(3))
            end_mintue= 0
            end_meridian= format2.group(4)

    if start_meridian== "PM" and end_meridian=="PM":
        start_hour+=12
        end_hour+=12
    elif start_meridian=="PM":
        start_hour+=12
    elif start_meridian=="AM":
        end_hour+=12
    if start_minute>59 or end_mintue>59:
        raise ValueError
    
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_mintue:02}"
    
if __name__ == "__main__":
    main()