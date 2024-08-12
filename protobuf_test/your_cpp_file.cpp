#include <fstream>
#include <iostream>

#include "addressbook.pb.h"  // 컴파일된 프로토콜 버퍼 파일 포함

using namespace std;

void SerializeAddressBook(const AddressBook& address_book) {
  // 데이터를 파일에 직렬화
  fstream output("addressbook.bin", ios::out | ios::trunc | ios::binary);
  if (!address_book.SerializeToOstream(&output)) {
    cerr << "Failed to write address book." << endl;
  }
}

void DeserializeAddressBook(AddressBook& address_book) {
  // 파일에서 데이터를 역직렬화
  fstream input("addressbook.bin", ios::in | ios::binary);
  if (!input) {
    cerr << "Failed to open addressbook.bin." << endl;
    return;
  } else if (!address_book.ParseFromIstream(&input)) {
    cerr << "Failed to parse address book." << endl;
  }
}

int main() {
  // AddressBook 객체 생성
  AddressBook address_book;

  // Person 객체 추가
  Person* person = address_book.add_people();
  person->set_name("John Doe");
  person->set_id(1234);
  person->set_email("johndoe@example.com");

  // 데이터를 직렬화하여 파일에 저장
  SerializeAddressBook(address_book);

  // 새 AddressBook 객체 생성하여 파일에서 역직렬화
  AddressBook new_address_book;
  DeserializeAddressBook(new_address_book);

  // 역직렬화된 데이터 출력
  for (const auto& person : new_address_book.people()) {
    cout << "Name: " << person.name() << endl;
    cout << "ID: " << person.id() << endl;
    cout << "Email: " << person.email() << endl;
  }

  return 0;
}