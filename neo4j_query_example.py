#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 02:58:16 2019

@author: user
"""

from neo4j import GraphDatabase


driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', '123456789'))



def print_result(tx):
  for record in tx.run("MATCH rel=(u:User)-[r*1..2]->(p:Page) RETURN rel limit 25"):
    print(record)

with driver.session() as session:
    session.read_transaction(print_result)

driver.close()
