# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - Lists files in the current working directory that are not hidden  
`ls -a`  - Lists all files including the hidden ones in the current working directory
`ls -l`  - Lists files in the current working directory in the long format
`ls -lh` - Lists files in long format and human readable file sizes
`ls -lah` - Lists all files in long format with human readable file sizes
`ls -t`  - Lists files by modification time
`ls -Glp` - Lists files in long format with display of grouping information and appends "/" indicator to entry.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -a 
-t
-m 
-l 
-d


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs command can take the output of one command as an input to another command. It is used when there are issues with the piping command and when the user wants to repedeatly execute a certain command. one example of it is: ls | xargs -n 5 echo
This will list the files in the current directory and will display five entries on each line at a time. 

 

