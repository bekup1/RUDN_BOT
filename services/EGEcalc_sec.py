class Subject:
    def __init__(self, name, min_score, max_score):
        self.name = name
        self.min_score = min_score
        self.max_score = max_score
        self.score = 0
    
    def set_score(self, score):
        if score < self.min_score or score > self.max_score:
            raise ValueError(f"Балл по {self.name} должен быть между {self.min_score} и {self.max_score}")
        self.score = score
    
    def get_score(self):
        return self.score

class SpecialAchievement:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.is_achieved = False
    
    def set_achieved(self, achieved):
        self.is_achieved = achieved
    
    def get_points(self):
        return self.points if self.is_achieved else 0

class EgeCalculator:
    def __init__(self):
        self.russian = Subject("Русский язык", 0, 100)
        self.math = Subject("Математика", 0, 100)
        self.physics = Subject("Физика", 0, 100)
        self.chemistry = Subject("Химия", 0, 100)
        self.biology = Subject("Биология", 0, 100)
        self.history = Subject("История", 0, 100)
        self.social_studies = Subject("Обществознание", 0, 100)
        self.literature = Subject("Литература", 0, 100)
        self.foreign_lang = Subject("Иностранный язык", 0, 100)
        self.informatics = Subject("Информатика", 0, 100)
        self.geography = Subject("География", 0, 100)
        
        self.gto_badge = SpecialAchievement("Золотой значок ГТО", 2)
        self.essay = SpecialAchievement("Сочинение", 10)
        self.volunteering = SpecialAchievement("Волонтерство", 1)
        self.olympiad_winner = SpecialAchievement("Победитель олимпиады", 5)
        
        self.subjects = [
            self.russian, self.math, self.physics, self.chemistry,
            self.biology, self.history, self.social_studies, self.literature,
            self.foreign_lang, self.informatics, self.geography
        ]
        
        self.achievements = [
            self.gto_badge, self.essay, self.volunteering, self.olympiad_winner
        ]
    
    def calculate_total_score(self, required_subjects, additional_subjects=None):
        """
        Рассчитывает общий балл на основе выбранных предметов
        
        :param required_subjects: список обязательных предметов (объекты Subject)
        :param additional_subjects: список дополнительных предметов (объекты Subject)
        :return: общий балл
        """
        if additional_subjects is None:
            additional_subjects = []
        
        for subject in required_subjects:
            if subject.score == 0:
                raise ValueError(f"Не указан балл по обязательному предмету: {subject.name}")
        
        total = sum(subject.get_score() for subject in required_subjects)
        
        if additional_subjects:
            total += max(subject.get_score() for subject in additional_subjects)
        
        total += sum(achievement.get_points() for achievement in self.achievements)
        
        return total
    
    def get_direction_score(self, direction_name):
        """
        Рассчитывает баллы для конкретного направления подготовки
        
        :param direction_name: название направления
        :return: общий балл для направления
        """
        directions = {
            "Информатика и вычислительная техника": [
                [self.russian, self.math],  # обязательные
                [self.physics, self.informatics]  # дополнительные
            ],
            "Строительство": [
                [self.russian, self.math],
                [self.physics, self.chemistry]
            ],
            "Лингвистика": [
                [self.russian, self.foreign_lang],
                [self.history, self.social_studies, self.literature]
            ],
            "Экономика": [
                [self.russian, self.math],
                [self.social_studies, self.foreign_lang, self.geography]
            ],
            "Лечебное дело": [
                [self.russian, self.chemistry],
                [self.biology, self.physics]
            ]
        }
        
        if direction_name not in directions:
            raise ValueError("Указанное направление не найдено")
        
        required, additional = directions[direction_name]
        return self.calculate_total_score(required, additional)

# Пример использования
if __name__ == "__main__":
    calculator = EgeCalculator()
    
    calculator.russian.set_score(85)
    calculator.math.set_score(90)
    calculator.physics.set_score(78)
    calculator.informatics.set_score(88)
    
    calculator.essay.set_achieved(True)
    calculator.gto_badge.set_achieved(True)
    
    direction = "Информатика и вычислительная техника"
    total_score = calculator.get_direction_score(direction)
    
    print(f"Общий балл для направления '{direction}': {total_score}")
    print(f"Из них:")
    print(f"- Русский язык: {calculator.russian.get_score()}")
    print(f"- Математика: {calculator.math.get_score()}")
    print(f"- Физика: {calculator.physics.get_score()}")
    print(f"- Информатика: {calculator.informatics.get_score()}")
    print(f"- Индивидуальные достижения: {sum(a.get_points() for a in calculator.achievements)}")