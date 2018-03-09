from apps.dojo_ninjas.models import *

print "Creating the Dojos"
Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")

print "Creating the Ninjas"
dojo1 = Dojo.objects.first()
Ninja.objects.create(first_name="John", last_name="Doe", dojo=dojo1)
dojo2 = Dojo.objects.get(id=2) 
Ninja.objects.create(first_name="Waylon", last_name="Dalton", dojo=dojo2)
dojo3 = Dojo.objects.get(id=3)
Ninja.objects.create(first_name="Justine", last_name="Henderson", dojo=dojo3)


print "Creating the Ninjas, who belong to the Silicon Valley Dojo"
Ninja.objects.create(first_name="Angela", last_name="Walker", dojo=dojo1)
Ninja.objects.create(first_name="Eddie", last_name="Randolph", dojo=dojo1)
Ninja.objects.create(first_name="Janet", last_name="Jackson", dojo=dojo1)

print "Creating the Ninjas, who belong to the Seattle Dojo"
Ninja.objects.create(first_name="Janet", last_name="Wagner", dojo=dojo2)
Ninja.objects.create(first_name="Cleveland", last_name="Robins", dojo=dojo2)
Ninja.objects.create(first_name="Jackson", last_name="Jackson", dojo=dojo2)

print "Creating the Ninjas, who belong to the New York Dojo"
Ninja.objects.create(first_name="James", last_name="Smith", dojo=dojo3)
Ninja.objects.create(first_name="Steve", last_name="Hernandez", dojo=dojo3)
Ninja.objects.create(first_name="Carlos", last_name="Menlo", dojo=dojo3)
Ninja.objects.create(first_name="Jackson", last_name="Jackson", dojo=dojo2)


print "Getting all Ninjas belonging to the New York Dojo."
for ninja in Dojo.objects.get(id=3).ninjas.all():
  print "{} {}".format(ninja.first_name, ninja.last_name)

print "Getting all Ninjas belonging to the Silicon Valley Dojo."
for ninja in Dojo.objects.get(id=1).ninjas.all():
  print "{} {}".format(ninja.first_name, ninja.last_name)

print "Getting all Ninjas belonging to the Seattle Dojo."
for ninja in Dojo.objects.get(id=2).ninjas.all():
  print "{} {}".format(ninja.first_name, ninja.last_name)


print "Deleting all ninjas in Seattle:
for ninja in Dojo.objects.get(id=2).ninjas.all():
...   ninja.delete()
