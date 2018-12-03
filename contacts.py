def get_newcontact(contacts):
	name = input("Name:")
	address = input("Address:")
	phone_num = input("Phone Number:")
	email_add = input("Email Address:")
	new_contact= []
	new_contact.append(name)
	new_contact.append(address)
	new_contact.append(phone_num)
	new_contact.append(email_add)
	contacts.append(new_contact)
	return contacts

def get_addressbook(contacts):
	print('')
	print("Address Book:")
	for each in contacts:
		print ('  '.join(contacts[contacts.index(each)]))
	print('')

def get_search(contacts):
	count = 0
	user_search = input("Please enter the name that you want to search for:")
	for each in contacts:
		if user_search == each[0]:
			print('')
			print('  '.join(contacts[contacts.index(each)]) + '\n')
			count += 1
	if count != 1:
		print("There is no contact with that name in your address book.")
	return contacts

def get_modify(contacts):
	find = True
	check = True
	count = 0
	while find is True:
		user_modify = input("Please enter the name you want to modify:")
		for each in contacts:
			for x in each:
				if user_modify == x:
					print('')
					modify = contacts.index(each)
					print('  '.join(contacts[contacts.index(each)]) + '\n')
					count += 1
					find = False
		if count != 1:
			print("There is no contact with that name in your address book")
	while check is True:
		print("Which aspect of information do you want to modify.")
		user_choice = input("1. Name 2. Address 3. Phone Number 4. Email 5. Exit:")
		if user_choice not in ["1","2","3","4","5"]:
			print("Please input a valid choice from 1 to 5!")
			print("")
		else:
			if user_choice == "1":
				contacts[modify][0] = input("Please enter new name:")
				print('  '.join(contacts[modify]))
			elif user_choice == "2":
				contacts[modify][1] = input("Please enter new address:")
				print('  '.join(contacts[modify]))
			elif user_choice == "3":
				contacts[modify][2] = input("Please enter new number:")
				print('  '.join(contacts[modify]))
			elif user_choice == "4":
				contacts[modify][3] = input("Please enter new email:")
				print('  '.join(contacts[modify]))
			elif user_choice == "5":
				print('  '.join(contacts[modify]))
				check = False
	return contacts

def get_delete(contacts):
	user_delete = input("Please enter the name that you want to delete:")
	count = 0
	for each in contacts:
		for x in each:
			if user_delete == x:
				contacts.remove(each)
				count += 1
			if count != 1:
				print("There is no contact with that name!")
	return contacts

def main():
	x = True
	contactFile = open('contacts.txt','r')
	contacts = []
	for line in contactFile:
		line = line.strip('\n')
		each_contacts = line.split(sep='\t' * 2)
		contacts.append(each_contacts)
	contactFile.close()
	while x is True:
		contactFile.close()
		print("1. Add new contact", end='\n')
		print("2. Print the Address Book", end='\n')
		print("3. Search for a contact", end='\n')
		print("4. Modify a contact", end='\n')
		print("5. Delete a contact", end='\n')
		print("6. Exit")
		user = input("Please enter your option:")
		if user not in ["1", "2", "3", "4", "5", "6"]:
			print("Please enter a valid option between 1 to 6!")
		else:
			if user == "1":
				get_newcontact(contacts)
				print("The contact you enter has been added!" + '\n')
			elif user == "2":
				print(get_addressbook(contacts))
			elif user == "3":
				get_search(contacts)
			elif user == "4":
				get_modify(contacts)
			elif user == "5":
				get_delete(contacts)
			elif user == "6":
				contactFile = open('contacts.txt','w')
				for each in contacts:
					for x in each:
						if x == each[-1]:
							contactFile.write(str(x) + '\n')
						else:
							contactFile.write(str(x) + '\t' + '\t')
				contactFile.close()
				x = False
main()