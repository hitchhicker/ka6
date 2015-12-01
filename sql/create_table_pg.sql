/*principal database*/
-- DROP DATABASE ka6;
CREATE DATABASE ka6; 
\c ka6

CREATE TABLE Location (
	id SERIAL,
	country VARCHAR(255) NOT NULL,
	region VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Address (
	id SERIAL,
	area VARCHAR(255) NOT NULL,
	street VARCHAR(255) NOT NULL, /*include street number*/
	id_location INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id_location) REFERENCES Location(id)
);

CREATE TABLE Activity (
	id SERIAL,
	title VARCHAR(255) NOT NULL,
	start_date TIMESTAMP WITH TIME ZONE NOT NULL,
	end_date TIMESTAMP WITH TIME ZONE NOT NULL,
	publish_date TIMESTAMP WITH TIME ZONE NOT NULL,
	id_address INTEGER NOT NULL,
	allow_number INTEGER, /*if allowNumber is null, it means infinite*/
	like_number INTEGER DEFAULT 0,
	canceld BOOLEAN DEFAULT FALSE,
	PRIMARY KEY (id),
	FOREIGN KEY (id_address) REFERENCES Address(id)
);
CREATE INDEX index_title
ON Activity (title);

CREATE TABLE TagActivity (
	id SERIAL,
	tag_name VARCHAR(20) NOT NULL,
	id_activity INTEGER NOT NULL,
	FOREIGN KEY (id_activity) REFERENCES Activity(id),
	PRIMARY KEY(id)
);

/* User is reserved word in PostgreSQL*/
CREATE TABLE _User (
	id SERIAL,
	image VARCHAR(2083),
	email VARCHAR(255) UNIQUE NOT NULL,
	password CHAR(32) NOT  NULL, /*if we use MD5 password will be size of 32 bytes*/
	name VARCHAR(255) NOT NULL,
	id_location INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY (id_location) REFERENCES Location(id)

);
CREATE INDEX index_username
ON _User (name);

CREATE TABLE TagUser (
	id SERIAL,
	tag_name VARCHAR(20) NOT NULL,
	id_user INTEGER NOT NULL,
	FOREIGN KEY (id_user) REFERENCES _User(id),
	PRIMARY KEY(id)
);

CREATE TABLE UserActivity (
	id_user INTEGER NOT NULL,
	id_activity INTEGER NOT NULL,
	join_date TIMESTAMP WITH TIME ZONE NOT NULL,
	PRIMARY KEY(id_user,id_activity),
	FOREIGN KEY (id_user) REFERENCES _User(id),
	FOREIGN KEY (id_activity) REFERENCES Activity(id)
);

CREATE TABLE ActivityContent (
	id_activity INTEGER PRIMARY KEY,
	content TEXT NOT NULL,
	FOREIGN KEY (id_activity) REFERENCES Activity(id)
);
--
CREATE TABLE Comment (
	id SERIAL,
	id_activity INTEGER NOT NULL,
	id_comment INTEGER NOT NULL, /*if idComment is 0, it means it's a comment to the Activity*/
	id_user INTEGER NOT NULL,
	comment_date TIMESTAMP WITH TIME ZONE NOT NULL,
	body TEXT NOT NULL,
	FOREIGN KEY (id_user) REFERENCES _User(id),
	FOREIGN KEY (id_activity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);
/*Problem of foreign key ??*/

/*
if we create only one table and 2 indexs fromid and toid
it will be slower while inserting
*/

/*Relation*/

CREATE TABLE Following (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	follow_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_fromid
ON Following (fromid);

CREATE TABLE Follower (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	follow_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_toid
ON Follower (toid);

CREATE TABLE Activity_following (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	follow_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES Activity(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_fromid_activity
ON Activity_following (fromid);

CREATE TABLE Activity_follower (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	follow_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES Activity(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_toid_activity
ON Activity_follower (toid);

CREATE TABLE Friends (
	id_user1 INTEGER NOT NULL,
	id_user2 INTEGER NOT NULL,
	add_date TIMESTAMP WITH TIME ZONE NOT NULL,
	PRIMARY KEY(id_user1, id_user2),
	FOREIGN KEY (id_user1) REFERENCES _User(id),
	FOREIGN KEY (id_user2) REFERENCES _User(id)
);

CREATE TABLE Invitation (
	id SERIAL,
	invitor INTEGER NOT NULL,
	invited INTEGER NOT NULL,
	id_activity INTEGER NOT NULL,
	invite_date TIMESTAMP WITH TIME ZONE NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (invitor) REFERENCES _User(id),
	FOREIGN KEY (invited) REFERENCES _User(id)
);

/*Chat*/
CREATE TABLE Conversation (
	id SERIAL,
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	time TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY (id)
);

CREATE TABLE Reply (
	id SERIAL,
	reply TEXT NOT NULL,
	time TIMESTAMP WITH TIME ZONE NOT NULL,
	conversation_id INTEGER NOT NULL,
	FOREIGN KEY (conversation_id) REFERENCES Conversation(id),
	PRIMARY KEY (id)
);

CREATE TABLE Broadcast (
	id SERIAL,
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	message TEXT NOT NULL,
	send_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY (id)
);

/*Statistic*/
CREATE TABLE Click (
	id SERIAL,
	id_user INTEGER NOT NULL,
	id_activity INTEGER NOT NULL,
	click_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (id_user) REFERENCES _User(id),
	FOREIGN KEY (id_activity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);

CREATE TABLE Search (
	id SERIAL,
	id_user INTEGER NOT NULL,
	id_activity INTEGER NOT NULL,
	search_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (id_user) REFERENCES _User(id),
	FOREIGN KEY (id_activity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);

/*attention: it's l1ke, not like*/
CREATE TABLE L1ke (
	id SERIAL,
	id_user INTEGER NOT NULL,
	id_activity INTEGER NOT NULL,
	like_date TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (id_user) REFERENCES _User(id),
	FOREIGN KEY (id_activity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);
