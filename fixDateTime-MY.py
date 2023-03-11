from datetime import datetime, timedelta
import re

def clndate(date,date_formats):
    try:
        
        result = re.search(r"^[A-Za-z]+\s\d{1,2},\s\d{4},\s\d{2}:\d{2}\s[A-Z]{2}", date).group()
        for date_format in date_formats:
            try:
                date_object = datetime.strptime(result, date_format)
                # new_format = "%d-%m-%Y"
                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                print(new_date_string)
                return new_date_string
            except:
                pass

    except:
        pass

def date_formating(date_string):
    date_formats = [ '%Y-%m-%d %H:%M:%S', '%Y-%m-%d','%m-%d-%Y', '%Y/%m/%d,%H:%M:%S', '%d-%m-%Y','%d-%m-%Y,%H:%M:%S','%m-%d-%Y,%H:%M:%S', '%d-%m-%Y %H:%M:%S', '%B %d, %Y, %I:%M %p', '%b %d, %Y, %I:%M %p', '%Y%m%dT%H%M%S.%fZ', '%Y%m%dT%H%M%S.%f%z', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%S.%f%z', '%Y-%m-%dT%H:%M:%S.%f', '%Y/%m/%d', '%d.%m.%Y', '%d.%m.%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %I:%M:%S %p', '%m/%d/%Y %I:%M %p', '%m/%d/%y %I:%M:%S %p', '%m/%d/%y %I:%M %p', '%d %B %Y', '%d %b %Y', '%d %B %y', '%d %b %y', '%d,%m,%Y,%I:%M %p', '%m,%d,%Y,%I:%M:%S %p', '%Y,%m,%d,%H:%M:%S', '%m,%d,%y,%I:%M:%S %p', '%d,%b,%Y,%I:%M %p', '%d/%m/%Y %H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%S.%f%z','%m-%d-%Y, %I:%M %p']
    for date_format in date_formats:
        try:
            date_object = datetime.strptime(date_string, date_format)
            # new_format = "%d-%m-%Y"
            new_format="%Y-%m-%d %H:%M:%S"
            new_date_string = date_object.strftime(new_format)
            return new_date_string
        except :
            try:
                new_date_string = clndate(date_string,date_formats)
                if new_date_string:
                    return new_date_string
            except:
                pass  
                        
            #Today with hrs
            try:      
                match = re.search("(\d+) hours", date_string) or re.search("(\d+) Hours", date_string) or re.search("(\d+) hrs", date_string) or re.search("(\d+) Hrs", date_string) or re.search("(\d+) hrs.", date_string) or re.search("(\d+) Hrs.", date_string) or re.search("Today,(\d+) hours", date_string) or re.search("Today,(\d+) Hours", date_string) or re.search("Today,(\d+) hrs", date_string) or re.search("Today,(\d+) Hrs", date_string) or re.search("Today,(\d+) hrs.", date_string) or re.search("Today,(\d+) Hrs.", date_string)  or re.search("today,(\d+) hours", date_string) or re.search("today,(\d+) Hours", date_string) or re.search("today,(\d+) hrs", date_string) or re.search("today,(\d+) Hrs", date_string) or re.search("today,(\d+) hrs.", date_string) or re.search("today,(\d+) Hrs.", date_string)
                if match:
                    hours = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(hours=hours)
                # new_format = "%d-%m-%Y"
                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
                               
            # today with minutes              
            try:      
                match = re.search("(\d+) minutes", date_string) or re.search("(\d+) Minutes", date_string) or re.search("(\d+) min", date_string) or re.search("(\d+) Min", date_string) or re.search("(\d+) min.", date_string) or re.search("(\d+) Min.", date_string) or re.search("Today,(\d+) minutes", date_string) or re.search("Today,(\d+) Minutes", date_string) or re.search("Today,(\d+) min", date_string) or re.search("Today,(\d+) Min", date_string) or re.search("Today,(\d+) min.", date_string) or re.search("Today,(\d+) Min.", date_string)  or re.search("today,(\d+) minutes", date_string) or re.search("today,(\d+) Minutes", date_string) or re.search("today,(\d+) min", date_string) or re.search("today,(\d+) Min", date_string) or re.search("today,(\d+) min.", date_string) or re.search("today,(\d+) Min.", date_string)
                if match:
                    minutes = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(minutes=minutes)
                # new_format = "%d-%m-%Y"
                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass
            
            # Seconds ago
            try:      
                match = re.search("(\d+) seconds", date_string) or re.search("(\d+) Seconds", date_string) or re.search("(\d+) sec", date_string) or re.search("(\d+) Sec", date_string) or re.search("(\d+) sec.", date_string) or re.search("(\d+) Sec.", date_string)
                if match:
                    second = int(match.group(1))
                else:
                    raise ValueError("Invalid date string format")
                now = datetime.now()
                date_object = now - timedelta(seconds=second)
                # new_format = "%d-%m-%Y"
                new_format="%Y-%m-%d %H:%M:%S"
                new_date_string = date_object.strftime(new_format)
                return new_date_string
            except:
                pass

def date_coverter(input_date):
    # input_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = date_formating(input_date)
    dt = datetime.strptime(output, "%Y-%m-%d %H:%M:%S")
    print(dt)
    timestamp = int(dt.timestamp())
    return timestamp

print(date_coverter("8 hours ago")) #add input


# "10-17-2020, 09:38 PM"
# "2023-01-17T17:40:42Z"
# "8 hours ago"
# "28-02-2023"
#2-02-2023
# 22-12-2023
# "12-22-2023,03:34:45"



