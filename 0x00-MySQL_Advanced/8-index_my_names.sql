-- create index on the first letter of name column
-- create index
CREATE INDEX idx_name_first ON names(name(1));
