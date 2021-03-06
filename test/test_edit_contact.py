from model.contact import Contact
from random import randrange
import allure


def test_edit_random_contact(app, orm, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(orm.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="Del Contact"))
        old_contacts = orm.get_contact_list()
    with allure.step('When I modify the contact'):
        index = randrange(len(old_contacts))
        contact = Contact(firstname='updated test', lastname='updated test', middlename='updated test',
                          nickname='updated test', title='updated Mr', company='updated none', address='updated Addr1',
                          homephone='222222222', mobilephone='222222222', workphone='222222222', fax='222222222', email1='222@222.222',
                          bday='2', bmonth='July', byear='1922', aday='22', amonth='october', ayear='2002',
                          address2='updated none', secondaryphone='updated none', notes='updated none')
        contact.id = old_contacts[index].id
        app.contact.edit_contact_by_id(contact.id, contact)
    with allure.step('Then the new contact list is equal to the contact list with modified contact'):
        new_contacts = orm.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            new_contacts = list(map(app.contact.remove_extra_spaces_in_contact_names, new_contacts))
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


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
