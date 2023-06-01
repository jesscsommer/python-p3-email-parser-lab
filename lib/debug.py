#!/usr/bin/env python3

from email_address_parser import EmailAddressParser

if __name__ == '__main__':
    t1 = EmailAddressParser("talk@talk.com, john.jones@flatironschool.com, alexa@amazon.com")
    t2 = EmailAddressParser("talk@talk.com, talk@talk.com alexa@amazon.com what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
    import ipdb; ipdb.set_trace()
