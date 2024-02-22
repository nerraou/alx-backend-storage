-- list glam rock bands
-- use LEAST and COALESCE functions
SELECT band_name, (LEAST(COALESCE(split, 2022), 2022) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
