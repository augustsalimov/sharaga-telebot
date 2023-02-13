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
  ('2023-02-13', 'Л', '604', 1, 1),
  ('2023-02-14', 'Л', '611-1', 4, 4),
  ('2023-02-15', 'Л', '611', 5, 5),
  ('2023-02-16', 'ВЛ', 'информация разнится', 3, 3),
  ('2023-02-17', 'ПЗ', '607', 6, 6),
  ('2023-02-20', 'ПЗ', '', 1, 1),
  ('2023-02-21', 'ПЗ', '', 1, 1),
  ('2023-02-27', 'ПЗ', '', 2, 2),
  ('2023-02-28', 'С', '', 4, 4),
  ('2023-03-01', 'ПЗ', '', 5, 5),
  ('2023-03-02', 'ПЗ', '', 6, 6),
  ('2023-03-03', 'С', '', 6, 7),
  ('2023-03-06', 'ПЗ', '', 2, 2),
  ('2023-03-10', 'Л', '', 6, 7),
  ('2023-03-13', 'Л', '', 1, 1),
  ('2023-03-14', 'С', '', 4, 4),
  ('2023-03-15', 'Л', '', 5, 5),
  ('2023-03-16', 'С', '', 3, 3),
  ('2023-03-17', 'Л', '', 6, 6),
  ('2023-03-20', 'ПЗ', '', 1, 1),
  ('2023-03-21', 'Л', '', 1, 1),
  ('2023-03-22', 'ПЗ', '', 2, 2),
  ('2023-03-23', 'Л', '', 6, 6),
  ('2023-03-24', 'Л', '', 6, 7);
