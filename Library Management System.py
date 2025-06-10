# เป้าหมาย: สร้างระบบจัดการข้อมูลหนังสือและสมาชิกในห้องสมุดแบบง่ายๆ

class Book():           # คลาส แม่
    def __init__(self, title, author, isbn):       #สร้างชุดคำสั่ง ให้มี ชื่อหนังสือ, ผู้เขียน, หมายเลขกำกับ
        self.__title = title                       #กำหนดให้รับค่า ชื่อหนังสือ แบบ Capsulation 
        self.__author = author                     #กำหนดให้รับค่า ผู้เขียน แบบ Capsulation
        self.__isbn = isbn                         #กำหนดให้รับค่า ISBN แบบ Capsulation
        
    def __str__(self):                             #สร้างชุดคำสั่ง ให้ print ชื่อหนังสือ, ผู้เขียน, หมายเลขกำกับ
        return (f"Title: {self.__title}, Auther: {self.__author}, ISBN: {self.__isbn}")
    
    def get_title(self):                           #สร้าง Getter_ เพื่อรับค่า ชื่อหนังสือ แล้วเก็บไว้ในคลาสแม่
        return self.__title 
    def get_author(self):                          #สร้าง Getter_ เพื่อรับค่า ชื่อผู้เขียน แล้วเก็บไว้ในคลาสแม่
        return self.__author
    def get_isbn(self):                            #สร้าง Getter_ เพื่อรับค่า ISBN แล้วเก็บไว้ในคลาสแม่
        return self.__isbn
    
class PhysicalBook(Book):                               #คลาสลูก ตัวที่1
    def __init__(self, title, author, isbn, location):  #สร้างุดคำสั่ง เพื่อรับ ค่าเดิม - เพิ่มเติมคือ location
        super().__init__(title, author, isbn)           #super().__init__() สืบทอดคลาสแม่มา แล้วเก็บค่า title, author, isbn เข้าไป
        self.__location = location                      #กำหนดให้รับค่า location แบบ Capsulation
    def get_location(self):                         #สร้าง Getter_ เพื่อรับค่า location เพื่อเก็บเอาไว้
        return self.__location
    def __str__(self):           #คำสั่งนี้ เป็นการ override คำสั่งแม่ หรือเขียนทับคำสั่งคลาสแม่ โดยกำหนดให้ print ชื่อหนังสือ, ผู้เขียน, หมายเลขกำกับ และ location
        return (f"Physical Book - Title: {self._Book__title}, Author: {self._Book__author}, ISBN: {self._Book__isbn}, Location: {self.__location}")
        # สังเกตุดูว่า จะมี self.(เข้าสู่คลาสแม่) | _Book (ตรงนี้สำคัญ เนื่องจากเป็น Capsulation หากแก้ไขจะต้องมีการ name mangling) | __title (ส่วนของชื่อหนังสือ)
          
class Ebook(Book):                                          #คลาสลูก ตัวที่2 - ทำแบบเดียวกับ คลาสลูกตัวที่1
    def __init__(self, title, author, isbn, file_size):      
        super().__init__(title, author, isbn)               
        self.__file_size = file_size                        
        
    def get_file_size(self):                                
        return self.__file_size
    def __str__(self):                     #คำสั่งแบบเดียวกัน กับคลาสลูกตัวที่ 1
        return (f"EBook - Title: {self._Book__title}, Author: {self._Book__author}, ISBN: {self._Book__isbn}, File Size: {self.__file_size}MB")
    
class Library():                                    #คลาสแม่อีกอัน เพื่อเอามาใช้งาน
    def __init__(self):                             #สร้างชุดคำสั่ง ให้ รับค่าอยู่ใน list ว่าง
        self.__books = []
        
    def add_book(self, book):                       #สร้างชุดคำสั่ง เพิ่มหนังสือ
        self.__books.append(book)                   #โดยกำหนดให้ หนังสือที่เพิ่มเข้ามา อยู่ใน list
        print(f"Added: {book.get_title()}")         #แล้ว print บอกว่า เพิ่มหนังสือ: .... 
        
    def list_all_book(self):                        #สร้างชุดคำสั่ง รายละเอียดหนังสือทั้งหมด
        print("\n--- Listing All Books ---")        #print บอกว่า รายละเอียดหนังสือทั้งหมด: .... 
        for b in self.__books:                      #การทำงานคือ กำหนดให้ b วนลูป list หนังสือ
            print(b.__str__())                      #แล้ว print ตัว __str__ ที่มีอยู่ใน class ลูก ทั้งหมด
            
    def find_book_by_title(self,title):                 #สร้างชุดคำสั่ง ค้นหาชื่อหนังสือ
        print(f"\n--- Searching for '{title} ---")      #print บอกว่า หนังสือที่ค้นหา: .... 
        for book in self.__books:                       #การทำงานคือ กำหนดให้ book วนลูปใน list หนังสือ
            if book.get_title() == title:               # เงื่อนไขคือ ถ้า (ชื่อหนังสือ) "ตรงกับ" ไอเจ้าตัว (book) ที่กำลัง (หาค่า/Getter) (ชื่อหนังสือ)  
                return book                             #คืนค่าที่หาได้ ให้กับ book
        return None                                     # แต่ถ้า วนคำสั่งลูปแล้วก็ยังไม่มีหนังสือ  ก็คืนค่า None 
     
    def remove_book(self, isbn):                    #สร้างชุดคำสั่ง ลบหนังสือ จากหมายเลข ISBN
        print(f"removing: {isbn}")                  #print บอกว่า กำลังลบหนังสือที่ค้นหา: .... 
        book_to_remove = None                       #สร้างตัวแปรว่างขึ้นมาก่อน เพื่อรับค่าทีหลัง
        for book in self.__books:                   #ใช้คำสั่งวนลูปอีกรอบ โดยให้ book วนลูป list หนังสือ
            if book.get_isbn() == isbn:             #เงื่อนไข ถ้าหาก ISBN "ตรงกับ" book ที่กำลัง (หาค่า/Getter) ISBN 
                book_to_remove = book               #ให้ เจ้า book เก็บค่าที่หาได้ ไว้ที่ ตัวแปร ที่สร้างไว้ก่อนหน้านี้
                break                               # ยกเลิกคำสั่งวนลูป
        if book_to_remove:                          # เงือนไขต่อมา กำหนดให้ ลบหนังสือที่มีอยู่ในตัวแปร
            self.__books.remove(book_to_remove)     # โดยกำหนดให้ หนังสือที่อยู่ในตัวแปร ลบจาก list หนังสือ
            return True                             # ถ้าหาก มีหนังสืออยู่จริงๆ ก็ ลบ
        else:                                       # แต่ถ้าไม่ ก็ลบไม่ได้
            return False
        
# สร้าง Object เรียกใช้งาน        
lb = Library()
pb = PhysicalBook("Harry Potter", "JK Rolling", "a01", "New arrival")
eb = Ebook("Learning Python", "Mor Gemini Ai", "o001", 50)


lb.add_book(pb)
lb.add_book(eb)

lb.list_all_book()
print("-" * 20)

found_book = lb.find_book_by_title("Harry Potter")
if found_book:
    print(f"here is the book: {found_book}")
else:
    print(f"No book found")
remove_book=lb.remove_book("a01")
if remove_book:
    print(f"the book has been removed")
else:
    print(f"the book hasn't been removed")
print("-" * 20)

lb.list_all_book()
print("-" * 20)

