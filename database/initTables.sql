
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS FOLLOW;
DROP TABLE IF EXISTS POST;
DROP TABLE IF EXISTS COMMENT;
DROP TABLE IF EXISTS DM;

CREATE TABLE USER(	
    fname 			VARCHAR(20)		   	NOT NULL,
	lname           VARCHAR(20)         NOT NULL,
	username        VARCHAR(20)         NOT NULL,
	password        VARCHAR(20),			
	email           VARCHAR(20),        	
	admin_status    SMALLINT            NOT NULL,       -- 1 : admin , 0 : NOT admin ;
	block_status    SMALLINT            NOT NULL,       -- 1 : blocked , 0 : NOT blocked ;
	
	PRIMARY KEY(username)
);

CREATE TABLE FOLLOW(
	follower 		VARCHAR(20)			NOT NULL,		-- user doing following 
	target	 		VARCHAR(20)			NOT NULL,		-- user being followed
	
	FOREIGN KEY(follower) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(target) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(follower, target)
);

CREATE TABLE POST(
	postID			INT 					AUTO_INCREMENT,
	poster			VARCHAR(20) 			NOT NULL,
	pTime			TIMESTAMP				NOT NULL,		-- post time
	songTitle		VARCHAR(30) 			NOT NULL,
	author			VARCHAR(20)				NOT NULL,		
	video			BLOB					NOT NULL,		-- idk how to store the video. Is it just a hyperlink? !!!!!!!!!!!!!!!!!!!
	caption 		VARCHAR(500),							-- caption is optional
	
	FOREIGN KEY(poster) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(postID)
);

CREATE TABLE COMMENT(
	comID			INT						AUTO_INCREMENT,		-- comment ID number
	sender			VARCHAR(20)				NOT NULL,		
	postID			INT						NOT NULL,		-- post ID number of post comment is on
	message 		VARCHAR(500)			NOT NULL,		
	cTime			TIMESTAMP				NOT NULL,		-- comment time
	
	FOREIGN KEY(sender) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(postID) REFERENCES POST(postID) ON DELETE CASCADE,	-- this should never be updated
	PRIMARY KEY(comID)
);

CREATE TABLE DM(											-- Direct Message
	msgID			INT 					AUTO_INCREMENT,		-- message ID number
	sender			VARCHAR(20) 			NOT NULL,		
	receiver		VARCHAR(20) 			NOT NULL,		
	message			VARCHAR(500),							
	dTime			TIMESTAMP				NOT NULL,		-- DM time
	
	FOREIGN KEY(sender) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(receiver) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(msgID) 
);

