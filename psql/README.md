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


CREATE TYPE game.results.total AS ENUM ('over', 'under', 'push');
CREATE TYPE game.field_type AS ENUM ('grass', 'turf');
CREATE TYPE game.stadium_type AS ENUM ('indoor', 'outdoor', 'retractable');

CREATE TABLE games )
    @timestamp                      date
    game.away_team                  varchar
    game.field_type                 enum
    game.home_team                  varchar
    game.id                         keyword
    game.kickoff                    date
    game.last_updated               date
    game.location                   point   
    game.source                     varchar
    game.stadium_type               emum
    game.completed                  boolean
    game.spread.favorite_odds       float
    game.spread.favorite_points     float
    game.spread.favorite_team       varchar
    game.spread.underdog_odds       float
    game.spread.underdog_points     float
    game.spread.underdog_team       varchar
    game.total.over_odds            float
    game.total.over_under           float
    game.total.under_odds           float
    game.weater.detailed_forecast   varchar
    game.weater.precipitation       long
    game.weater.short_forecast      varchar
    game.weater.temp                long
    game.weater.wind_speed          varchar
    game.results.winner             varchar
    game.results.loser              varchar
    game.results.winning_score      integer
    game.results.losing_score       integer
    game.results.ats_winner         varchar
    game.results.total              enum
    game.results.total_points       integer
);



CREATE TABLE films (
    code        char(5) CONSTRAINT firstkey PRIMARY KEY,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
);

