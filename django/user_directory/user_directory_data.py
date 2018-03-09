from apps.user_lab.models import *

print "Creating Users"
User.objects.create(first_name="Mike", last_name="Henderson", email="mhenderson@yahoo.com", admin_id=1)
User.objects.create(first_name="Speros", last_name="Dalton", email="dsperos@hotmail.com", admin_id=1)
User.objects.create(first_name="Jimmy", last_name="Jun", email="jjun@gmail.com", admin_id=1)
User.objects.create(first_name="Jay", last_name="Takkar", email="jtakkar@codingdojo.com", admin_id=1)

print "Creating Admin"
Admin.objects.create(first_name="John", last_name="Doe", email="jdoe@jdoe.com", password="$2b$12$YR4m3W/MuYY/moWD.vC6rOvq77BqiHtx11d4t0qe5C8wiySUcWmGq")
