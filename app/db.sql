create table lecturer (
  id integer primary key,
  name text,
  e_mail text
);

create table subject (
  id integer primary key,
  name text,
  lecturer_id integer,
  foreign key(lecturer_id) references lecturer(id)
);

create table day (
  id integer primary key,
  my_date date not null unique,
  l_s text,
  cab text,
  lecturer_id integer,
  subject_id integer,
  foreign key(lecturer_id) references lecturer(id),
  foreign key(subject_id) references subject(id)
);

insert into lecturer (name, e_mail) values 
  ('Миловзоров Д.Е.', 'milovzorovde@stud.rosnou.ru'),
  ('Кокорина Е.А.', 'kokorinaea@stud.rosnou.ru'),
  ('Лихачева Э.В.', 'lihachevaev@stud.rosnou.ru'),
  ('Толмачев А.И.', 'tolmachevai@stud.rosnou.ru'),
  ('Батманова О.В.', 'batmanovaolv@stud.rosnou.ru'),
  ('Былова Н.В.', 'bilovanv@stud.rosnou.ru');

insert into subject (name, lecturer_id) values 
  ('Физика', 1),
  ('Иностранный язык', 2),
  ('Жизненная навигация', 3),
  ('Вероятность и статистика', 4),
  ('Информационные технологии', 5),
  ('Управление информационными ресурсами и проектами', 6),
  ('Архитектура информационных систем', 6);

insert into day (my_date, l_s, cab, lecturer_id, subject_id) values 
  ('2023-02-13', 'л', '', 1, 1),
  ('2023-02-14', 'л', '', 4, 4),
  ('2023-02-15', 'л', '', 5, 5),
  ('2023-02-16', 'вл', '', 3, 3),
  ('2023-02-17', 'пз', '', 6, 6),
  ('2023-02-20', 'пз', '', 1, 1),
  ('2023-02-21', 'пз', '', 1, 1),
  ('2023-02-27', 'пз', '', 2, 2),
  ('2023-02-28', 'с', '', 4, 4),
  ('2023-03-01', 'пз', '', 5, 5),
  ('2023-03-02', 'пз', '', 6, 6),
  ('2023-03-03', 'с', '', 6, 7),
  ('2023-03-06', 'пз', '', 2, 2);
