# Import the addressbook proto class
import addressbook_pb2

# Add some random data
person = addressbook_pb2.Person()
person.id = 1234 # Mandatory
person.name = "John Doe" # Mandatory
person.email = "jdoe@example.com"

# Return a reference to manipulate `phone`
phone = person.phones.add()

# Add some data on phone
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.WORK

# Store binary data
with open("data.bin", "wb") as file:
    file.write(person.SerializeToString())

# Re-load
with open("data.bin", "rb") as file:
    data = file.read()
    person_reloaded = addressbook_pb2.Person()
    person_reloaded.ParseFromString(data)
print(person_reloaded)
