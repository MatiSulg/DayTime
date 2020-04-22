#code was taken from here: https://gis.stackexchange.com/questions/191080/calculating-sunrise-sunset-time-while-considering-topography
import ephem

obs = ephem.Observer()

#Change latitude, longitude and date variables to get
lat = '51.509865'
long = '-0.118092'
date = '2020/4/22'

obs.long = ephem.degrees(long)
obs.lat = ephem.degrees(lat)


obs.date = ephem.Date(date)

sun = ephem.Sun(obs)

r1 = obs.next_rising(sun)
s1 = obs.next_setting(sun)
d1 = obs.next_transit(sun)

print("rising sun (UTC time): ", r1)
print("setting sun (UTC time): ", s1)
print(type(r1))
