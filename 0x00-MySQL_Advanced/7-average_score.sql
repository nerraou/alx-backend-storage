-- user average score
-- create stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    SET @average_score =  (SELECT AVG(score)
                           FROM corrections
                           WHERE corrections.user_id = user_id);

    UPDATE users
    SET average_score = @average_score;
END$$

DELIMITER ;
