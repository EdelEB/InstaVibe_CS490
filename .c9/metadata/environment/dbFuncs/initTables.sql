{"filter":false,"title":"initTables.sql","tooltip":"/dbFuncs/initTables.sql","undoManager":{"mark":68,"position":68,"stack":[[{"start":{"row":0,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["","CREATE TABLE USER(\t","    fname \t\t\tVARCHAR(20)\t\t    \tNOT NULL,","\tlname           VARCHAR(20)             NOT NULL,","\tusername        VARCHAR(20)             NOT NULL,","\tpassword        VARCHAR(20),\t\t\t","\temail           VARCHAR(20),        \t","\tadmin_status    SMALLINT                     NOT NULL,       -- 1 : admin , 0 : NOT admin ","\tblock_status    SMALLINT                     NOT NULL,       -- 1 : blocked , 0 : NOT blocked","\t","\tPRIMARY KEY(username)",");","","","CREATE TABLE POST(","\tpostID\t\t\tINT \t\t\t\t\tAUTO_INCREMENT,","\tposter\t\t\tVARCHAR(20) \t\t\tNOT NULL,","\tpTime\t\t\tTIMESTAMP\t\t\t\tNOT NULL,\t\t-- post time","\tsongTitle\t\tVARCHAR(30) \t\t\tNOT NULL,","\tauthor\t\t\tVARCHAR(20)\t\t\t\tNOT NULL,\t\t","\tvideo\t\t\tBLOB\t\t\t\t\tNOT NULL,\t\t-- idk how to store the video. Is it just a hyperlink? !!!!!!!!!!!!!!!!!!!","\tcaption \t\tVARCHAR(500),\t\t\t\t\t\t\t-- caption is optional","\t","\tFOREIGN KEY(poster) REFERENCES USER(username),","\tFOREIGN KEY(",");","","CREATE TABLE COMMENT(","\tcomID\t\t\tINT\t\t\t\t\t\tAUTO_INCREMENT,\t\t-- comment ID number","\tsender\t\t\tVARCHAR(20)\t\t\t\tNOT NULL,\t\t","\tpostID\t\t\tINT\t\t\t\t\t\tNOT NULL,\t\t-- post ID number of post comment is on","\tmessage \t\tVARCHAR(500)\t\t\tNOT NULL,\t\t","\tcTime\t\t\tTIMESTAMP\t\t\t\tNOT NULL,\t\t-- comment time","\t","\tFOREIGN KEY(sender) REFERENCES USER(username),","\tFOREIGN KEY(postID) REFERENCES POST(postID),","\tPRIMARY KEY(comID)",");","","CREATE TABLE DM(\t\t\t\t\t\t\t\t\t\t\t-- Direct Message","\tmsgID\t\t\tINT \t\t\t\t\tAUTO_INCREMENT,\t\t-- message ID number","\tsender\t\t\tVARCHAR(20) \t\t\tNOT NULL,\t\t","\treceiver\t\tVARCHAR(20) \t\t\tNOT NULL,\t\t","\tmessage\t\t\tVARCHAR(500),\t\t\t\t\t\t\t","\tdTime\t\t\tTIMESTAMP\t\t\t\tNOT NULL,\t\t-- DM time","\t","\tFOREIGN KEY(sender) REFERENCES USER(username),","\tFOREIGN KEY(receiver) REFERENCES USER(username),","\tPRIMARY KEY(msgID) ",");",""],"id":1}],[{"start":{"row":11,"column":2},"end":{"row":12,"column":0},"action":"remove","lines":["",""],"id":2}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"remove","lines":["B"],"id":3},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":["O"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["L"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"remove","lines":["B"]}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["i"],"id":4},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["n"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":["t"],"id":5},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["n"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"remove","lines":["i"]}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["B"],"id":6},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["L"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["O"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["B"]}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["/"],"id":8},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["/"]}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["/"],"id":9},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["/"]},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["''"],"id":11}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["'"],"id":12}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"remove","lines":[" "],"id":14},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":["'"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["'"]},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["'"]},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["/"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["/"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["/"]}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":["/"],"id":16},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["/"]},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["/"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["/"],"id":17},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["*"]}],[{"start":{"row":50,"column":2},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":51,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":52,"column":0},"end":{"row":52,"column":1},"action":"insert","lines":["*"],"id":19},{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"insert","lines":["."]}],[{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"remove","lines":["."],"id":20}],[{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"insert","lines":["."],"id":21}],[{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"remove","lines":["."],"id":22}],[{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"insert","lines":["/"],"id":23}],[{"start":{"row":52,"column":2},"end":{"row":53,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"insert","lines":["a"]}],[{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"remove","lines":["a"],"id":25}],[{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"insert","lines":["w"],"id":26},{"start":{"row":53,"column":1},"end":{"row":53,"column":2},"action":"insert","lines":["o"]},{"start":{"row":53,"column":2},"end":{"row":53,"column":3},"action":"insert","lines":["r"]},{"start":{"row":53,"column":3},"end":{"row":53,"column":4},"action":"insert","lines":["d"]},{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"remove","lines":["s"],"id":27},{"start":{"row":53,"column":3},"end":{"row":53,"column":4},"action":"remove","lines":["d"]},{"start":{"row":53,"column":2},"end":{"row":53,"column":3},"action":"remove","lines":["r"]},{"start":{"row":53,"column":1},"end":{"row":53,"column":2},"action":"remove","lines":["o"]},{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"remove","lines":["w"]},{"start":{"row":52,"column":2},"end":{"row":53,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["D"],"id":29},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["E"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["R"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["P"]}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["P"],"id":30},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["R"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["E"]}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["R"],"id":31},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["O"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["P"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":32},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["T"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["A"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["M"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["M"],"id":33},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["A"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["B"],"id":34},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["L"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["L"],"id":35},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["B"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["A"],"id":36},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["B"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["L"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["E"]}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":[" "],"id":37},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["I"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["F"]}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":[" "],"id":38},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["E"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["X"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["I"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["X"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["X"],"id":39}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["S"],"id":40}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":18},"action":"remove","lines":["EXIS"],"id":41},{"start":{"row":1,"column":14},"end":{"row":1,"column":20},"action":"insert","lines":["EXISTS"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":[" "],"id":42}],[{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["U"],"id":43},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["S"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["E"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["R"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":[";"]}],[{"start":{"row":1,"column":26},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":44}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":21},"action":"insert","lines":["DROP TABLE IF EXISTS "],"id":45}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["p"],"id":46},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["o"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"remove","lines":["s"],"id":47},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"remove","lines":["o"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":["p"]}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["P"],"id":48},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["O"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["S"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["T"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":[";"]}],[{"start":{"row":2,"column":26},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":49}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":21},"action":"insert","lines":["DROP TABLE IF EXISTS "],"id":50}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["C"],"id":51},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["O"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["M"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["M"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["E"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["N"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["T"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":[";"]}],[{"start":{"row":3,"column":29},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":52}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":21},"action":"insert","lines":["DROP TABLE IF EXISTS "],"id":53}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["D"],"id":54},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["M"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":[";"]}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["\t"],"id":55}],[{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["O"],"id":56},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["N"]}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":[" "],"id":58},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["N"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["O"]}],[{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["\t"],"id":59}],[{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"remove","lines":[" "],"id":60},{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"remove","lines":[" "]}],[{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"remove","lines":[" "],"id":61},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"remove","lines":[" "]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"remove","lines":[" "],"id":62},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"remove","lines":[" "]},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"remove","lines":[" "]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"remove","lines":[" "]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":[" "]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":[" "],"id":63}],[{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["\t"],"id":64}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["o"],"id":65},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"remove","lines":["n"],"id":66},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":["o"]}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["O"],"id":67},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["N"]}],[{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":[" "],"id":68},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["U"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["P"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":["D"]},{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["A"]},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":["T"]},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["E"]}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":[" "],"id":69},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["C"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["A"]},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["S"]},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["C"]},{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"insert","lines":["A"]},{"start":{"row":8,"column":67},"end":{"row":8,"column":68},"action":"insert","lines":["D"]},{"start":{"row":8,"column":68},"end":{"row":8,"column":69},"action":"insert","lines":["E"]}]]},"ace":{"folds":[{"start":{"row":33,"column":21},"end":{"row":43,"column":0},"placeholder":"..."},{"start":{"row":45,"column":16},"end":{"row":55,"column":0},"placeholder":"..."}],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":19},"end":{"row":6,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1622385260866,"hash":"0b298267b6d4c401981f6dbacdd906cca9c41ac5"}