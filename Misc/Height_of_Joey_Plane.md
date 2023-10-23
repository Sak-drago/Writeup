# Height Of Joeys Plane
How to track an entire plane just through a single image.
## Category
**OSINT**
## Points
**299**
## Challange Description
Mr. Joey Miller this, miller there, miller where. He wants to find the height of his plane after a year. Help him find the lat and long(in decimal upto 4 decimal), speed(mph) and height(feet) of the plane a year and 24 secs after this photo was taken.
## Attached file
![image](https://github.com/Sak-drago/Writeup/assets/116898248/130e11e8-4fa2-43a5-af14-aa8c6d29469b)

## Explanation
We have to find out the lat and long of the plane, speed and height. The basic idea we get is that we have to access the flight namem, id, and the time the photo was taken so that we can add one year and twenty four seconds to it.
We can access the time of the photo through `metadata`. As for flight details, we can access that through [FlightAware](https://www.flightaware.com/)


The website used to find `metadata` is [MetaData2Go](https://www.metadata2go.com/)

![image](https://github.com/Sak-drago/Writeup/assets/116898248/ee49a368-0e75-427e-b415-960c79d537ab)


Here we can see that the image was taken on `6:55:36 3 september 2022`. 
Now 1 year 24 seconds after that would be `6:50:00 3 september 2023`

 The flight can be found using `VT-IFP` on  [FlightAware](https://www.flightaware.com/).

![image](https://github.com/Sak-drago/Writeup/assets/116898248/12293560-2d0e-4aae-8773-2828c3fc754c)


From here we open the tracker logs of the flight and find the log at `6:56:00` since it is 24 seconds added to `6:55:36`

![image](https://github.com/Sak-drago/Writeup/assets/116898248/cad462e0-0239-4f61-baaf-6bc053e93280)


We can notice that :
```sh
Latitude=19.4032	Longitude=77.8842 Height=33,000ft Speed=531mph
```

## Flag
`d4rk{19.4032_77.8842_531_33000}c0de`
