from apps.login_registration.models import *


User.objects.create(first_name="Mike", last_name="Henderson", email="mhenderson@yahoo.com", password = '$2b$12$43gQp3LF3EYKWj52Deggwes4sdJjtmpPvzkbe.WgIDmWCkZo5ny8G', password_confirmation = '$2b$12$43gQp3LF3EYKWj52Deggwes4sdJjtmpPvzkbe.WgIDmWCkZo5ny8G')

User.objects.create(first_name="Speros", last_name="Dalton", email="dsperos@hotmail.com", password = '$2b$12$43gQp3LF3EYKWj52Deggwes4sdJjtmpPvzkbe.WgIDmWCkZo5ny8G', password_confirmation = '$2b$12$43gQp3LF3EYKWj52Deggwes4sdJjtmpPvzkbe.WgIDmWCkZo5ny8G')


User.objects.create(first_name="Jimmy", last_name="Jun", email="jjun@gmail.com", password = '$2b$12$43gQp3LF3EYKWj52Deggwes4sdJjtmpPvzkbe.WgIDmWCkZo5ny8G', password_confirmation = '$2b$12$43gQp3LF3EYKWj52Deggwes4sdJjtmpPvzkbe.WgIDmWCkZo5ny8G')

user1 = User.objects.first()
user2 = User.objects.get(id=2)
user3 = User.objects.get(id=3)

Registration.objects.create(registered_user=user1)
Registration.objects.create(registered_user=user2)
Registration.objects.create(registered_user=user3)