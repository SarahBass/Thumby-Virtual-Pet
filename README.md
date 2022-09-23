# Thumby-Virtual-Pet
MicroPython Game for Thumby

A Game Created in MicroPython for Thumby that simulates a virtual pet. The virtual pet is a star that lives in a galaxy far, far away! Raise the pet starting from a baby blackhole! The star evolves into a nebula cloud, then finally a star!
Play games , give toys, feed, and take proper care of hygiene. 

The best way to play is to give it a proper balance of all 4. Everytime you feed it , it levels up to a max of 10.

Blackhole Level 0-3
Nebula level 4-7
Star Level 8-9
Final Form Level 10

Final Forms:
Smart Star: Education == 7 or 8 
Super Smart Star: Education > 9 
Super Happy Star: Happy > 8
Happy Star: Happy == 7 or 8 
Average star: Happy == 5 or 6
Sad Star: happy < 5

Variables: Level(Food), Education, Happy, Sick, Sad, Angry
States: Sad, Average, Happy, Super happy

Rules: 
Win a game -> +1 Happy, +1 Education
Lose a game -> +1 Sad 
Food -> + 1 Level, -1 Happy, -1 Sad
Hygene -> +1 Happy, -1 sick
Toy -> +1 Happy -1 Angry
2 toys in a row -> -1 happy, +1 sad
2 hygenes in a row -> -1 happy, +1 Angry
2 food in a row -> +1 Sick

Hygene heals sick
Toys heal anger
food heals sad

Sick && Sad && Angry states == 0 -> Star Happy State
Sick<-Angry<-Sad<-State
if sick > 0 {show sick}
else if angry >0 {show angry}
else if sad > 0 {show sad}
else [show state}


The games are all inspired by LEETCODE Challenges!!

Game 1: Leetcode Roman -> Integer Challenge #0013


