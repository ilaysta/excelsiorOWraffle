
import requests, random, time, json
from time import sleep
from faker import Faker
from random import getrandbits


print ("################################################")
print ("             DEVELOPED BY @IAMKISHANN ©.        ")
print ("################################################")

def main():

    faker = Faker()
    s = requests.Session()
    s.headers = {
            'Origin':'https://www.excelsiormilano.com',
            'Referer':'https://www.excelsiormilano.com/content/45-nike-air-jordan-1-x-off-white',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
    s.headers.update()
    url = "https://www.excelsiormilano.com/module/antcontactcustom/sendmail"



########edit  this###########
    bdate = "2000-12-31"
    phone = "818-917-0357"
    size = ['8']
    instagram = "still.sell.supreme" 
    country = "United States"
    city = "tarzana"
    zipcode = "91356"
    street = "18643 collins st"

    #if your email 1234lab@gmail.com replase xxx with 1234lab
    email = "ilay1231+{}@gmail.com".format(getrandbits(40)) 
#####################

    fname = faker.first_name(ilay)
    lname = faker.last_name(benshabat)

    data = {
        'first_name':fname,
        'last_name':lname,
        'birth':bdate,
        'mail':email,
        'number':phone,
        'size':random.choice(size),
        'state':instagram,
        'country':country,
        'city':city,
        'zip':zipcode,
        'street':street
    }
    re = s.post(url, data=data)
    
    if re.status_code == 200:
        print("Entry Successful with ", email, "success")
    else:
        print("Error submitting entry", "error")
        

while True:
    main()
    #time.sleep(2)
