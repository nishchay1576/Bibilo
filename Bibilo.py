'''
1. Create a Book class which stores the follwing information 
about the book as instance variables:
       authorlast, 
       authorfirst, 
       title, 
       place, 
       publisher, 
       and year
   Also create a instance method:
    "write_bib_entry" 
   which returns a formatted bibliographic reference for the book.
   
2. Create a two instances of Book class in the name of "beauty" and "pynut":
    For getting all the info about authors and other details,
    please make a Google search with below book names:
    book1: The Evidential Power of Beauty
    book2: Python in a Nutshell
    
3. How would you print out the book attribute of the pynut instance?


4. If you type print beauty.write_bib_entry() at the interpreter, what will happen?

5. How would you change the publication year for the beauty book to "2021" and
print it back?
'''

class Book:
    
    # authorlast, authorfirst, title, place, publisher and year
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
  
    def write_bib_entry(self):
        return self.authorlast \
               + ', ' + self.authorfirst \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
  
                                                          
# Create a few instances of Book classes:
beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999", )
pynut  = Book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )


#How would you print out the book attribute of the pynut instance?
print(Book.write_bib_entry(pynut))
#other way is
print (pynut.write_bib_entry())

                            
#If you type print beauty.write_bib_entry() at the interpreter, what will happen?
print(beauty.write_bib_entry())
# It'll give all attributes values

#How would you change the publication year for the beauty book to"2010"?
beauty.year="2021"
print(beauty.write_bib_entry()) # It will year 2021 along with remaining attributes
