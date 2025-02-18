# Task_2
# The relationship between the Boss and Worker classes.


class BaseClass:
    def __init__(self, id_, name, company):
        """Ініціалізація спільних атрибутів"""
        self.id_ = id_
        self.name = name
        self.company = company


class Boss(BaseClass):
    def __init__(self, id_, name, company):
        """Виклик конструктора базового класу для ініціалізації спільних
        атрибутів"""
        super().__init__(id_, name, company)
        self._workers = []

    def add_worker(self, worker):
        """Додаємо працівника до списку, якщо він ще не доданий
        та встановлюємо боса для працівника"""
        if isinstance(worker, Worker) and worker not in self._workers:
            self._workers.append(worker)
            if worker.get_boss() != self:
                worker.set_boss(self)

    def get_workers(self):
        """Повертає список працівників"""
        return self._workers


class Worker(BaseClass):
    def __init__(self, id_, name, company, boss=None):
        """Виклик конструктора базового класу для ініціалізації спільних
        атрибутів"""
        super().__init__(id_, name, company)
        self._boss = None
        if boss:
            self.set_boss(boss)

    def set_boss(self, boss):
        """Перевірка, чи є новий бос екземпляром класу Boss,
        і встановлення його як боса для працівника"""
        if isinstance(boss, Boss):
            self._boss = boss
            if self not in boss.get_workers():
                boss.add_worker(self)

    def get_boss(self):
        """Повертає поточного боса"""
        return self._boss
