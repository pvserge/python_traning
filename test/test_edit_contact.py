from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Del Contact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='updated test', lastname='updated test', middlename='updated test',
                      nickname='updated test', title='updated Mr', company='updated none', address='updated Addr1',
                      home='222222222', mobile='222222222', work='222222222', fax='222222222', email='222@222.222',
                      bday='2', bmonth='July', byear='1922', aday='22', amonth='October', ayear='2002',
                      address2='updated none', phone2='updated none', notes='updated none')
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_first_contact_first_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Del Contact"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname='updated test new')
#    contact.id = old_contacts[0].id
#    contact.lastname = old_contacts[0].lastname
#    app.contact.edit_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_first_contact_birth_year(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Del Contact"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(byear='1977')
#    contact.id = old_contacts[0].id
#    contact.lastname = old_contacts[0].lastname
#    contact.firstname = old_contacts[0].firstname
#    app.contact.edit_first_contact(Contact(byear='1977'))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
