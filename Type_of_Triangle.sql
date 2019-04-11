CREATE FUNCTION TriType(p_sideA INT, p_sideB INT, p_sideC INT) RETURNS VARCHAR(14)
    DETERMINISTIC
BEGIN
    DECLARE tri_result varchar(14);

    tri_result = 'Yup!'
    
 RETURN (tri_result); 
END

SELECT ID, TriType(A,B,C) FROM TRIANGLES;