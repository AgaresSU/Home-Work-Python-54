class Student:
    def __init__(self, name, model, processor, memory):
        self.name = name
        self.note = self.Notebook(model, processor, memory)

    def show(self):
        print(f"{self.name} => {self.note.model}, {self.note.processor}, {self.note.memory}")

    class Notebook:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory


st1 = Student("Roman", "HP", "i7", 16)
st2 = Student("Vladimir", "HP", "i7", 16)

st1.show()
st2.show()
