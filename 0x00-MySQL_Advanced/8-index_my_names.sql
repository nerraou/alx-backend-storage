-- create index on the first letter of name column
-- create index
ALTER TABLE names ADD INDEX (name(1));
