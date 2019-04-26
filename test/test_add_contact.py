# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname='test', lastname='test', middlename='test', nickname='test',
                               title='Mr', company='none', address='Addr1', home='123123123',
                               mobile='123123123', work='123123123', fax='123123123', email='123@123.123',
                               bday='7', bmonth='June', byear='1977', aday='12', amonth='August',
                               ayear='2000', address2='none', phone2='none', notes='none'))
    app.session.logout()