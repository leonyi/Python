from apps.user_login.models import User
 
users = []
 
for i in range(20):
    user = User(first_name='User%dFirstName' % i, 
                last_name='User%dLastName' % i,
                email='user%d@mydomain.com' % i)
    users.append(user)
 
User.objects.bulk_create(users)
