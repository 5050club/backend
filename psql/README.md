# Docker

$ docker run -p 5432:5432 --name 5050-postgres -e POSTGRES_PASSWORD=password -d postgres

un: postgres
pw: password

psql -h localhost -p 5432 -U postgres -W


# Field Types from backend > es > component_templates > game.json

@timestamp  -->  date
game.away_team  -->  keyword
game.field_type  -->  keyword
game.home_team  -->  keyword
game.id  -->  keyword
game.kickoff  -->  date
game.last_updated  -->  date
game.location  -->  geo_point
game.source  -->  keyword
game.stadium_type  -->  keyword
game.completed  -->  boolean
game.spread.favorite_odds  -->  float
game.spread.favorite_points  -->  float
game.spread.favorite_team  -->  keyword
game.spread.underdog_odds  -->  float
game.spread.underdog_points  -->  float
game.spread.underdog_team  -->  keyword
game.total.over_odds  -->  float
game.total.over_under  -->  float
game.total.under_odds  -->  float
game.weater.detailed_forecast  -->  text
game.weater.precipitation  -->  long
game.weater.short_forecast  -->  text
game.weater.temp  -->  long
game.weater.wind_speed  -->  text
game.results.winner  -->  keyword
game.results.loser  -->  keyword
game.results.winning_score  -->  short
game.results.losing_score  -->  short
game.results.ats_winner  -->  keyword
game.results.total  -->  keyword
game.results.total_points  -->  short


# Postgres documentation

https://www.postgresql.org/docs/current/index.html

# Enum Types

Postgres supports enum field types.  Those must be defined prior to creating the table.

https://www.postgresql.org/docs/current/datatype-enum.html

CREATE TYPE results_total AS ENUM ('over', 'under', 'push');
CREATE TYPE field_type AS ENUM ('grass', 'turf');
CREATE TYPE stadium_type AS ENUM ('indoor', 'outdoor', 'retractable');

# Create Table

https://www.postgresql.org/docs/current/sql-createtable.html


CREATE TABLE games (
    timestamp                  date,
    away_team                  varchar,
    field_type                 field_type,
    home_team                  varchar,
    id                         varchar PRIMARY KEY,
    kickoff                    date,
    last_updated               date,
    location                   point,   
    source                     varchar,
    stadium_type               stadium_type,
    completed                  boolean,
    spread_favorite_odds       float,
    spread_favorite_points     float,
    spread_favorite_team       varchar,
    spread_underdog_odds       float,
    spread_underdog_points     float,
    spread_underdog_team       varchar,
    total_over_odds            float,
    total_over_under           float,
    total_under_odds           float,
    weater_detailed_forecast   varchar,
    weater_precipitation       integer,
    weater_short_forecast      varchar,
    weater_temp                integer,
    weater_wind_speed          varchar,
    results_winner             varchar,
    results_loser              varchar,
    results_winning_score      integer,
    results_losing_score       integer,
    results_ats_winner         varchar,
    results_total              results_total,
    results_total_points       integer
);


# Insert a document

https://www.postgresql.org/docs/current/dml-insert.html

INSERT INTO games (id, home_team, away_team) VALUES (123, 'Ravens', 'BooBirds');



# TODO

- what other tables do I need? (compare to what I had in mysql)
- should I apply any constraints to tables?

  https://www.postgresql.org/docs/current/ddl-constraints.html