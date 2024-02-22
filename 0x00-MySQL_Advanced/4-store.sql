-- decrease item quantity after adding order
-- trigger after insert
DELIMITER $$

CREATE TRIGGER decrease_item_quantity     
AFTER INSERT
ON orders FOR EACH ROW     
BEGIN
    UPDATE items SET quantity = quantity - 1 WHERE name LIKE NEW.item_name;
END$$

DELIMITER ;
