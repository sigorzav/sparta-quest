1) CASE문 사용
    SELECT ANIMAL_TYPE
         , CASE 
            WHEN NAME IS NULL THEN 'No name'
            ELSE NAME
           END AS NAME
         , SEX_UPON_INTAKE
      FROM ANIMAL_INS 
  ORDER BY ANIMAL_ID      

2) IFNULL문 사용    
    SELECT ANIMAL_TYPE
         , IFNULL(NAME, 'No name') AS NAME
         , SEX_UPON_INTAKE
      FROM ANIMAL_INS 
  ORDER BY ANIMAL_ID

3) IF문 사용 - IF(조건문, TRUE, FALSE)
    SELECT ANIMAL_TYPE
         , IF(NAME IS NULL, 'No name', NAME) AS NAME
         , SEX_UPON_INTAKE
      FROM ANIMAL_INS 
  ORDER BY ANIMAL_ID      
