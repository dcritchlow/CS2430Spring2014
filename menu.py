#!/usr/bin/python
import sys

def quit():
    print 'Thank You! Bye Bye!'
    sys.exit()

def display_all():
    print '\nDisplay All Records\n'

def query_record():
    print '\nSearch for Term in Record\n'

def mymenu():
    print """
        1: Display all Records
        2: Search for a Term
        5: Quit
    """

menu = {
    5: quit,
    1: display_all,
    2: query_record
}

def main():
    while True:
        # print menu
        mymenu()
        try:
            answer = int(raw_input("Make a selection: "))
            if answer in menu:
                menu[answer]()
            else:
                print '\nPlease choose a valid option\n'
        except ValueError:
            print 'Please enter a valid number'

if __name__ == '__main__':
    main()
