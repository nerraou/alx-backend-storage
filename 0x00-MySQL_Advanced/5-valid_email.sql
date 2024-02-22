-- set valid_email to false
-- trigger after insert
DELIMITER $$

CREATE TRIGGER set_valid_email_to_false
AFTER INSERT
ON users FOR EACH ROW
BEGIN
    UPDATE users SET valid_email = false WHERE id = NEW.id;
END$$

DELIMITER ;
