1.Пока файл остается открытым - операционная система "держит" его за совершаемым процессом и больше никто не может его использовать.

2.Конструкция with нужна для оборачивания блока инструкций менеджером контекста. Ее стоит использовать, для гарантии того, что критические функции выполнятся в любом случае- например, при открытии файла гарантируется, что вне зависимости от введенной в файл информации он закроется, даже если произойдет какая-то ошибка.

3.Сериализация используется для передачи сложных объектов по сети или при записи их в файл(структуры данных преобразуются в "линейную" форму для более быстрой и простой передачи)

4.pickle.load()(модуль Pickle реализует двоичные протоколы для сериализации и десериализации объекта Python) или json.loads()(модуль json стандартной библиотеки, позволяющий выполнять сериализацию и десериализацию JSON).