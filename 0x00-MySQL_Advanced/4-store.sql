-- decrease item quantity after adding order
-- trigger after insert
DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE name LIKE NEW.item_name;
END$$

DELIMITER ;
