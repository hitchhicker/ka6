/*principal database*/
/*DROP DATABASE ka6;*/
CREATE DATABASE ka6; 
\c ka6

CREATE TABLE Activity (
	id SERIAL,
	title VARCHAR(255) NOT NULL,
	startDate TIMESTAMP WITH TIME ZONE NOT NULL,
	endDate TIMESTAMP WITH TIME ZONE NOT NULL,
	publishDate TIMESTAMP WITH TIME ZONE NOT NULL,
	allowNumber INTEGER, /*if allowNumber is null, it means infinite*/
	likeNumber INTEGER DEFAULT 0,
	canceld BOOLEAN DEFAULT FALSE,
	PRIMARY KEY (id)
);
CREATE INDEX index_title
ON Activity (title);

CREATE TABLE Tag (
	id SERIAL,
	tagName VARCHAR(20) NOT NULL,
	idActivity INTEGER NOT NULL,
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY(id)
);

/* User is reserved word in PostgreSQL*/
CREATE TABLE _User (
	id SERIAL,
	image VARCHAR(2083),
	email VARCHAR(255) UNIQUE NOT NULL,
	password CHAR(32) NOT  NULL, /*if we use MD5 password will be size of 32 bytes*/
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX index_username
ON _User (name);

CREATE TABLE TagUser (
	id SERIAL,
	tagName VARCHAR(20) NOT NULL,
	idUser INTEGER NOT NULL,
	FOREIGN KEY (idUser) REFERENCES _User(id),
	PRIMARY KEY(id)
);

CREATE TABLE UserActivity (
	idUser INTEGER NOT NULL,
	idActivity INTEGER NOT NULL,
	joinDate TIMESTAMP WITH TIME ZONE NOT NULL,
	PRIMARY KEY(idUser,idActivity),
	FOREIGN KEY (idUser) REFERENCES _User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id)
);

CREATE TABLE ActivityContent (
	idActivity INTEGER PRIMARY KEY,
	content TEXT NOT NULL,
	FOREIGN KEY (idActivity) REFERENCES Activity(id)
);
--
CREATE TABLE Comment (
	id SERIAL,
	idActivity INTEGER NOT NULL,
	idComment INTEGER NOT NULL, /*if idComment is 0, it means it's a comment to the Activity*/
	idUser INTEGER NOT NULL,
	commentDate TIMESTAMP WITH TIME ZONE NOT NULL,
	body TEXT NOT NULL,
	FOREIGN KEY (idUser) REFERENCES _User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
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
	followDate TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_fromid
ON Following (fromid);

CREATE TABLE Follower (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	followDate TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_toid
ON Follower (toid);

CREATE TABLE Activity_following (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	followtime TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES Activity(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_fromid_activity
ON Activity_following (fromid);

CREATE TABLE Activity_follower (
	fromid INTEGER NOT NULL,
	toid INTEGER NOT NULL,
	followtime TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromid) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES Activity(id),
	PRIMARY KEY(fromid, toid)
);
CREATE INDEX index_toid_activity
ON Activity_follower (toid);

CREATE TABLE Friends (
	idUser1 INTEGER NOT NULL,
	idUser2 INTEGER NOT NULL,
	addDate TIMESTAMP WITH TIME ZONE NOT NULL,
	PRIMARY KEY(idUser1, idUser2),
	FOREIGN KEY (idUser1) REFERENCES _User(id),
	FOREIGN KEY (idUser2) REFERENCES _User(id)
);

CREATE TABLE Invitation (
	id SERIAL,
	invitor INTEGER NOT NULL,
	invited INTEGER NOT NULL,
	idActivity INTEGER NOT NULL,
	inviteDate TIMESTAMP WITH TIME ZONE NOT NULL,
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
	sendDate TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (fromId) REFERENCES _User(id),
	FOREIGN KEY (toid) REFERENCES _User(id),
	PRIMARY KEY (id)
);

/*Statistic*/
CREATE TABLE Click (
	id SERIAL,
	idUser INTEGER NOT NULL,
	idActivity INTEGER NOT NULL,
	clickDate TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (idUser) REFERENCES _User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);

CREATE TABLE Search (
	id SERIAL,
	idUser INTEGER NOT NULL,
	idActivity INTEGER NOT NULL,
	searchDate TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (idUser) REFERENCES _User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);

/*attention: it's l1ke, not like*/
CREATE TABLE L1ke (
	id SERIAL,
	idUser INTEGER NOT NULL,
	idActivity INTEGER NOT NULL,
	likeDate TIMESTAMP WITH TIME ZONE NOT NULL,
	FOREIGN KEY (idUser) REFERENCES _User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
);
