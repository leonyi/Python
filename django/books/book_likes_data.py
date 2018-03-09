from apps.likes_books.models import *

print "Creating Users"
User.objects.create(first_name="Mike", last_name="Henderson", email="mhenderson@yahoo.com")
User.objects.create(first_name="Speros", last_name="Dalton", email="dsperos@hotmail.com")
User.objects.create(first_name="John", last_name="Doe", email="jdoe@jdoe.com")
User.objects.create(first_name="Jadee", last_name="Johnson", email="jjohnson@gmail.com")
User.objects.create(first_name="Jay", last_name="Takkar", email="jtakkar@codingdojo.com")

print "Creating Books"
Book.objects.create(name="C sharp", desc="C sharp by examples.", uploader_id=1)
Book.objects.create(name="Java", desc="The Ultimate Java book.", uploader_id=1)
Book.objects.create(name="Python", desc="The Little Python Book.", uploader_id=2)
Book.objects.create(name="PHP", desc="PHP Cookbook.",uploader_id=2)
Book.objects.create(name="Ruby", desc="Build Awesome Command Line Applications in Ruby.", uploader_id=3)
Book.objects.create(name="Introduction to Algorithms", desc="The ultimate algorithm book.", uploader_id=3)


print "Instantiating the users."
user1 = User.objects.first()
user2 = User.objects.get(id=2)
user3 = User.objects.get(id=3)
user4 = User.objects.get(id=4)
user5 = User.objects.get(id=5)

print "Instantiating books."
book1 = Book.objects.first()
book2 = Book.objects.get(id=2)
book3 = Book.objects.get(id=3)
book4 = Book.objects.get(id=4)
book5 = Book.objects.get(id=5)
book6 = Book.objects.get(id=6)

print "Setting the first user to like the first book and the last."
user1.liked_books=book1,book6

print "Setting the second user to like the first and the second books."
user2.liked_books=book1,book2

print "Setting the third user to like all the books."
user3.liked_books=Book.objects.all()

print "Showing all users who like the first book."
for user in book1.liked_by.all():
    print "{} {}".format(user.first_name, user.last_name)

print "Showing the user who uploaded the first book"
book1.uploader.first_name

print "Showing the users who liked the second book."
for u in book2.liked_by.all():
    print "{} {}".format(u.first_name, u.last_name)

print "Showing the user who uploaded the second book."
book2.uploader.first_name
