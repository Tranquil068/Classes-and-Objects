class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, tracks:list, score:float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, change_name):
        self.name = change_name
        print(self.name)
        
    def change_age(self, change_age):
        self.age = change_age
        print(self.age)

    def add_track(self,add_track):
        new_track = self.tracks
        new_track.append(add_track)
        print(self.tracks)
    
    def get_score(self):
        print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
