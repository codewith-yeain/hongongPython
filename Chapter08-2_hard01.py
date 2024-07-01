# StudentList 클래스 구현하기 

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class StudentList:
    def __init__(self):
        self.students = []

    def append(self, student):
        self.students.append(student)

    def get_average(self):
        total = 0
        for student in self.students:
            total += student.score
        return total / len(self.students)

    def get_first_by_score(self):
        max_score = self.students[0].score
        max_student = self.students[0].name

        for student in self.students[1:]:
            if student.score > max_score:
                max_score = student.score
                max_student = student.name

        return max_student

    def get_last_by_score(self):
        min_score = self.students[0].score
        min_student = self.students[0].name

        for student in self.students[1:]:
            if student.score < min_score:
                min_score = student.score
                min_student = student.name

        return min_student


students = StudentList()
students.append(Student("구름", 100))
students.append(Student("별", 49))
students.append(Student("초코", 81))
students.append(Student("아지", 90))

print(f"학급의 평균 점수는 {students.get_average()}입니다.")
print(f"가장 성적이 높은 학생은 {students.get_first_by_score()}입니다.")
print(f"가장 성적이 낮은 학생은 {students.get_last_by_score()}입니다.")
