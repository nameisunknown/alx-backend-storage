-- Creating SQL scripts that ranks country origins
-- of brands, ordered by the number of fans

WITH CountryFans AS (
    SELECT
        origin,
        SUM(nb_fans) AS total_fans
    FROM
        bands
    GROUP BY
        origin
)

-- Rank the countries by total fans
SELECT
    origin,
    total_fans,
    RANK() OVER (ORDER BY total_fans DESC) AS rank
FROM
    CountryFans;

