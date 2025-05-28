class Student:
    def hello(self):
        print("Hello!")

    def raise_hand(self):
        print("Raises hand respectfully.")


class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("By the way, did you watch the latest episode of that show?")

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()
