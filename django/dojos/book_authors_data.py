from apps.book_authors.models import *

print "Creating the Authors"
Author.objects.create(first_name="Mike", last_name="Henderson")
Author.objects.create(first_name="Speros", last_name="Dalton")
Author.objects.create(first_name="John", last_name="Doe")
Author.objects.create(first_name="Jadee", last_name="Johnson")
Author.objects.create(first_name="Jay", last_name="Takkar")


print "Creating five Books"
Book.objects.create(name="C sharp", desc="C sharp by examples.")
Book.objects.create(name="Java", desc="The Ultimate Java book.")
Book.objects.create(name="Python", desc="The Little Python Book.")
Book.objects.create(name="PHP", desc="PHP Cookbook.")
Book.objects.create(name="Ruby", desc="Build Awesome Command Line Applications in Ruby.")


print "Associating the Books with their Authors"
author1 = Author.objects.first()
author2 = Author.objects.get(id=2)
author3 = Author.objects.get(id=3)
author4 = Author.objects.get(id=4)
author5 = Author.objects.get(id=5)

book1 = Book.objects.first()
book2 = Book.objects.get(id=2)
book3 = Book.objects.get(id=3)
book4 = Book.objects.get(id=4)
book5 = Book.objects.get(id=5)

print "Changing the name of the 5th book to C#"
book5.name
book5.desc

book5.name="C#"
book5.desc="Another C# Book."
book5.save()


print "Changing the first_name of the 5th author to Ketul"
author5.first_name
author5.first_name = "Ketul"
author5.save()
author5.first_name


print "Assinging the first author to the first 2 books"
author1.books.add(book1,book2)
for b in author1.books.all():
  b.name
  b.desc

print "Assigning the second author the first 3 books"
author2.books.add(book1,book2,book3)
for b in author2.books.all():
  b.name
  b.desc

print "Assigning the third author to the first 4 books"
author3.books.add(book1,book2,book3,book4)
for b in author3.books.all():
  b.name
  b.desc

print "Assigning the fourth author all of the books"
author4.books.add(book1,book2,book3,book4,book5)
for b in author4.books.all():
  b.name
  b.desc

print "Retrieving all authors for the 3rd book"
for author in Book.objects.get(id=3).authors.all():
  author.first_name
  author.last_name
  author.id

print "Removing the first author for the 3rd book"
Book.objects.get(id=3).authors.get(id=2).delete()
for author in Book.objects.get(id=3).authors.all():
  author.first_name
  author.last_name
  author.id


print "Adding the 5th author to book2"
book2.authors.add(author5)
for author in book2.authors.all():
  author.first_name
  author.last_name

print "Finding all the books that the 3rd author is part of"
for book in Author.objects.get(id=3).books.all():
  book.name
  book.desc