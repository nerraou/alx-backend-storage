-- create index on two fields
-- create index
CREATE INDEX idx_name_first_score ON names(name(1), score);
