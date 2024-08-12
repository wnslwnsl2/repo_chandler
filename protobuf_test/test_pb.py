import addressbook_pb2

address_book = addressbook_pb2.AddressBook()

person = address_book.people.add()
person.name = "Chandler kim"
person.id = 1234
person.email = "hyunjun@bearrobotics.ai"

serialized_data = address_book.SerializeToString()

with open("addressbook.bin","wb") as f:
    f.write(serialized_data)

# 파일에서 읽어오기
with open("addressbook.bin", "rb") as f:
    new_address_book = addressbook_pb2.AddressBook()
    new_address_book.ParseFromString(f.read())

# 역직렬화 후 데이터 사용
for person in new_address_book.people:
    print(f"Name: {person.name}, ID: {person.id}, Email: {person.email}")