    SELECT CATEGORY
         , COUNT(CATEGORY)
      FROM (
            SELECT SUBSTR(PRODUCT_CODE, 1, 2) AS CATEGORY
              FROM PRODUCT 
           ) M
  GROUP BY CATEGORY
  ORDER BY CATEGORY

SELECT SUBSTR(PRODUCT_CODE, 1, 2) AS CATEGORY,
       COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT 
GROUP BY CATEGORY # MYSQL에서는 GROUP BY에서 별칭 사용이 가능하다
ORDER BY CATEGORY
