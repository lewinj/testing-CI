"""

Homework 4 part 2
ZIP It Up
by James Lewin

The function can determine locations with ZIP codes, ZIP codes by location, 
and distances based on locations.

"""
import hw4_util
import math

def location_by_zip(zip_codes, code):
    """
    The function returns a locations based on a user inputed zip code
    """
    #Searches through the list of zip codes when it finds a match it prints the matching info.
    for i in range(len(zip_codes)):
        if zip_codes[i][0] == code:
            return (zip_codes[i][1], zip_codes[i][2], zip_codes[i][3], zip_codes[i][4], zip_codes[i][5])
    return ()

def zip_by_location(zip_codes, location):
    """
    The function determines the Zip codes of a specific location tuple:(city,state)
    """
    location = (location[0].lower(), location[1].lower())
    zips = []
    #The for loop goes through the list of ZIP codes and finds the matching city names and state abbreviations.
    for i in range(len(zip_codes)):
        #When the matching city and state names are found it addsthe ZIP code to the list of coresponding zip codes
        if location[0].lower() == zip_codes[i][3].lower() and location[1].upper() == zip_codes[i][4]:
            zips.append(zip_codes[i][0])
    return zips

def distance_between(zip_codes, zip1, zip2):
    """
    The function calulates the distance between two zip codes based on coordinates and the given formulae.
    """
    #Gets the coordinates based on the zip codes
    location1 = location_by_zip(zip_codes, zip1)
    location2 = location_by_zip(zip_codes, zip2)

    if location1 == () or location2 == ():
        return ()
    #The next lines convert the latitude and longitude to radians.
    lat1 = rad(location1[0])
    lat2 = rad(location2[0])
    lon1 = rad(location1[1])
    lon2 = rad(location2[1])
    
    change_lat = lat2 - lat1
    change_lon = lon2 - lon1
    #Calculates the distance betweenthe two coordinates.
    arc = ((math.sin(change_lat/2)) ** 2) + (math.cos(lat1) * math.cos(lat2) * (math.sin(change_lon/2)) ** 2 )
    distance = (2 * 3959.191) * math.asin(arc ** 0.5)
    return distance

def rad(num):
    """
    The function converts a number to radians.
    """
    num = float(num)
    num = num * ((2 * math.pi)/360)
    return num

def coordinate_format(latitude, longitude):
    """
    The function takes the fractional degrees latitude and longitudes and 
    formats them to use degrees, minutes, and seconds that the output requires.
    """
    lat_direction = ""
    long_direction = ""
    #The if statements determine the direction designators.
    if latitude > 0:
        lat_direction = "N"
    elif latitude < 0:
        lat_direction = "S"
        latitude = latitude * -1
     
    if longitude > 0:
        long_direction = "E"
    elif longitude < 0:
        long_direction = "W"
        longitude = longitude * -1
    #The calulations first convert the degrees to seconds.        
    latitude = latitude * 3600
    longitude = longitude * 3600
    #Then we determine the fractional seconds from that.
    latitude_sec = latitude % 60
    longitude_sec = longitude % 60
    #Then we calculate the minutes.
    latitude_min = int((latitude % 3600)/60)
    longitude_min = int((longitude % 3600)/60)
    #And finally the degrees.
    latitude_deg = int(latitude / 3600) 
    longitude_deg = int(longitude / 3600)
   
    return "({:03d}\xb0{}'{:.02f}\"{},{:03d}\xb0{}'{:.02f}\"{})"\
           .format(latitude_deg, int(latitude_min), latitude_sec, lat_direction,longitude_deg, int(longitude_min), longitude_sec, long_direction)
   
if __name__ == "__main__":   
    command = "0"
    zip_codes = hw4_util.read_zip_all()
    
    while command.lower() != "end":
        command = input("Command ('loc', 'zip', 'dist', 'end') => ")
        print(command)
        #For the loc command
        if command.lower() == "loc":
            code = input("Enter a ZIP Code to lookup => ")
            print(code)
            result = location_by_zip(zip_codes, code)
            #THE if statement formats the output.
            if result == ():
                print("Invalid or unknown ZIP Code\n")
            else:
                print("ZIP Code {} is in {}, {}, {} county, \ncoordinates: {}\n"\
                      .format(code, result[2],result[3], result[4], coordinate_format(result[0], result[1])))
               
        #For the ZIP command   
        elif command.lower() == "zip":
            #Gets relevant parameters from user
            city = input("Enter a city name to lookup => ")
            print(city)
            state = input("Enter the state name to lookup => ")
            print(state)
            
            location = (city,state)
            zips = zip_by_location(zip_codes, location)
            #The if statement formats the output.
            if zips == []:
                print("No ZIP Code found for {}, {}\n".format(location[0].title(), location[1].upper()))
            else:
                print("The following ZIP Code(s) found for {}, {}: ".format(location[0].title(), location[1].upper())\
                      + ", ".join(zips) + "\n")
                
        #For distance command 
        elif command.lower() == "dist":
            zip1 = input("Enter the first ZIP Code => ")
            print(zip1)
            zip2 = input("Enter the second ZIP Code => ")
            print(zip2)
            distance = distance_between(zip_codes, zip1, zip2)
            #The if statement formats the output.
            if distance == ():
                print("The distance between {} and {} cannot be determined\n".format(zip1, zip2))
            else:
                print("The distance between {} and {} is {:.02f} miles\n".format(zip1, zip2, distance))
                
        elif command.lower() != "end":
            print("Invalid command, ignoring\n")
    print("\nDone")