from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text="""
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    def get_details(self):
        return self.name
        
    def is_passing(self):
        return self.garde >= 6.0
        
## Example usage
student1=Student("Reeya",21,8.2)
print(student1.get_details())
if student1.-s_passing():
    print("The student is passing")
else:
    print("The Student is not passing)
 """

## Initialize the splitter
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=270,
    chunk_overlap=0
)

## Perform the split
chunks=splitter.split_text(text)

print(len(chunks))
print(chunks[1])