-- set valid_email to false
-- trigger after insert
DELIMITER $$

CREATE TRIGGER set_valid_email_to_false
BEFORE UPDATE
ON users FOR EACH ROW     
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
