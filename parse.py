from HTMLParser import HTMLParser
  
class MyHTMLParser(HTMLParser):  
    def __init__(self):  
        HTMLParser.__init__(self)  
#         self.current_tag = None  
        self.flag = False
        self.name_flag = False
  
    def handle_starttag(self, tag, attrs): 
        if tag == 'td':
            for name,value in attrs:  
                if name == 'id' and value.startswith("job_"):  
                    self.flag = True
                    self.name_flag = False
                    break
                elif name == 'id' and value.startswith("name_"):
                    self.flag = True
                    self.name_flag = True
                    break
                    
    def handle_endtag(self, tag):  
        self.flag = False
  
    def handle_data(self, data):  
        if self.flag:
            print data, 
            if self.name_flag:
                print ' '
  
if __name__ == '__main__': 
    fp = open("./jobtracker.jsp")
    data = fp.read()
    my = MyHTMLParser()  
    my.feed(data)  
    
    
    
