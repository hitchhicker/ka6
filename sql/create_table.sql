/*principal database*/
/*DROP DATABASE ka6;*/
CREATE DATABASE ka6; 
USE ka6;

CREATE TABLE Activity (
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(255) NOT NULL,
	startDate DATETIME NOT NULL,
	endDate DATETIME NOT NULL,
	publishDate DATETIME NOT NULL,
	allowNumber INT, /*if allowNumber is null, it means infinite*/
	likeNumber INT DEFAULT 0,
	canceld TINYINT(1) DEFAULT 0,
	PRIMARY KEY (id)
)ENGINE = InnoDB;
CREATE INDEX index_title
ON Activity (title);

CREATE TABLE Tag (
	id INT NOT NULL AUTO_INCREMENT,
	tagName VARCHAR(20) NOT NULL,
	idActivity INT NOT NULL,
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY(id)
)ENGINE = InnoDB;

CREATE TABLE User (
	id INT NOT NULL AUTO_INCREMENT,
	image VARCHAR(2083),
	email VARCHAR(255) UNIQUE NOT NULL ,
	password CHAR(32) NOT  NULL, /*if we use MD5 password will be size of 32 bytes*/
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
)ENGINE = InnoDB;
CREATE INDEX index_username
ON User (name);

CREATE TABLE UserActivity (
	idUser INT NOT NULL,
	idActivity INT NOT NULL,
	joinDate DATETIME NOT NULL,
	PRIMARY KEY(idUser,idActivity),
	FOREIGN KEY (idUser) REFERENCES User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id)
)ENGINE = InnoDB;

CREATE TABLE ActivityContent (
	idActivity INT PRIMARY KEY,
	content TEXT NOT NULL,
	FOREIGN KEY (idActivity) REFERENCES Activity(id)
)ENGINE = InnoDB;
--
CREATE TABLE Comment (
	id INT NOT NULL AUTO_INCREMENT,
	idActivity INT NOT NULL,
	idComment INT NOT NULL, /*if idComment is 0, it means it's a comment to the Activity*/
	idUser INT NOT NULL,
	commentDate DATETIME NOT NULL,
	body TEXT NOT NULL,
	FOREIGN KEY (idUser) REFERENCES User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;
/*Problem of foreign key ??*/

/*
if we create only one table and 2 indexs fromid and toid
it will be slower while inserting
*/

/*Relation*/

CREATE TABLE Following (
	fromid INT NOT NULL,
	toid INT NOT NULL,
	followDate DATETIME NOT NULL,
	FOREIGN KEY (fromid) REFERENCES User(id),
	FOREIGN KEY (toid) REFERENCES User(id),
	PRIMARY KEY(fromid, toid)
)ENGINE = InnoDB;
CREATE INDEX index_fromid
ON Following (fromid);

CREATE TABLE Follower (
	fromid INT NOT NULL,
	toid INT NOT NULL,
	followDate DATETIME NOT NULL,
	FOREIGN KEY (fromid) REFERENCES User(id),
	FOREIGN KEY (toid) REFERENCES User(id),
	PRIMARY KEY(fromid, toid)
)ENGINE = InnoDB;
CREATE INDEX index_toid
ON Follower (toid);

CREATE TABLE Activity_following (
	fromid INT NOT NULL,
	toid INT NOT NULL,
	followtime DATETIME NOT NULL,
	FOREIGN KEY (fromid) REFERENCES User(id),
	FOREIGN KEY (toid) REFERENCES Activity(id),
	PRIMARY KEY(fromid, toid)
)ENGINE = InnoDB;
CREATE INDEX index_fromid
ON Activity_following (fromid);

CREATE TABLE Activity_follower (
	fromid INT NOT NULL,
	toid INT NOT NULL,
	followtime DATETIME NOT NULL,
	FOREIGN KEY (fromid) REFERENCES User(id),
	FOREIGN KEY (toid) REFERENCES Activity(id),
	PRIMARY KEY(fromid, toid)
)ENGINE = InnoDB;
CREATE INDEX index_toid
ON Activity_follower (toid);

CREATE TABLE Friends (
	idUser1 INT NOT NULL,
	idUser2 INT NOT NULL,
	addDate DATETIME NOT NULL,
	PRIMARY KEY(idUser1, idUser2),
	FOREIGN KEY (idUser1) REFERENCES User(id),
	FOREIGN KEY (idUser2) REFERENCES User(id)
)ENGINE = InnoDB;

CREATE TABLE Invitation (
	id INT NOT NULL AUTO_INCREMENT,
	invitor INT NOT NULL,
	invited INT NOT NULL,
	idActivity INT NOT NULL,
	inviteDate DATETIME NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (invitor) REFERENCES User(id),
	FOREIGN KEY (invited) REFERENCES User(id)
)ENGINE = InnoDB;

/*Chat*/
CREATE TABLE Conversation (
	id INT NOT NULL AUTO_INCREMENT,
	fromid INT NOT NULL,
	toid INT NOT NULL,
	time DATETIME NOT NULL,
	FOREIGN KEY (fromid) REFERENCES User(id),
	FOREIGN KEY (toid) REFERENCES User(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;

CREATE TABLE Reply (
	id INT NOT NULL AUTO_INCREMENT,
	reply TEXT NOT NULL,
	time DATETIME NOT NULL,
	conversation_id INT NOT NULL,
	FOREIGN KEY (conversation_id) REFERENCES Conversation(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;

CREATE TABLE Broadcast (
	id INT NOT NULL AUTO_INCREMENT,
	fromid INT NOT NULL,
	toid INT NOT NULL,
	message TEXT NOT NULL,
	sendDate DATETIME NOT NULL,
	FOREIGN KEY (fromId) REFERENCES User(id),
	FOREIGN KEY (toid) REFERENCES User(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;

/*Statistic*/
CREATE TABLE Click (
	id INT NOT NULL AUTO_INCREMENT,
	idUser INT NOT NULL,
	idActivity INT NOT NULL,
	clickDate DATETIME NOT NULL,
	FOREIGN KEY (idUser) REFERENCES User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;

CREATE TABLE Search (
	id INT NOT NULL AUTO_INCREMENT,
	idUser INT NOT NULL,
	idActivity INT NOT NULL,
	searchDate DATETIME NOT NULL,
	FOREIGN KEY (idUser) REFERENCES User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;

/*attention: it's l1ke, not like*/
CREATE TABLE L1ke (
	id INT NOT NULL AUTO_INCREMENT,
	idUser INT NOT NULL,
	idActivity INT NOT NULL,
	likeDate DATETIME NOT NULL,
	FOREIGN KEY (idUser) REFERENCES User(id),
	FOREIGN KEY (idActivity) REFERENCES Activity(id),
	PRIMARY KEY (id)
)ENGINE = InnoDB;
