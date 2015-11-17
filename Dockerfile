# pyJasper
#
# VERSION               0.0.0

FROM      dockerfile/java:oracle-java7

MAINTAINER Mikhail Petrov <me@mixael.ru>

ADD ./ /usr/local/pyJasper

EXPOSE 5555

ENTRYPOINT /usr/local/pyJasper/pyjasper/backend/pyJasper-httpd.sh -Xms128m -Xmx512m
