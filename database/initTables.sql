
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
	admin_status    SMALLINT            NOT NULL,       	-- 1 : admin , 0 : NOT admin ;
	block_status    SMALLINT            NOT NULL,       	-- 1 : blocked , 0 : NOT blocked ;
	
	PRIMARY KEY(username)
);

CREATE TABLE FOLLOW(
	follower 		VARCHAR(20)			NOT NULL,			-- user doing following 
	target	 		VARCHAR(20)			NOT NULL,			-- user being followed
	
	FOREIGN KEY(follower) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(target) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(follower, target)
);

CREATE TABLE POST(
	post_id			INT 					AUTO_INCREMENT,
	poster			VARCHAR(20) 			NOT NULL,
	song_title		VARCHAR(30) 			NOT NULL,
	artist			VARCHAR(30)				NOT NULL,		
	song_link		VARCHAR(100)			NOT NULL,			-- hyperlink to Spotify Song link
	image			VARCHAR(100)			NOT NULL,			-- hyperlink to image
	caption 		VARCHAR(500),								-- caption is optional
	ptime			TIMESTAMP				NOT NULL,			-- post time
	
	FOREIGN KEY(poster) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(post_id)
);

CREATE TABLE COMMENT(
	com_id			INT						AUTO_INCREMENT,		-- comment ID number
	sender			VARCHAR(20)				NOT NULL,		
	post_id			INT						NOT NULL,			-- post ID number of post comment is on
	message 		VARCHAR(500)			NOT NULL,		
	ctime			TIMESTAMP				NOT NULL,			-- comment time
	
	FOREIGN KEY(sender) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(post_id) REFERENCES POST(post_id) ON DELETE CASCADE,	-- this should never be updated
	PRIMARY KEY(com_id)
);

CREATE TABLE DM(												-- Direct Message
	msg_id			INT 					AUTO_INCREMENT,		-- message ID number
	sender			VARCHAR(20) 			NOT NULL,		
	receiver		VARCHAR(20) 			NOT NULL,		
	message			VARCHAR(500),							
	dtime			TIMESTAMP				NOT NULL,			-- DM time
	
	FOREIGN KEY(sender) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(receiver) REFERENCES USER(username) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(msg_id) 
);

