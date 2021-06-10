'''
This is currently not being used. Its purpose is to take a SQL file
and break it by command. This was made because the cursor.execute() from
mysql.connector can only execute one SQL command at a time.
'''

sql = open("/home/ec2-user/environment/database/initTables.sql", "r");

curr_string = ""

for line in sql:
    no_comments = line.split("--")[0];
    
    for char in no_comments:
        
        if(char == ';'):
            curr_string = curr_string + char;
            print(curr_string); # execute sql command(curr_string) here
            curr_string = "";
            
        elif(char == '\t' or char == '\n'):
            curr_string = curr_string + ' ';
            
        else:
            curr_string = curr_string + char;