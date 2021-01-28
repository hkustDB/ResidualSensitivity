Copy edge1 FROM '$$$/edge1.csv' WITH DELIMITER AS '|';
Copy edge2 FROM '$$$/edge2.csv' WITH DELIMITER AS '|';
Copy edge3 FROM '$$$/edge3.csv' WITH DELIMITER AS '|';
Copy edge4 FROM '$$$/edge4.csv' WITH DELIMITER AS '|';
Copy edge5 FROM '$$$/edge5.csv' WITH DELIMITER AS '|';
Create table R6 as (Select e1.edge1_from as A, e2.edge1_from as B, e3.edge1_from as C from edge1 e1, edge1 e2, edge1 e3 where e1.edge1_to=e2.edge1_from and e2.edge1_to=e3.edge1_from and e3.edge1_to=e1.edge1_from) union (Select e1.edge2_from as A, e2.edge2_from as B, e3.edge2_from as C from edge2 e1, edge2 e2, edge2 e3 where e1.edge2_to=e2.edge2_from and e2.edge2_to=e3.edge2_from and e3.edge2_to=e1.edge2_from);
