    SELECT ANIMAL_TYPE
         , COUNT(1) AS COUNT
      FROM ANIMAL_INS 
     WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
  GROUP BY ANIMAL_TYPE
  ORDER BY ANIMAL_TYPE