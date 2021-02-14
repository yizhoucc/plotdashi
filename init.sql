USE plot_test;
DROP TABLE IF EXISTS test;
CREATE TABLE test(
    dt DATETIME(3) DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
    x  float,
    y  float,
    user int,
    userplot int
    );

DROP TABLE IF EXISTS test_user;
CREATE TABLE test_user(
    user int NOT NULL AUTO_INCREMENT,
    rank int DEFAULT 1 not NULL,
    email varchar(64) not NULL,
    pass varchar(64) not NULL,
    PRIMARY KEY (user)
    );

DROP TABLE IF EXISTS test_rank;
CREATE TABLE test_user(
    rank int not null,
    maxplot int not null,
    savetime DATETIME(3) not null,
    writespeedlimit DATETIME(3) not null,
    datalimit varchar(32)
    PRIMARY KEY (rank)
        );