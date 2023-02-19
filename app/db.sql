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

create table user_phrases (
  id integer primary key,
  phrase text
);

create table users (
  id integer primary key,
  user_id text unique
);

create table month (
  id integer primary key,
  my_date date not null unique,
  user integer,
  foreign key(user) references users(id)
);

create table all_users (
  id integer primary key,
  user_id text unique
);

create table phrases (
  id integer primary key,
  key_phrase text,
  phrase text
);
