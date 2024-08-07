# Adjacency matrix and influences

## Before reading

Hi. The name's Fullbust. I am a student at EFREI and for a project of Linear Algebra, we had to calculate the influence of talkative students in a classroom and, by using the eigenvector centrality method, we should find where to seat the most talkative students and the most silent ones, in order to have a productive class. This "project" was made in the sole purpose of avoiding the computation of a 40x40 matrix by hand or in MATLAB. For more information on the eigenvector centrality method, please refer to [this wikipedia link](https://en.wikipedia.org/wiki/Eigenvector_centrality).

## The models

We're using classrooms designed in python with arrays where each "1" represent a seat for a student. Feel free to change the order of the class.
We are using two distinct method to calculate the influence of each student :

1. The "direct" method : Students can only influence their direct neighbors, on a line. For example, a student in the middle of a line can only bother the students on his right and his left. A student on the left end of a line can only bother its neighbor on his right.
2. The "all" method : Here, everyone influences everyone. However, the greater the distance between two students, the lighter the influence.
