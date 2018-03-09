INSERT INTO `users` (id, first_name, last_name,created_at) VALUES (1,'Chris','Baker','2017-12-06 12:16:43'),(2,'Jessica','Davidson','2017-12-06 12:16:59'),(3,'James','Johnson','2017-12-06 12:17:13'),(4,'Diana','Smith','2017-12-06 12:17:34');

INSERT INTO `friendships` (id, user_id, friend_id, created_at) VALUES (1, 1, 2, "2017-12-06 13:43:41"), (2, 1, 3, "2017-12-06 13:43:51"), (3, 1, 4, "2017-12-06 13:44:41"), (4, 4, 1, "2017-12-06  13:45:40"), (5, 3, 1, "2017-12-06 13:47:11"), (6, 2, 1, "2017-12-06 13:48:09");





1 Chris	Baker (1)	Jessica	Davidson (2)
2 Chris	Baker (1)   James	Johnson (3)
3 Chris	Baker (1)   Diana	Smith   (4)  
4 Diana	Smith (4)	Chris	Baker   (1)
5 James	Johnson	(3) Chris	Baker   (1)
6 Jessica	Davidson (2)	Chris	Baker (1)