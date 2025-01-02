# backend

comment: this is a "backend" repo.  right now i have it doing 2 things seemingly.  1 - storing stuff thats needed for creating eck, deploying a cluster, or docker spinning up an es cluster.  2 - source control for things like index templates and sample data.  Might want to split this up long term

#########

next steps

- think about if i need transforms for either latest or trending (as the season goes or from one season to next)
    - games should def be a "stream" aka continuous write, no updates.  w/ transform to get latest
- do i need any field aliases?
- consider teams index - store info from teams.yaml, plus record, plus maybe logo maybe for some cool maps or other displays
- ingest pipeline for teams that sets timestamp value

#########

ECK

###
# setup ECK operator
# https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-deploy-eck.html

> kubectl create -f https://download.elastic.co/downloads/eck/2.14.0/crds.yaml
> kca -f https://download.elastic.co/downloads/eck/2.14.0/operator.yaml

###
# create es and kb cluster

# create namespace and then es/kb cluster in that namespace
> kca -f /Users/j10s/apps/5050club/backend/k8s/namespaces/elastic-clusters.yaml
> kca -f /Users/j10s/apps/5050club/backend/k8s/es_kibana_simple.yaml -n elastic-clusters


###
# authentication

# A default user named elastic is created by default w/ pw stored in k8s secret

> PASSWORD=$(kubectl get secret es-5050club-es-elastic-user -o go-template='{{.data.elastic | base64decode}}')
> echo $PASSWORD

###
# networking - es

# A ClusterIP Service is auto created
> kcg service es-5050club-es-http

# connect from inside the k8s cluster
> curl -u "elastic:$PASSWORD" -k "https://es-5050club-es-http:9200"

# set up port forward to connect from laptop
> kubectl port-forward service/es-5050club-es-http 9200
> curl -u "elastic:$PASSWORD" -k "https://localhost:9200"

###
# networking - kb

# A ClusterIP Service is auto created
> kcg service kb-5050club-kb-http

# set up port forward to connect from laptop
> kubectl port-forward service/kb-5050club-kb-http 5601

# go to browser - https://localhost:5601


!! might require executing this in k3d config to access these things from local

See /Users/j10s/apps/5050club/kubernetes/README.md


##########

docker run -d --name theclub-es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.14.2

curl -X GET -H "Content-Type: application/json" localhost:9200/
curl -X PUT -H "Content-Type: application/json" localhost:9200/_template/cdm_stig_dictionary -u james.byroads -o <file> -d '



users
----------
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| memberid    | int(11)     | NO   | PRI | NULL    | auto_increment |
| memberemail | varchar(50) | NO   | UNI |         |                |
| password    | varchar(50) | NO   |     |         |                |
| userlevel   | int(1)      | NO   |     | 0       |                |
| firstname   | varchar(50) | NO   |     |         |                |
| lastname    | varchar(50) | NO   |     |         |                |
| survivor    | tinyint(4)  | YES  |     | NULL    |                |
| wins        | int(10)     | NO   |     | 0       |                |
| losses      | int(10)     | NO   |     | 0       |                |
| pushes      | int(10)     | NO   |     | 0       |                |
| lonewolf    | int(11)     | YES  |     | 0       |                |
| bonus       | float(5,2)  | YES  |     | NULL    |                |
| points      | float(5,2)  | YES  |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+




games
----------
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| week      | varchar(8)  | YES  |     | NULL    |       |
| gameid    | int(11)     | YES  |     | NULL    |       |
| date      | datetime    | YES  |     | NULL    |       |
| favorite  | varchar(30) | YES  |     | NULL    |       |
| underdog  | varchar(30) | YES  |     | NULL    |       |
| spread    | varchar(30) | YES  |     | NULL    |       |
| ATSwinner | varchar(30) | YES  |     | NULL    |       |
| winner    | varchar(30) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+

+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| date       | datetime    | YES  |     | NULL    |                |
| favorite   | varchar(30) | YES  |     | NULL    |                |
| spread     | varchar(30) | YES  |     | NULL    |                |
| underdog   | varchar(30) | YES  |     | NULL    |                |
| result     | varchar(30) | YES  |     | NULL    |                |
| winner     | varchar(30) | YES  |     | NULL    |                |
| pinnacleid | int(11)     | YES  |     | NULL    |                |
| gameid     | int(11)     | NO   | PRI | NULL    | auto_increment |
+------------+-------------+------+-----+---------+----------------+

game
    id
    source
        id (need a source id and game id?)
        name
    date
    favorite
    spread
    underdog
    spread
    ats_winner
    winner
    home/away?
    goe loc?
    weather?

    see some previous work around this

picks
-------------
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| week     | varchar(7)  | YES  |     | NULL    |       |
| gameid   | tinyint(4)  | YES  |     | NULL    |       |
| memberid | int(11)     | YES  |     | NULL    |       |
| pick     | varchar(30) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
