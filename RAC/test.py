#! /usr/bin/python
# -*- encoding: utf-8 -*-

import raclib

# Запуск rac с параметрами

Clusters = raclib.get_rac('/opt/1C/v8.3/x86_64/rac','cluster','list', '192.168.30.185:1545')
#print Clusters

for c in Clusters:
    if c.get('cluster') == '8c5d2670-ff7d-11e7-bd82-005056a421dc':
        print "OK!!! ", c.get('cluster')
